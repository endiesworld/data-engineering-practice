## Running pyspark

Before running pysaprk on a jupyter notebook, you need to export some environment variables to point jupyter to the pyspark directory.

Run the below code directoly on the directory where you want to run the jupyter notebook from

>> export PYTHONPATH="${SPARK_HOME}/python/:$PYTHONPATH"
>> export PYTHONPATH="${SPARK_HOME}/python/lib/py4j-0.10.9.5-src.zip:$PYTHONPATH"

<!-- Make sure that the version under ${SPARK_HOME}/python/lib/ matches the filename of py4j or you will encounter ModuleNotFoundError: No module named 'py4j' while executing import pyspark.

For example, if the file under ${SPARK_HOME}/python/lib/ is py4j-0.10.9.3-src.zip, then the export PYTHONPATH statement above should be changed to --!>