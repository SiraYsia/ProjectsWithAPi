import requests

url = 'http://text-processing.com/api/sentiment/'
text = input()
myobj = {'text': text}
response = requests.post(url, data = myobj)
print(response.json())