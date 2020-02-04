"""Module to test module1 in template_pkg package
"""
import os
import sys

from quinn.dataframe_validator import DataFrameMissingColumnError
from sparktestingbase.sqltestcase import SQLTestCase

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from example_pkg.module1 import Logic1  # noqa pylint: disable=E0401,C0413


class Logic1Test(SQLTestCase):
    """Class to test Logic1 class
    """

    def valid_input_dataframe(self):
        """Returns a valid input for Logic1
        """
        return self.sqlCtx.createDataFrame([(1, 1, 100), (1, 2, 200), (1, 3, 0)], ["key_a", "key_b", "vol_a"])

    def test1_invalid_input_dataframe(self):
        """Test exception when Logic1 object initialize with invalid dataframe
        """
        input_dataframe = self.sqlCtx.createDataFrame([(1, 100)], ["key_a", "vol_a"])
        with self.assertRaises(DataFrameMissingColumnError):
            Logic1(input_dataframe)

    def test2_get_zero_vol(self):
        """Test get_zero_vol correctly returns dataframe containing rows with only zero volume
        """
        logic1 = Logic1(self.valid_input_dataframe())
        actual = logic1.get_zero_vol()
        expected = self.sqlCtx.createDataFrame([(1, 3)], ["key_a", "key_b"])
        self.assertDataFrameEqual(expected, actual)

    def test3_get_non_zero_vol(self):
        """Test get_non_zero_vol correctly returns dataframe containing rows with only non zero volume
        """
        logic1 = Logic1(self.valid_input_dataframe())
        actual = logic1.get_non_zero_vol()
        expected = self.sqlCtx.createDataFrame([(1, 1), (1, 2)], ["key_a", "key_b"])
        self.assertDataFrameEqual(expected, actual)
