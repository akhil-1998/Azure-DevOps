#Import Required Libraries
import requests
import base64
import pandas as pd
import sys

#Path for publishing as an artifact
export_path=str(sys.argv[1])
#PAT token for connecting to ADO
pat=str(sys.argv[2])

project_name=""
organization=""

#Authorization
authorization = str(base64.b64encode(bytes(':'+pat, 'ascii')), 'ascii')

#Header
headers = {
    'Accept': 'application/json',
    'Authorization': 'Basic '+authorization
}

#Create a dataframe to store the list of Repos
column_names = ["Repository"]
df = pd.DataFrame(columns = column_names)
Repositorylist=[]

#API CALLS TO AZURE DEVOPS REPOS
response = requests.get(
    url=f"https://dev.azure.com/{organization}/{project_name}/_apis/git/repositories?api-version=6.1-preview.1", headers=headers)
json_data = response.json()

for value in json_data['value']:
    Repository=value['name']
    print(value['name'])
    Repositorylist.append(Repository)

df["Repository"]=Repositorylist

# Generating a CSV from the dataframe and publishing it to the source path
df.to_csv(export_path)



