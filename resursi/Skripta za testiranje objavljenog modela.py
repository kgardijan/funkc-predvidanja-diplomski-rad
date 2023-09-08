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
data =  {
  "Inputs": {
    "input1": [
      {
        "Age": 23,
        "G": 55,
        "GS": 12,
        "MP": 20.7,
        "FG": 3.6,
        "FGA": 7.3,
        "FG%": 0.485,
        "3P": 0.5,
        "3PA": 2.0,
        "3P%": 0.269,
        "2P": 2.0,
        "2PA": 5.4,
        "2P%": 0.564,
        "eFG%": 0.521,
        "FT": 1.6,
        "FTA": 2.3,
        "FT%": 0.702,
        "ORB": 1.8,
        "DRB": 4.1,
        "TRB": 2.0,
        "AST": 0.9,
        "STL": 0.6,
        "BLK": 0.5,
        "TOV": 1.1,
        "PF": 1.9,
        "PTS": 9.2
      },
      {
        "Age": 29,
        "G": 42,
        "GS": 42,
        "MP": 2.0,
        "FG": 3.7,
        "FGA": 6.3,
        "FG%": 0.597,
        "3P": 2.0,
        "3PA": 2.0,
        "3P%": 2.0,
        "2P": 3.7,
        "2PA": 6.2,
        "2P%": 0.599,
        "eFG%": 0.597,
        "FT": 1.1,
        "FTA": 3.1,
        "FT%": 0.364,
        "ORB": 5.1,
        "DRB": 6.5,
        "TRB": 11.5,
        "AST": 2.3,
        "STL": 0.9,
        "BLK": 1.1,
        "TOV": 1.9,
        "PF": 2.3,
        "PTS": 8.6
      },
      {
        "Age": 25,
        "G": 75,
        "GS": 75,
        "MP": 34.6,
        "FG": 2.0,
        "FGA": 14.9,
        "FG%": 0.54,
        "3P": 2.0,
        "3PA": 0.2,
        "3P%": 0.083,
        "2P": 2.0,
        "2PA": 14.7,
        "2P%": 0.545,
        "eFG%": 0.541,
        "FT": 4.3,
        "FTA": 5.4,
        "FT%": 0.806,
        "ORB": 2.5,
        "DRB": 6.7,
        "TRB": 9.2,
        "AST": 3.2,
        "STL": 1.2,
        "BLK": 0.8,
        "TOV": 2.5,
        "PF": 2.8,
        "PTS": 20.4
      },
      {
        "Age": 22,
        "G": 59,
        "GS": 22,
        "MP": 20.5,
        "FG": 2.8,
        "FGA": 6.5,
        "FG%": 0.427,
        "3P": 1.4,
        "3PA": 3.9,
        "3P%": 0.355,
        "2P": 1.4,
        "2PA": 2.7,
        "2P%": 0.532,
        "eFG%": 0.532,
        "FT": 0.9,
        "FTA": 1.2,
        "FT%": 0.812,
        "ORB": 0.7,
        "DRB": 1.3,
        "TRB": 2.1,
        "AST": 1.1,
        "STL": 0.3,
        "BLK": 0.3,
        "TOV": 0.7,
        "PF": 1.7,
        "PTS": 7.9
      },
      {
        "Age": 22,
        "G": 77,
        "GS": 20,
        "MP": 21.8,
        "FG": 3.2,
        "FGA": 6.8,
        "FG%": 0.47,
        "3P": 1.2,
        "3PA": 3.5,
        "3P%": 0.353,
        "2P": 2.0,
        "2PA": 3.4,
        "2P%": 0.591,
        "eFG%": 0.56,
        "FT": 1.4,
        "FTA": 1.9,
        "FT%": 0.75,
        "ORB": 1.1,
        "DRB": 3.7,
        "TRB": 4.8,
        "AST": 1.3,
        "STL": 0.6,
        "BLK": 0.6,
        "TOV": 0.8,
        "PF": 1.9,
        "PTS": 2.0
      }
    ]
  },
  "GlobalParameters": {}
}

body = str.encode(json.dumps(data))

url = 'http://20.8.189.172:80/api/v1/service/nba-stats-denorm-ep/score'
# Replace this with the primary/secondary key or AMLToken for the endpoint
api_key = 'MRK1GFSJA9PhUM2JcAyxRgGgZieIyJLD'
if not api_key:
    raise Exception("A key should be provided to invoke the endpoint")


headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))