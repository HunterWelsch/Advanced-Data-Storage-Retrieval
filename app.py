#import dependencies 
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#set up the database
engine = create_engine("sqlite:///hawaii.sqlite")

#automap database
Base = automap_base()

#reflect the database
Base.prepare(engine, reflect=True)

#create variable
measurement = Base.classes.measurement
station = Base.classes.station

#create a session link
session = Session(engine)

#create flask app
app = Flask(__name__)

#define welcome route
@app.route("/")

def welcome():
        return(
        f"Welcome to the Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start/end<br/>"
        )

if __name__ == '__main__':
    app.run(debug=True)    