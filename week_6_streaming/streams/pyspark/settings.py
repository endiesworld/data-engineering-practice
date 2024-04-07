import os
import findspark

# Replace "../../../../" with the actual absolute path to your home directory
home_directory = "../../../../../../"
os.environ["SPARK_HOME"] = os.path.join(home_directory, "spark-3.3.2-bin-hadoop3")
spark_python = os.path.join(os.environ["SPARK_HOME"], "python")
py4j_path = os.path.join(spark_python, "lib", "py4j-*.zip")

findspark.init()

import pyspark.sql.types as T

INPUT_DATA_PATH = '../../resources/rides.csv'
BOOTSTRAP_SERVERS = 'localhost:9092'

TOPIC_WINDOWED_VENDOR_ID_COUNT = 'vendor_counts_windowed'

PRODUCE_TOPIC_RIDES_CSV = CONSUME_TOPIC_RIDES_CSV = 'rides_csv'

RIDE_SCHEMA = T.StructType(
    [T.StructField("vendor_id", T.IntegerType()),
     T.StructField('tpep_pickup_datetime', T.TimestampType()),
     T.StructField('tpep_dropoff_datetime', T.TimestampType()),
     T.StructField("passenger_count", T.IntegerType()),
     T.StructField("trip_distance", T.FloatType()),
     T.StructField("payment_type", T.IntegerType()),
     T.StructField("total_amount", T.FloatType()),
     ])