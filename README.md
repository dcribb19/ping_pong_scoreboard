# Ping Pong Scoreboard
## Hardware
- [64x32 RGB LED Matrix - 5mm pitch](http://www.adafruit.com/product/2277#tutorials)
- [Raspberry Pi Zero WH (Zero W with Headers)](http://www.adafruit.com/product/3708#tutorials)
- [Adafruit RGB Matrix Bonnet for Raspberry Pi](http://www.adafruit.com/product/3211#tutorials)
- [Pimoroni HAT Hacker HAT](http://www.adafruit.com/product/4673#tutorials)
- [5V 4A (4000mA) switching power supply](http://www.adafruit.com/product/1466#tutorials)
- [Premium Female/Female Jumper Wires - 20 x 3" (75mm)](http://www.adafruit.com/product/1951#tutorials)
- SD Card
### IR Version
- [IR (Infrared) Receiver Sensor](http://www.adafruit.com/product/157#tutorials)
- [Mini Remote Control](http://www.adafruit.com/product/389#tutorials)
### RF Version
- [Keyfob 4-Button RF Remote Control - 315MHz](http://www.adafruit.com/product/1095#tutorials)
- [Simple RF M4 Receiver - 315MHz Momentary Type](http://www.adafruit.com/product/1096#tutorials)


## Pi Zero Setup
1. [Install OS on to SD card.](https://learn.adafruit.com/raspberry-pi-zero-creation/install-os-on-to-sd-card)
- I used the [Raspberry Pi Imager](https://www.raspberrypi.org/software/) to install Raspberry Pi OS Lite.
2. [Configure WIFI and Enable SSH](https://learn.adafruit.com/raspberry-pi-zero-creation/text-file-editing)
3. [Ping Pi Zero](https://learn.adafruit.com/raspberry-pi-zero-creation/give-it-life-1) to make sure it has connected to network.
- I'm using Windows, so I needed to install [Bonjour](https://learn.adafruit.com/bonjour-zeroconf-networking-for-windows-and-linux/#microsoft-windows).
4. ssh into Pi Zero.
````
ssh pi@raspberrypi.local
````
- Default Password is raspberry
5. [Change default password](https://www.raspberrypi.org/documentation/configuration/security.md)
6. System Update. Run these 2 commands:
````
sudo apt-get update
sudo apt-get upgrade
````
7. Take a look at general system configuration.
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

### Install OpenSign Library
````
sudo apt install -y git python3-dev python3-pillow python3-pip libatlas-base-dev libtiff-dev libtiff5-dev libopenjp2-7-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk libharfbuzz-dev libfribidi-dev libxcb1-dev

sudo pip3 install opensign
````

### Install Adafruit RGB Matrix Bonnet
````
curl -O https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/rgb-matrix.sh

sudo bash rgb-matrix.sh
````

### Install [Adafruit-Blinka](https://pypi.org/project/Adafruit-Blinka/) (IR Version)
````
sudo pip3 install Adafruit-Blinka
````

## IR Sensor
### Wire it Up
- Pin 1: Output
- Pin 2: Ground
- Pin 3: VCC, Connect to 3-5V

## Transfer file(s) to pi via scp
```
scp (INSERT FILENAME HERE) pi@(INSERT IP ADDRESS OF PI HERE):
````

## Run program
````
sudo python3 scoreboard.py
````

## Start on boot.
````
sudo nano /etc/rc.local
````
Insert new line right before exit 0
````
sudo python3 /home/pi/scoreboard.py &
````

#### Shutdown command
````
sudo shutdown -h now
````
