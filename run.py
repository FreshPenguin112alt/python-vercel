from requests import get
from os import environ as env
get(env["url"])
f = open("api/index.py", "r")
exec(f.read()+"\napp.run(host='0.0.0.0', port=8080)")
