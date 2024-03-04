# ds_protocol.py

# Starter code for assignment 3 in ICS 32 Programming
# with Software Libraries in Python

# Replace the following placeholders with your information.

# Nicole Utama
# nutama@uci.edu
# 20267081

"""
This module has the extract_json file that is used
in ds_client.py
"""

import json
from collections import namedtuple

# Namedtuple to hold the values retrieved from json messages.
DataTuple = namedtuple('DataTuple', ['type', 'message', 'token'])


def extract_json(json_msg: str) -> DataTuple:
    '''
    Call the json.loads function on a json string 
    and convert it to a DataTuple object
    '''
    try:
        json_obj = json.loads(json_msg)
        msg_type = json_obj['response']['type']
        message = json_obj['response']['message']
        if msg_type == "ok":
            msg_token = json_obj['response']['token']
        else:
            msg_token = ""
    except json.JSONDecodeError:
        print("Json cannot be decoded.")
    return DataTuple(msg_type, message, msg_token)
