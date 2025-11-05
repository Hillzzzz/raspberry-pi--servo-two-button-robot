from time import sleep
from gpiozero import Servo, Button
from gpiozero.pins.native import NativeFactory

factory = NativeFactory()  # software PWM; may jitter

servo = Servo(18,
              min_pulse_width=0.0006,
              max_pulse_width=0.0023,
              pin_factory=factory)

button_open  = Button(17, pull_up=True)
button_close = Button(27, pull_up=True)

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
