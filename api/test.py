

import builtins
import uuid

import requests

from configs import config

# res111 = dir(builtins)
# print(res)

# result = requests.get("http://10.43.160.198:5000/internal/api/home")
# if result.status_code != 200:
#     print('no', result.json())


import flask_migrate

flask_migrate.upgrade()


