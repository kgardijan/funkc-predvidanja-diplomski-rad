from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

@app.route('/prediction', methods=['POST'])
def hello():
    print(request.data)
    data = request.get_json()
    print(invoke_api(data, "MRK1GFSJA9PhUM2JcAyxRgGgZieIyJLD"))
    return invoke_api(data, "MRK1GFSJA9PhUM2JcAyxRgGgZieIyJLD")

import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
def invoke_api(data, api_key):
    # Encode the data to JSON
    body = str.encode(json.dumps(data))
    
    # Specify the API URL
    url = 'http://20.8.189.172:80/api/v1/service/nba-stats-denorm-ep/score'
    
    # Check if an API key is provided
    if not api_key:
        raise Exception("A key should be provided to invoke the endpoint")
    
    # Set the headers with API key
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
    
    # Create the HTTP request
    req = urllib.request.Request(url, body, headers)
    
    try:
        # Send the request and get the response
        response = urllib.request.urlopen(req)
        
        # Read and return the result
        result = response.read()
        return result.decode("utf8", 'ignore')
    
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))
        # Print the headers - they include the request ID and timestamp for debugging
        print(error.info())
        print(error.read().decode("utf8", 'ignore'))

if __name__ == "__main__":
    app.run(port=8000)