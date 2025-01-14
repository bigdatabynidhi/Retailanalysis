''' To create spark dataframes'''

from lib import ConfigReader 

#defining customers schema

def get_customers_schema():
    schema = "customer_id int,customer_fname string,customer_lname string,username string,password string,address string,city string,state string,pincode string"
    return schema

# creating customers dataframe
def read_customers(spark,env): # here passing spark i.e, spark session and env i.e, local or test or prod.
    conf = ConfigReader.get_app_config(env) # reading the configuration from ConfigReader.py
    customers_file_path = conf["customers.file.path"] # conf is dictionary here and passing keys here.
    return spark.read \
        .format("csv") \
        .option("header", "true") \
        .schema(get_customers_schema()) \
        .load(customers_file_path)

#defining orders schema
def get_orders_schema():
    schema = "order_id int,order_date string,customer_id int,order_status string"
    return schema

#creating orders dataframe
def read_orders(spark,env): # here passing spark i.e, spark session and env i.e, local or test or prod.
    conf = ConfigReader.get_app_config(env) # here passing spark i.e, spark session and env i.e, local or test or prod.
    orders_file_path = conf["orders.file.path"] # here passing spark i.e, spark session and env i.e, local or test or prod. 
    return spark.read \
        .format("csv") \
        .option("header", "true") \
        .schema(get_orders_schema()) \
        .load(orders_file_path)

