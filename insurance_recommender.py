### Imports [Please have these libraries installed wherever you are using in your flutter/flask environment]

import numpy as np
import random
from flask import Flask
from flask import jsonify
from flask import request
# Critical Imports for running the model 

from tensorflow import keras
import tensorflow as tf

#you are required to Unzip the bayesian_nn.zip & put the path of the folder here (folder name is bayesian_nn)

  
  # ======================================================================4
  
  ## Flask Code 
    
app = Flask(__name__)
  
@app.route("/")
def hello_api():
  return "Welcome to Heroku App :: InsureBuddy"
  
app.run()
