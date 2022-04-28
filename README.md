Professional Skills 1 

1.	What are you going to make?

Personalized messages with face recognition and email notifications.

2.	Who are you going to make it for?

For me and my family

3.	Why are you going to make it?

My family goes always in and out, to work or to study, I would like to welcome them when they arrive home.

4.	How are you going to make it?
4.1.	Description

The purpose of this project is to send welcome messages, ask to turn on or off the lights, at the moment camera recognize a member of my family, an email will be send to me, and the text message will be sent to their phone.

4.2.	Hardware Materials:

-	Raspberry pi 4
-	Rpi Camera v2 8 megapixels
-	LDR sensor
-	Resistor of 1k ohm
-	USB Cable, Type A to type C
-	16 Gb micro SD (min)
-	Case for camera
-	Case for Raspberry pi

4.3.	Software and Platforms

-	Open CV
-	Python 3.7+ & Flask
-	Face recognition and dlib
-	Numpy
-	Smtplib (To send emails)
-	Twilio (To send text messages)

4.4.	Setup Procedure:
-	Setup Raspberry pi with “Pi Imager” select the Operating System “Raspberry Pi OS (Legacy)”
 
-	Connect Rpi Camera to Raspberry pi
 
-	Connect LDR on GPIO17 (BCM)and resistor of 1k Ohm to Breadboard, and Breadboard to Raspberry pi 4

-	Install and use Putty for the following part

Upgrade python to 3.8
See what version of python you have  with : python -V

Upgrade with : https://itheo.tech/install-python-38-on-a-raspberry-pi

Install one at a time:

	sudo apt-get update
	sudo apt-get upgrade
	sudo apt-get install build-essential
	sudo apt-get install cmake
	sudo apt-get install gfortran
	sudo apt-get install git
	sudo apt-get install wget
	sudo apt-get install curl
	sudo apt-get install graphicsmagick
	sudo apt-get install libgraphicsmagick1-dev
	sudo apt-get install libatlas-base-dev
	sudo apt-get install libavcodec-dev
	sudo apt-get install libavformat-dev
	sudo apt-get install libboost-all-dev
	sudo apt-get install libgtk2.0-dev
	sudo apt-get install libjpeg-dev
	sudo apt-get install liblapack-dev
	sudo apt-get install libswscale-dev
	sudo apt-get install pkg-config
	sudo apt-get install python3-dev
	sudo apt-get install python3-numpy
	sudo apt-get install python3-pip
	sudo apt-get install zip
	sudo apt-get clean

-	Install the following:
	sudo apt-get install python3-picamera
	sudo pip3 install --upgrade picamera[array]
-	Increase the SWAP FILE
	sudo nano /etc/dphys-swapfile
	Change CONF_SWAPSIZE=100 to CONF_SWAPSIZE=1024 and save / exit nano
-	Git clone and install dlib library
	mkdir -p dlib
	git clone -b 'v19.6' --single-branch https://github.com/davisking/dlib.git dlib/
	cd ./dlib
	sudo apt-get install cmake
	mkdir build; cd build; cmake .. ; cmake –build
-	Install dlib via pip3
	pip3 install dlib
-	Decrease the SWAP Size:
	sudo nano /etc/dphys-swapfile
	Change CONF_SWAPSIZE=1024 to CONF_SWAPSIZE=100 and save / exit nano
-	Install supporting dlib libraries:
	pip3 install numpy
	pip3 install scikit-image
	sudo apt-get install python3-scipy
	sudo apt-get install libatlas-base-dev
	sudo apt-get install libjasper-dev
	sudo apt-get install libqtgui4
	sudo apt-get install python3-pyqt5
	sudo apt install libqt4-test
	pip3 install opencv-python==3.4.6.27
	pip3 install face_recognition
-	Clone the Face recognition library:
	git clone --single-branch https://github.com/ageitgey/face_recognition.git
	cd ./face_recognition/examples && python3 facerec_on_raspberry_pi.py
	python3 facerec_on_raspberry_pi.py
-	SING UP to Twilio
-	Install Twilio libraries 
	sudo pip3 install twilio

-	Base code for Twilio:

from twilio.rest import Client
account_sid ="XXXXXXX" # Put your Twilio account SID here
auth_token ="XXXXXXX" # Put your auth token here
client = Client(account_sid, auth_token)
message = client.api.account.messages.create(
to="+#####", # Put your cellphone number here
from_="+######", # Put your Twilio number here
body="This is my message that I am sending to my phone!")

-	Install SMTP
	pip install secure-smtplib
-	Configure the SMTP 
	sudo nano /etc/ssmtp/ssmtp.conf
	ADD this:

Hostname=xxxx #Put hostname of raspberry
AuthUser= xxxx@xxx.com #Put your email account
AuthPass= xxxxxx #Password of email account
UseSTARTTLS=YES


-	Allowing Gmail SMTP Access for Accounts with Standard Authentication
-	In less secure app access turn “ON” Allow less secure apps

5.	References:

-	https://www.electroniclinic.com/raspberry-pi-send-email-using-python/
-	https://smartbuilds.io/installing-face-recognition-library-on-raspberry-pi-4/
-	https://pypi.org/project/face-recognition/
-	http://thezanshow.com/electronics-tutorials/raspberry-pi/tutorial-43
-	https://iotdesignpro.com/projects/sending-smtp-email-using-raspberry-pi

