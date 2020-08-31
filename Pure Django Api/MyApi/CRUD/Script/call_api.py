import json
import requests

BASE_URL ="http://127.0.0.1:8000/"
ENDPOINT ="MyApi/Api/"


def Get(id=None): ##This is retrieve function
    data=json.dumps({})
    if id is not None:
        data=json.dumps({"id":id})   
    r=requests.get(BASE_URL + ENDPOINT,data=data)
    print(r.status_code)
    if r.status_code!=200:
        print('probably not a good thing!')
    # print(type(json.dumps(data)))  #It is converting in string 
    # for obj in data:
    #     if obj['id'] == 1:  #user interaction
    #         r2=requests.get(BASE_URL + ENDPOINT + str(obj['id']))
    #         print(r2.json())
    #         print(obj)
    data=r.json()
    return data

print(Get())
# Get()

def Post():
    new_data={
        "user":1,
        "name":"Manish",
        "content":"Achha beta"
    }
    r=requests.post(BASE_URL + ENDPOINT ,data=new_data)
    # print(r.headers)
    print(r.status_code)
    if r.status_code==requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text

# print(Post())   


def update():
    new_data={
        "id":7,
        "content":"lets check one point"
    }
    r=requests.put(BASE_URL + ENDPOINT ,data=json.dumps(new_data))
    # print(r.headers)
    print(r.status_code)
    if r.status_code==requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text

# print(update())

def delete():
    new_data={
        "id":7
    }
    r=requests.delete(BASE_URL + ENDPOINT,data=json.dumps(new_data))
    # print(r.headers)
    print(r.status_code)
    if r.status_code==requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text

# print(delete())