# Pi Servo – Two Button Control (0° / 90°)

Control a 9g SG90 servo with **two buttons** on a Raspberry Pi:
- **Button 1 (GPIO17)** → moves servo to **90°**
- **Button 2 (GPIO27)** → moves servo to **0°**

Supports modern Pi GPIO stacks:
- Primary: **lgpio** backend (libgpiod)
- Fallback: native backend (software PWM; may jitter)

---

## Hardware

- Raspberry Pi (any model with GPIO)
- SG90 9g servo
- 2× momentary push buttons
- Jumper wires, breadboard

### Wiring
- **Servo**: Red → 5V (Pin 2/4), Brown/Black → GND, Orange → **GPIO18 (Pin 12)**
- **Buttons** (using internal pull-ups):
  - Button 1: one leg → **GPIO17 (Pin 11)**, other leg → **GND**
  - Button 2: one leg → **GPIO27 (Pin 13)**, other leg → **GND**
- Strongly recommended: **external 5V** for servo (share ground with Pi)

