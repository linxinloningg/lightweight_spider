import requests
import re

content = requests.get('https://gz.58.com/pinpaigongyu/pn/0/').content.decode()
print(content)
print(content.count('class="house"'))
