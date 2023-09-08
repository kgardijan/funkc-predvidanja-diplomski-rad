import requests
import json

# Define the endpoint URL
endpoint_url = "http://20.8.189.172:80/api/v1/service/nba-stats-denorm-ep/score"

# Prepare input data as a dictionary
input_data = {
    "Age": 0.25648,
        "G": 0.658965,
        "GS": 0.265060241,
        "MP": 0.3625,
        "FG": 0.18756,
        "FGA": 0.2,
        "FG%": 0.54,
        "3P": 0.183673,
        "3PA": 0.929825,
        "3P%": 0.399,
        "2P": 0.733333,
        "2PA": 0.348314607,
        "2P%": 0.579,
        "eFG%": 0.556,
        "FT": 0.14,
        "FTA": 0.227652,
        "FT%": 0.836,
        "ORB": 0.352961,
        "DRB": 0.458333,
        "TRB": 0.48,
        "AST": 0.130841,
        "STL":0.2,
        "BLK": 0.2333,
        "TOV": 0.0235,
        "PF": 0.32,
        "Pos_C": 0,
        "Pos_PF": 0,
        "Pos_PF-C": 0,
        "Pos_PF-SF": 0,
        "Pos_PG": 0,
        "Pos_PG-SG": 0,
        "Pos_SF": 1,
        "Pos_SF-PF": 0,
        "Pos_SF-SG": 0,
        "Pos_SG": 0,
        "Pos_SG-PG": 0,
        "Tm_ATL": 0,
         "Tm_BOS": 1,
        "Tm_BRK": 0,
         "Tm_CHI": 0,
        "Tm_CHO": 0,
         "Tm_CLE": 0,
        "Tm_DAL": 0,
         "Tm_DEN": 0,
        "Tm_DET": 0,
         "Tm_GSW": 0,
        "Tm_HOU": 0,
         "Tm_IND": 0,
        "Tm_LAC": 0,
         "Tm_LAL": 0,
        "Tm_MEM": 0,
         "Tm_MIA": 0,
        "Tm_MIL": 0,
         "Tm_MIN": 0,
        "Tm_NOP": 0,
         "Tm_NYK": 0,
        "Tm_OKC": 0,
         "Tm_ORL": 0,
        "Tm_PHI": 0,
         "Tm_PHO": 0,
        "Tm_POR": 0,
         "Tm_SAC": 0,
        "Tm_SAS": 0,
         "Tm_TOR": 0,
        "Tm_TOT": 0,
         "Tm_UTA": 0,
        "Tm_WAS": 0
    # Add more input columns and values as needed
}

# Convert input data to JSON format
input_json = json.dumps({"data": [input_data]})

# Set headers for the POST request
headers = {
    "Content-Type": "application/json",
    "Authorization": "jMJaoWn3gmV2BgIe16tM7bSouGo5mbjk",  # If authentication is required
}

# Send the POST request
response = requests.post(endpoint_url, data=input_json, headers=headers)

# Check the response status code and content
if response.status_code == 200:
    result = response.json()
    print("Prediction Result:", result)
else:
    print("Request failed with status code:", response.status_code)
    print("Response content:", response.text)
