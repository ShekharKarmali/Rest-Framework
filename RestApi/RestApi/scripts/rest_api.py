import requests
import json
import os

image_path =os.path.join(os.getcwd(),"picu.jpg")

ENDPOINT ="http://127.0.0.1:8000/status/api/"
AUTH_ENDPOINT ="http://127.0.0.1:8000/api/auth/"
# AUTH_ENDPOINT ="http://127.0.0.1:8000/api/auth/register/"
# REFRESH_ENDPOINT =AUTH_ENDPOINT + "refresh/"

# Here we are login
headers={
    'content-type':"application/json",
    # "Authorization": "JWT " + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFwaSIsImV4cCI6MTU5OTkxMDE5NCwiZW1haWwiOiJrYXJtYWxpc2hla2hAdGVhbS5jb20iLCJvcmlnX2lhdCI6MTU5OTkwOTg5NH0.nkdUEBvL8zqP-M-a0S2rxs4Fe2DGrmxGdtgXCrJ-Nu8',
}

data={
    'username':'api',
    'password':'123',
}

r=requests.post(AUTH_ENDPOINT,data=json.dumps(data),headers=headers)
token=r.json() ['token']
# print(token)

# here we are doing crud
BASE_ENDPOINT="http://127.0.0.1:8000/status/api/"
ENDPOINT = BASE_ENDPOINT + "24/"

headers2={
    # 'content-type':"application/json",
    "Authorization": "JWT " + token
}

data2={
    'content':"This new content is really cool"
}

if image_path is not None:
    with open(image_path, 'rb') as image:
        file_data = {
            'image': image   ###Not Working
        }
        # r=requests.post(BASE_ENDPOINT,data=data2,headers=headers2,files=file_data)
        r=requests.get(ENDPOINT,headers=headers2)
        print(r.text)
# if image_path is not None:
#     with open(image_path, 'rb') as image:
#         file_data = {
#             'image': image
#         }
#         r=requests.put(ENDPOINT,data=data2,headers=headers2,files=file_data)
#         print(r.text)



'''
This was for authenication operation
'''
# headers={
#     'content-type':"application/json",
#     # "Authorization": "JWT " + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxOSwidXNlcm5hbWUiOiJydW1teTEyMSIsImV4cCI6MTU5OTkwNDIxOSwiZW1haWwiOiJydW1teTEyMUB0ZWFtLmNvbSIsIm9yaWdfaWF0IjoxNTk5OTAzOTE5fQ.w4LkuCHzuT7Ny9Uf_eli4Uj2yPed6L6mUe2IpRKrCh8',
# }

# data={
#     'username':'rummy121',
#     'email':'rummy121@team.com',
#     'password':'123',
#     'password2':'123'
# }

# # This is the fundamental on how to do that
# r=requests.post(AUTH_ENDPOINT,data=json.dumps(data),headers=headers)
# # print(r.json()) or
# token=r.json() #['token']
# print(token)

# refresh_data = {
#     'token': token
# }

# new_response = requests.post(REFRESH_ENDPOINT, data=json.dumps(refresh_data), headers=headers)
# new_token = new_response.json() #['token']

# print(new_token)


'''
This is for post and updating of data with jwt authorization
'''

# headers = {
#     #"Content-Type": "application/json",
#     "Authorization": "JWT " + token,
# }

# data = {
#     "content": "This is for check of auth"
# }
# json_data = json.dumps(data)
# posted_response = requests.put(ENDPOINT + str(23) + "/", data=data, headers=headers)
# # posted_response = requests.post(ENDPOINT, data=data, headers=headers) #this post part is not working?
# print(posted_response.text)


'''
This is for post and updating of data with image along jwt authorization
'''
# headers = {
#     #"Content-Type": "application/json",
#     "Authorization": "JWT " + token,
# }

# with open(image_path, 'rb') as image:
#     file_data = {
#         'image': image
#     }
#     data = {
#         "content": "Updated description"
#     }
#     json_data = json.dumps(data)
#     posted_response = requests.put(ENDPOINT + str(24) + "/", data=data, headers=headers, files=file_data)
#     print(posted_response.text)









'''
This is for checking of permission and authentication

# get_endpoint=ENDPOINT + str(24)
# post_data=json.dumps({"content":"check this testing"})

# r=requests.get(get_endpoint)
# print(r.text)

# r2=requests.get(ENDPOINT)
# print(r2.status_code)

# post_headers={
#     'content-type':'application/json'
# }

# post_response=requests.post(ENDPOINT,data=post_data,headers=post_headers)
# print(post_response.text)
'''



'''
This is for posting and updating of data with image
'''
# def do_img(method='get',data={}, is_json=True,img_path=None):
#     headers={}
#     if is_json:
#         headers['content-type']='application/json'
#         data=json.dumps(data)
#     if img_path is not None:
#         with open(image_path,'rb') as image:
#             file_data = {
#                 'image':image
#             }
#             r=requests.request(method,ENDPOINT,data=data,files=file_data,headers=headers)
#     else:
#         r=requests.request(method, ENDPOINT , data=data,headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r

# do_img(
#     method='put',
#     data={'user':1,'id':1,'name':"Shekhar",'content':"Some image content"},
#     is_json=False,
#     img_path=image_path
#     )   



# def do(method='get',data={}, is_json=True):
#     headers={}
#     if is_json:
#         headers['content-type']='application/json'
#         data=json.dumps(data)
#     r=requests.request(method, ENDPOINT , data=data,headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r

# do(data={'id':5})

# do(method='post',data={'name':"siri",'content':"maintain the continuty",'user':1})
# do(method='put',data={'id':17,'content':"maintain the continuty",'user':1})
# do(method='patch',data={'id':17,'content':"maintain the continuty with focus",'user':1})
# do(method='delete',data={'id':14})