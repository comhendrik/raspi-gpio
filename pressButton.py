from gpiozero import LED, Button

led = LED(17)
button = Button(2)
counter = 0

while True:
    if button.is_pressed:
        led.on()
        counter += 1
        print(counter)
        button.wait_for_release()
        led.off()
