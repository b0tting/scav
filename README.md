## Scav

A simple scavenger hunt browser game. Players use a mobile device as a client, the number of steps to the next goal being displayed on the screen. Very suiteable for children. 

You place a map of x,y locations (found, for example, using maps.google.com) and image files with cryptic images. The clients will open the browser address and see the number of steps left to the goal. After walking, the screen will flash and the next location is loaded. This continues until the players reach the final location. Please take this lesson learned: do not give your toddler your expensive smart phone because he or she will start running the moment the child understands how the number of steps work. 

There's no session management or such. I've added a hidden button on the top-right of the screen to skip to the next location. You can also add a ?debug parameter to the URL to get full debug information on location, calculated distances etcetera. 

!["Never mind those 10.000 steps, screenshot taken while 5 kilometers away or so"](https://github.com/b0tting/scav/blob/master/screenshots/scav.png?raw=true)

## Installation
This game uses Flask, so: 
pip install flask 

Change the port number and whatnots in the scavhunt_properties.py file. Just start with python and open the context root (default: port 83) on a phone to start. Note that certain desktop browsers hide the "Allow this page to view my location" access question. 
