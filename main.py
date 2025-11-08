import pygame
import sys
import math
from pygame.locals import *

pygame.init()

FONT = pygame.font.SysFont("comicsans", 16)
ZOOM_FACTOR = 1.1

# Colors
DARK_GREY = (80, 78, 81)
LIGHT_GREY = (200, 200, 200)
ORANGE = (255, 165, 0)
LIGHT_BLUE = (173, 216, 230)
DARK_BLUE = (0, 0, 139)
DARK_GREEN = (0, 100, 0)
DARK_RED = (139, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Planet Simulation")

class Planet:
    AU = 149.6e6 * 1000  # Astronomical unit in meters
    G = 6.67428e-11      # Gravitational constant
    SCALE = 250 / AU     # 1 AU = 250 pixels
    TIMESTEP = 3600 * 24 # 1 day

    def __init__(self, x, y, radius, color, mass,name=None):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0
        self.x_vel = 0
        self.y_vel = 0
        self.name = name
        

    def draw(self, win):
        x = self.x * self.SCALE + WIN.get_width() / 2
        y = self.y * self.SCALE + WIN.get_height() / 2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                px, py = point
                px = px * self.SCALE + WIN.get_width() / 2
                py = py * self.SCALE + WIN.get_height() / 2
                updated_points.append((px, py))
            pygame.draw.lines(win, self.color, False, updated_points, 2)

        if not self.sun:
            distance_text = FONT.render(f"{round(self.distance_to_sun/1000, 1)}km", 1, WHITE)
            win.blit(distance_text, (x - distance_text.get_width()/2, y - distance_text.get_height()/2))

        pygame.draw.circle(win, self.color, (int(x), int(y)), self.radius)

        if self.name:
            name_text = FONT.render(self.name, 1, WHITE)
            win.blit(name_text, (x - name_text.get_width()/2, y - self.radius - 15))

                                 
    def attraction(self, other):
        distance_x = other.x - self.x
        distance_y = other.y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.sun:
            self.distance_to_sun = distance

        force = self.G * self.mass * other.mass / distance**2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y

    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue
            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP

        self.orbit.append((self.x, self.y))
    def draw_velocity_vector(self, win):
        x = self.x * self.SCALE + WIN.get_width() / 2
        y = self.y * self.SCALE + WIN.get_height() / 2
        scale = .00005
        
        end_x = x + self.x_vel * scale
        end_y = y + self.y_vel * scale
        
        pygame.draw.line(win, WHITE, (x, y), (end_x, end_y), 2)
        angle = math.atan2(self.y_vel, self.x_vel)
        
        arrow_size = 5
        left = (end_x + arrow_size * math.cos(angle - math.pi / 6),
                end_y + arrow_size * math.sin(angle - math.pi / 6))
        right = (end_x + arrow_size * math.cos(angle + math.pi / 6),
                 end_y + arrow_size * math.sin(angle + math.pi / 6))
        
        pygame.draw.polygon(win, WHITE, [left, (end_x, end_y), right])
   
        
        
        
        
def main():
    clock = pygame.time.Clock()
    run = True

    # Create planets
    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30,name="Sun")
    sun.sun = True
    mercury = Planet(0.387 * Planet.AU, 0, 8, DARK_GREY, 3.30 * 10**23,name="Mercury")
    mercury.y_vel = -47.4 * 1000
    venus = Planet(0.723 * Planet.AU, 0, 14, WHITE, 4.8685 * 10**24,name="Venus")
    venus.y_vel = -35.02 * 1000
    earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10**24,name="Earth")
    earth.y_vel = 29.783 * 1000
    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10**23,name="Mars")
    mars.y_vel = 24.077 * 1000
    jupiter = Planet(5.203 * Planet.AU, 0, 13, ORANGE, 1898.13 * 10**24,name="Jupiter")
    jupiter.y_vel = 13.06 * 1000
    saturn = Planet(9.537 * Planet.AU, 0, 11, LIGHT_GREY, 568.32 * 10**24,name="Saturn")
    saturn.y_vel = 9.68 * 1000
    uranus = Planet(19.191 * Planet.AU, 0, 13, LIGHT_BLUE, 86.813 * 10**24,name="Uranus")
    uranus.y_vel = 6.8 * 1000
    neptune = Planet(30.069 * Planet.AU, 0, 13, DARK_BLUE, 102.413 * 10**24,name="Neptune")
    neptune.y_vel = 5.43 * 1000

    planets = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

    while run:
        clock.tick(60)
        WIN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_EQUALS or event.key == pygame.K_PLUS:
                    Planet.SCALE *= ZOOM_FACTOR
                elif event.key == pygame.K_MINUS:
                    Planet.SCALE /= ZOOM_FACTOR


        for planet in planets:
            planet.update_position(planets)
            planet.draw_velocity_vector(WIN)
            planet.draw(WIN)

        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()