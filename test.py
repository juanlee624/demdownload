# -*- coding: utf-8 -*-

import json

str="{"params":{"id":222,"offset":0},{"nodename":"topic"}}

r=json.loads(str)

print(r['params']['id'])