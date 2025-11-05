
---
```python
from time import sleep
from gpiozero import Servo, Button
from gpiozero.pins.lgpio import LGPIOFactory

factory = LGPIOFactory()  # libgpiod-based backend

# SG90-friendly pulse limits (trim if buzzing)
servo = Servo(18,
              min_pulse_width=0.0006,  # 0.6 ms
              max_pulse_width=0.0023,  # 2.3 ms
              pin_factory=factory)

button_open  = Button(17, pull_up=True, pin_factory=factory)  # to GND
button_close = Button(27, pull_up=True, pin_factory=factory)  # to GND

def move_to_90():
    print("→ 90°")
    servo.max()

def move_to_0():
    print("→ 0°")
    servo.min()

button_open.when_pressed  = move_to_90
button_close.when_pressed = move_to_0

print("GPIO17=90°, GPIO27=0°. CTRL+C to exit.")
while True:
    sleep(0.1)
