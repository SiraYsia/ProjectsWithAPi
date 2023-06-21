import requests

url = 'http://api.open-notify.org/astros.json'
response = requests.get(url)

data = response.json()
people = data['people']
print(response.status_code)

for i in range(5):
  print (people[i]['name'])




