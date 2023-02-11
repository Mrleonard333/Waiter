from os import system
import requests
import json

system("clear")
# Data = {"User_Data":{"username":"User", "password":"Pass"}, "Food":"Spaghetti", "Price":25.5}
# print(requests.put("http://localhost:8000/menu/change/", json=Data).content)

# Data = {"User_Data":{"username":"User", "password":"Pass"}, "Id":3, "Food":"Pizza", "Price":50}
# print(requests.post("http://localhost:8000/menu/change/", json=Data).content)

# Data = {"User_Data":{"username":"User", "password":"Pass"}, "Food":"Pizza"}
# print(requests.delete("http://localhost:8000/menu/change/", json=Data).content)

# print(requests.post("http://localhost:8000/order/", json={"Client":"Mr.leonard", "Order":"Spaghetti"}).content)
# print(requests.post("http://localhost:8000/check/", json={"Client":"Mr.leonard"}).content)