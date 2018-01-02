import explorerhat
from time import sleep

def move(direction):
    if direction == "forward":
        print("Moving forward...")
        explorerhat.motor.one.forward()
        explorerhat.motor.two.forward()
        sleep(0.5)
        explorerhat.motor.one.stop()
        explorerhat.motor.two.stop()
    if direction == "backward":
        explorerhat.motor.one.backward()
        explorerhat.motor.two.backward()
        sleep(0.5)
        explorerhat.motor.one.stop()
        explorerhat.motor.two.stop()
        print("Moving backward...")
    if direction == "left":
        print("turning left...")
        explorerhat.motor.one.forward()
        explorerhat.motor.two.backward()
        sleep(0.5)
        explorerhat.motor.one.stop()
        explorerhat.motor.two.stop()
    if direction == "right":
        print("Turning right...")
        explorerhat.motor.one.backward()
        explorerhat.motor.two.forward()
        sleep(0.5)
        explorerhat.motor.one.stop()
        explorerhat.motor.two.stop()

if __name__ == "__main__":
    while True:
        direction = input()
        move(direction)