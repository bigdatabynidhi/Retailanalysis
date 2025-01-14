''' Entry point for the application
 or it is like rapper or stich everything together and tell what to do and when (of all mentioned in another folders are configs,lib,data)and also it is not inside any folder and directly under project folder '''

import sys
from lib import DataManipulation, DataReader, Utils
from pyspark.sql.functions import *

if __name__ == '__main__':
    
    if len(sys.argv) < 2:
        print("Please specify the environment")
        sys.exit(-1)

job_run_env = sys.argv[1] #Job run for enviornment and here env will be local,test or prod.

print("Creating Spark Session")

spark = Utils.get_spark_session(job_run_env) # calling utlity function having function name get_spark_session which is already defined and passing enviornment name under spark.

print("Created Spark Session")

orders_df = DataReader.read_orders(spark,job_run_env) # calling datareader function and passing spark and enviornment name here and capturing it inside orders_df.

orders_filtered = DataManipulation.filter_closed_orders(orders_df) # calling datamanipulation function and passing orders_df and capturing it inside orders_filtered.

customers_df = DataReader.read_customers(spark,job_run_env) # calling datareader function and passing spark and enviornment name here and capturing it inside customers_df.

joined_df = DataManipulation.join_orders_customers(orders_filtered,customers_df) # calling datamanipulation function and passing orders_filtered and customers_df capturing it inside joined_df.

aggregated_results = DataManipulation.count_orders_state(joined_df)# calling datamanipulation function and passing joined_df and capturing it inside aggregated_results.

aggregated_results.show() # calling show function for final aggregated_results.

print("end of main")
