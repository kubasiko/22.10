import requests 
response=requests.get('https://reqres.in')
print(response.status_code)