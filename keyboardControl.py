import sys
import explorerhat
import termios


print("Use the arrow keys to move the robot")
print("Press CTRL-c to quit the program")

UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3

def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    if ch == '0x03':
        raise KeyboardInterrupt
    return ch

def readkey(getchar_fn=None):
    getchar = getchar_fn or readchar
    c1 = getchar()
    if ord(c1) != 0x1b:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5b:
        return c1
    c3 = getchar()
    return ord(c3) - 65  # 0=Up, 1=Down, 2=Right, 3=Left arrows

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

while True:
    keyp = readkey()
    if keyp == UP:
        move('f')
    elif keyp == DOWN:
        move('b')
    elif keyp == RIGHT:
        move('r')
    elif keyp == LEFT:
        move('l')
    elif ord(keyp) == 3:
        break
