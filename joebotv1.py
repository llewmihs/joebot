import explorerhat
from time import sleep

def move(direction):
    if direction == "f":
        print("Moving forward...")
        explorerhat.motor.one.forward()
        explorerhat.motor.two.forward()
        sleep(1)
        explorerhat.motor.one.stop()
        explorerhat.motor.two.stop()
    if direction == "b":
        explorerhat.motor.one.backward()
        explorerhat.motor.two.backward()
        sleep(1)
        explorerhat.motor.one.stop()
        explorerhat.motor.two.stop()
        print("Moving backward...")
    if direction == "l":
        print("turning left...")
        explorerhat.motor.one.forward()
        explorerhat.motor.two.backward()
        sleep(0.5)
        explorerhat.motor.one.stop()
        explorerhat.motor.two.stop()
    if direction == "r":
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