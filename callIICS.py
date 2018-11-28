import botocore.vendored.requests as requests
import os
import json
import ssl

url='https://dm-us.informaticacloud.com/ma/api/v2/user/login'
myData = {"@type":"login","username":"username@troweprice.dev","password": ""}
vaultHeader = {"Content-Type": "application/json","Accept": "application/json"}
response = requests.post(url=url,headers =vaultHeader, data = json.dumps(myData))
print(str(response.text))
