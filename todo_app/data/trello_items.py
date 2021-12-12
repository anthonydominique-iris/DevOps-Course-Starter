from flask import session
import requests
import json
from werkzeug.datastructures import Headers

url="https://api.trello.com/1/actions/1"

def get_trelloitems():
    response = requests.request(
        "GET",
        url,
        headers=Headers
    )

#  NOT BEING USED    
