import os
import json
import pandas as pd
from pandas import json_normalize

from common import constants as const

def get_schema_json():
    """
    This function reads the schema json from res folder
    :return: dict of the schema json
    """
    with open(os.path.join(os.getcwd(), const.c_path_schema_json)) as f:
        data = json.load(f)
    return data
