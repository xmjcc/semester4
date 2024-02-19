import requests
URL='https://www.w3schools.com/html/default.asp'
response=requests.get(URL)
# print(response.status_code)
# print(response.ok)
# print(dir(response))
# print(response.encoding)
# print(response.text)
print(response.headers)
print(response.json())