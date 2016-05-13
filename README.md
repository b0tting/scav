## Scav

A simple scavenger hunt browser game. Players use a mobile device as a client, the number of steps to the next goal being displayed on the screen. Very suiteable for children. 

There's no session management or such. I've added a hidden button on the top-right of the screen to skip to the next location. You can also add a ?debug parameter to the URL to get full debug information on location, calculated distances etcetera. 

!["Never mind those 10.000 steps, screenshot taken while 5 kilometers away or so"](https://github.com/b0tting/scav/blob/master/screenshots/scav.png?raw=true)

## Installation
This game uses Flask, so: 
pip install flask 

Change the port number and whatnots in the scavhunt_properties.py file. Just start with python and open the context root (default: port 83) on a phone to start. Note that certain desktop browsers hide the "Allow this page to view my location" access question. 
