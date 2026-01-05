import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from validator import valid_filename
from validator import valid_filename

def test_filename():
    assert valid_filename("MED_DATA_20240101120101.csv")
    assert not valid_filename("wrong.csv")