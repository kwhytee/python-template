"""Module to demonstrate example class containing pyspark transformation
"""
from pyspark.sql.functions import col  # pylint: disable=E0611
from quinn import validate_presence_of_columns


class Logic1:
    """Class to demonstrate pyspark transformation

    Attributes:
        input_dataframe: A dataframe containing the columns key_a, key_b and vol_a
    """

    KEY_COL1_NAME = "key_a"
    KEY_COL2_NAME = "key_b"
    VOL_COL_NAME = "vol_a"
    EXPECTED_COLS = [KEY_COL1_NAME, KEY_COL2_NAME, VOL_COL_NAME]

    def __init__(self, input_dataframe):
        validate_presence_of_columns(input_dataframe, self.EXPECTED_COLS)
        self.df1 = input_dataframe

    def get_zero_vol(self):
        """Method which returns dataframe containing key columns with only
           rows with zero volume.
        """
        return self.df1.filter(col(self.VOL_COL_NAME) == 0).select(self.KEY_COL1_NAME, self.KEY_COL2_NAME)

    def get_non_zero_vol(self):
        """Method which returns dataframe containing key columns with only
           rows with non-zero volume.
        """
        return self.df1.filter(col(self.VOL_COL_NAME) != 0).select(self.KEY_COL1_NAME, self.KEY_COL2_NAME)
