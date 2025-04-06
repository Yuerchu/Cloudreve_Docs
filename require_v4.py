# pip install requests
import requests

# 服务器地址
url = 'http://127.0.0.1:5212'

# JWT Bearer Token
token = ''


# 使用表单数据
r = requests.get(
    url,
    headers={"Authorization": "Bearer " + token}
)

# 打印响应内容
print(r.text)