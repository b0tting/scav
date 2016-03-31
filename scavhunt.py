from flask import Flask, render_template, jsonify
from scavhunt_properties import *

app = Flask(__name__)

@app.route('/next/<mycurrent>')
def next_target(mycurrent):
    current = int(mycurrent)

    ## If no location was given, default to the first one in the list
    nextLocation = locations[0]

    if(current > 0):
        ## Search for the given rank in the list
        ## If we can find one, return the position that follows. If there are
        ## no more locations left, send the "won" location and image. 
        i = 0;
        while i < len(locations):
            location = locations[i]
            if location["next_rank"] == current:
                if (i+1) < len(locations):
                    nextLocation = locations[i+1]
                    break
                else:
                    nextLocation = won
            i = i + 1
    return jsonify(nextLocation)

@app.route('/')
def scavhunt():
    return render_template('scav.html')

if __name__ == '__main__':
    app.debug = debug
    app.run(host=listener, port=port)
