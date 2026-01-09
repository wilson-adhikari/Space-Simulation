# 🌌 Space Simulation (Pygame)

A simple planetary motion simulation built with **Python** and **Pygame**, visualizing the orbits of the planets around the Sun using Newtonian gravity. [web:1][web:2]

---

## Features

- Real-time 2D simulation of the Sun and 8 planets.
- Newtonian gravity with multi-body interactions.
- Orbit trails for each planet.
- Velocity vectors rendered as arrows.
- Zoom in/out of the whole system.
- Labels for planet names and distance to the Sun (in km). [web:1][web:2]

---

## Physics Overview

The simulation uses **Newton’s law of universal gravitation**: [web:2]

\[
F = G \frac{m_1 m_2}{r^2}
\]

- \( G = 6.67428 \times 10^{-11} \, N·m^2/kg^2 \)
- Distances are in meters; 1 AU \(= 149.6 \times 10^6 \, km\). [web:7][web:10]
- Time step: 1 day per frame (`TIMESTEP = 3600 * 24`).
- Positions and velocities are updated with basic Euler integration. [web:2]

---

## Planets Included

Initial distances and velocities are based on approximate real orbital parameters. [web:1][web:2]

| Body    | Role | Distance (AU) | Speed (km/s) |
|---------|------|---------------|--------------|
| Sun     | Star | 0.000         | 0.00         |
| Mercury | Planet | 0.387       | 47.4         |
| Venus   | Planet | 0.723       | 35.02        |
| Earth   | Planet | 1.000       | 29.78        |
| Mars    | Planet | 1.524       | 24.08        |
| Jupiter | Planet | 5.203       | 13.06        |
| Saturn  | Planet | 9.537       | 9.68         |
| Uranus  | Planet | 19.191      | 6.80         |
| Neptune | Planet | 30.069      | 5.43         |

---

## Installation

1. Make sure **Python 3.8+** is installed. [web:6]
2. Install Pygame:

```bash
pip install pygame
