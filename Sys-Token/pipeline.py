import requests
import base64
import json
import os

token = os.environ.get("SYSTEM_ACCESSTOKEN")

authorization = str(base64.b64encode(bytes(':'+token, 'ascii')), 'ascii')

headers = {
    'Accept': 'application/json',
    'Authorization': 'Basic '+authorization
}

Org=""
Project=""

#API CALLS TO AZURE DEVOPS Pipelines
response = requests.get(
    url=f"https://dev.azure.com/{Org}/{Project}/_apis/pipelines?api-version=6.0-preview.1", headers=headers)
responsedata=json.dumps(response.json(), indent=4, separators=(',', ': '))
print(responsedata)