'''For all the pyspark transformations'''

from pyspark.sql.functions import *

# filter the orders dataframe based on order status

def filter_closed_orders(orders_df):
    return orders_df.filter("order_status = 'CLOSED'")


# join the ordersfilterd with customers (on the bases of column customer_id)

def join_orders_customers(orders_df, customers_df):
    return orders_df.join(customers_df, "customer_id")


# do a groupBy on State and do the aggregation

def count_orders_state(joined_df):
    return joined_df.groupBy('state').count()