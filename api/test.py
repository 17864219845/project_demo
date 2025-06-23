

import builtins
import uuid

import requests

res = dir(builtins)
# print(res)

# result = requests.get("http://10.43.160.198:5000/internal/api/home")
# if result.status_code != 200:
#     print('no', result.json())

a = uuid.uuid4().hex

print(a)