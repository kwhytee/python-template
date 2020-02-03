"""Progam to run module1.Logic1 example
"""
# Example of flake8 violation
# import os

# 3rd party libs
from pyspark.sql import SparkSession

# RI libs
from template_pkg.module1 import Logic1


def debug():
    """Function to create Logic1 object and run methods
    """
    # Example of black violation:

    #    spark = SparkSession \
    #        .builder \
    #        .appName("Python template") \
    #        .getOrCreate()

    spark = SparkSession.builder.appName("Python template").getOrCreate()

    dataframe = spark.createDataFrame([(1, 1, 100), (1, 2, 200), (1, 3, 0)], ["key_a", "key_b", "vol_a"])

    logic1 = Logic1(dataframe)
    logic1.get_zero_vol().show()

    # Example of bandit violation
    my_secret = "password"
    print(my_secret)


if __name__ == "__main__":
    debug()
