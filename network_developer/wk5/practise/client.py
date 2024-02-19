import requests
def abc():
    URL='http://127.0.0.1:5000'
    response=requests.get(URL)
    if response.status_code==200:
        print(response.text)
    else:
        print(response.status_code)

def all_students():
    URL='http://127.0.0.1:5000/allstudents'
    response=requests.get(URL)
    if response.status_code==200:
        print(response.text)
    else:
        print(response.status_code)
abc()
all_students()
# if __name__=='__main__':
#     abc()