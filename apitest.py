import requests, json

base_url = "http://colormind.io/api/"

data = {
    'input': [[44,43,44],[90,83,82],"N","N","N"],
    'model': 'default'
}

r = requests.get(base_url, params=data)
newdata = r.json()
pprint(newdata)
    

    
					
