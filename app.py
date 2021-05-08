from chalice import Chalice,  Rate
import os
import requests
from datetime import datetime,  timezone

from pymongo import MongoClient

# Set up normal Mongo Atlas connection + db + collection
# mongopass = os.getenv('MONGOPASS')
uri = "mongodb+srv://cluster0.mmhgn.mongodb.net/test"
client = MongoClient(uri, username='mongouser', password="mayfirst", connectTimeoutMS=200, retryWrites=True)
db = client.test

app = Chalice(app_name='project2')

@app.schedule(Rate(1, unit=Rate.MINUTES))
def access_api(event):
    dt = datetime.strptime("2021-05-08 03:05:01", "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
    if datetime.now(tz=timezone.utc) > dt:
        return {"fail":500}
    resp_json = requests.get("https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi").json()
    db.testing.insert_one(resp_json)
    return {"SUCCESS":200}


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
