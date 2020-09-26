import  requests
url = 'https://github.com/'
res =requests.get(url,cookies=None)
# print(res)
# print("响应头：",res.headers)
print("响应状态码:",res.status_code)
# print("响应报文:",res.text)


url='http://119.23.241.154:8080/futureloan/mvc/api/member/login'
data={"mobile_phone":"17521187997","pwd":"123"}
res1 =requests.post(url,data)
# print(res)
# print("响应头：",res.headers)
print("响应状态码:",res1.status_code)
# print("响应报文:",res.text)

