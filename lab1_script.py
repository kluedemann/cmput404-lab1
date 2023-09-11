import requests

# print(requests.__version__)

url = "http://www.google.com"
request = requests.get(url)
print(request)
