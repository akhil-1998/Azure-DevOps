import requests
import json

url = "http://449cf201-0789-41c4-9b8c-570035a3c2de.eastus2.azurecontainer.io/score"

test_sample = json.dumps({'data': [
    [1,2,3,4,54,6,7,8,88,10], 
    [10,9,8,37,36,45,4,33,2,1]
]})
test_sample = str(test_sample)

payload=test_sample
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
#print(response.content)
print(response.text)