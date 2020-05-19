
import requests
# r = requests.get("http://127.0.0.1:8000/api/profile/")
# print(r.json())

def addPro(m,n):
    mydata ={
        "mobile": m,
        "name": n
    }
    r =requests.post("http://127.0.0.1:8000/api/profile/",data=mydata)
    print(r.content)
# postman
# m1= input("Mobile Enter:")
# n1= input("Mobile Name:")
#
# addPro(m1,n1)


r =requests.get("http://127.0.0.1:8000/api/product/")
# print(r.json())

data =r.json()

print(data)