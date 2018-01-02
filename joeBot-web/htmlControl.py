import sys
import explorerhat
import termios
import tty
from time import sleep

from flask import Flask, render_template, request, url_for, redirect

print("Use the arrow keys to move the robot")
print("Press CTRL-c to quit the program")

# Create an instance of our Flask web application
app = Flask(__name__)

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

# These Flask functions are bound to HTTP routes

# This function simply returns the index.html main page to client
@app.route("/")
def index():
    return render_template("index.html")

# This function deals with HTTP posts made by the client, and controls motor accordingly
@app.route("/control", methods = ["POST"])
def control_rosie():
    control = request.form.get("control")
    if control == "Forward":
        # If too close, disable control to move forwards and log message instead
        move('f')
    elif control == "Reverse":
        move('b')
    elif control == "Right":
        move('r')
    elif control == "Left":
        move('l')
    else:
        print("Stop")
    return redirect(url_for("index"))

if __name__ == "__main__":
    # Start Flask web server, make it accessible across the network
    app.run(host = "0.0.0.0")
