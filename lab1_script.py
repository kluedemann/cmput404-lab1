import requests

# print(requests.__version__)

url = "https://raw.githubusercontent.com/kluedemann/cmput404-lab1/main/lab1_script.py"
request = requests.get(url)
print(request.text)
