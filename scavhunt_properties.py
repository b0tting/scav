## Run the Flask webserver in debug mode?
debug=True

## Port number for the web server
port=83

## Listen address, use 0.0.0.0 for all addresses
listener="0.0.0.0"

## A Python list of locations
locations = [
    ## Auto
        {"next_lat":51.998875,"next_long":4.326210,"imgUrl":"/static/locations/auto.jpg", "next_rank":1},
    ## Voetbalplein
        {"next_lat":52.000166,"next_long":4.325660,"imgUrl":"/static/locations/voetbal.png", "next_rank":2},
    ## Galjoen
        {"next_lat":52.002721,"next_long":4.325757,"imgUrl":"/static/locations/galjoen.jpg", "next_rank":3},
    ## Heuvel
        {"next_lat":52.000275,"next_long":4.326729,"imgUrl":"/static/locations/heuvel.png", "next_rank":4},
    ## Pons romanus
        {"next_lat":52.028200,"next_long":4.288328,"imgUrl":"/static/locations/pons.png", "next_rank":5},
    ]

## The "won" location, used as the final destination
won = {"next_lat":51.999346,"next_long":4.326040,"imgUrl":"/static/locations/award.jpg", "next_rank":-1}

