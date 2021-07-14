# Ping Pong Scoreboard
## Hardware

## Pi Zero Setup
1. Install OS on to SD card.
- I used the Raspberry Pi Imager to install Raspberry Pi OS Lite.
- https://learn.adafruit.com/raspberry-pi-zero-creation/install-os-on-to-sd-card
2. Configure WIFI, Enable UART, and Enable SSH
- https://learn.adafruit.com/raspberry-pi-zero-creation/text-file-editing
- I don't think that I'll be using UART, but it's only 2 lines added to bottom of config.txt file.
3. Ping Pi Zero to make sure it has connected to network.
- https://learn.adafruit.com/raspberry-pi-zero-creation/give-it-life-1
- I'm using Windows, so I needed to install [Bonjour](https://learn.adafruit.com/bonjour-zeroconf-networking-for-windows-and-linux/#microsoft-windows).
4. ssh into Pi Zero.
````
ssh pi@raspberrypi.local
````
5. System Update. Run these 2 commands:
````
sudo apt-get update
sudo apt-get upgrade
````
6. Take a look at general system configuration.
````
sudo raspi-config
````

## Install Python and Required Packages
```
sudo apt-get install python3
sudo apt-get install python3-gpiozero

sudo apt install git
git clone https://www.github.com/hzeller/rpi-rgb-led-matrix.git

sudo apt install libgraphicsmagick++-dev libwebp-dev

cd rpi-rgb-led-matrix
make

cd rpi-rgb-led-matrix/bindings/python
make build-python PYTHON=$(which python3)
sudo make install-python PYTHON=$(which python3)
````

## Install OpenSign Library
````
sudo apt install -y git python3-dev python3-pillow python3-pip libatlas-base-dev libtiff-dev libtiff5-dev libopenjp2-7-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk libharfbuzz-dev libfribidi-dev libxcb1-dev

sudo pip3 install opensign
````

## Install Adafruit RGB Matrix Bonnet
````
curl -O https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/rgb-matrix.sh

sudo bash rgb-matrix.sh
````

### Transfer file(s) to pi via scp
```
scp (INSERT FILENAME HERE) pi@(INSERT IP ADDRESS OF PI HERE):
````

### Run program
````
sudo python3 (INSERT FILENAME HERE)
````

After testing, I want the scoreboard to start up on boot.
Instructions:
````
sudo nano /etc/rc.local
````
Insert new line right before exit 0
````
sudo python3 /home/pi/scoreboard.py &
````

#### Shutdown
````
sudo shutdown -h now
````
