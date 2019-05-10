import requests
import json

url = 'http://colormind.io/api/'
data = '''{"input":[[44,43,44],[90,83,82],"N","N","N"],
   "model": "default"
 }'''
bin_data = data.encode('ascii')
response = requests.post(url, data=bin_data)
print("Response:",response)
print("Content:",response.content)
print("JSON Content:", json.loads(response.content.decode('ascii')))

# For successful API call, response code will be 200 (OK)
if(response.ok):
    # Loading the response data into a dict variable
    # json.loads takes in only binary or string variables so using content to fetch binary content
    # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
    jData = json.loads(response.content.decode('ascii'))
    print(jData)
else:
  # If response code is not ok (200), print the resulting http error code with description
    myResponse.raise_for_status()
