''' To read the config files'''

import configparser
from pyspark import SparkConf

# loading the application configs in python dictionary
def get_app_config(env):  # here env means what env want to call like local,test,prod.
    config = configparser.ConfigParser()
    config.read("configs/application.conf")
    app_conf = {} # creating empty dictionary
    for (key, val) in config.items(env): # keep iterating the key values from above path
        app_conf[key] = val
    return app_conf

# loading the pyspark configs and creating a spark conf object
def get_pyspark_config(env):
    config = configparser.ConfigParser()
    config.read("configs/pyspark.conf")
    pyspark_conf = SparkConf() # creating a spark object  so that we can pass the same when creating spark session.
    for (key, val) in config.items(env):
        pyspark_conf.set(key, val)
    return pyspark_conf
