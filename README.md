# joebot
Joe's Roboto

Start with Raspbian Lite.

Install git `sudo apt install git`

Change the hostname:

`sudo nano /etc/hosts` - replace raspberrypi with your desired hostname.

Then `sudo nano /etc/hostname` - replace raspberrypi with same hostname. Then reboot.

Change the password - `passwd`

Set python3 as default:

edit `sudo nano ~/.bashrc` file

add `alias python=python3`

Save then update `source ~/.bashrc`

Check with `python -V`

Install the explorer hat:

`sudo apt-get install python3-explorerhat` 

Turn on I2C

`sudo rasp-config` it's in Networking.