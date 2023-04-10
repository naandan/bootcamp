# import time
# import math
# def calculate_time(func):
#     def inner(*args, **kwargs):
#         begin = time.time()
#         func(*args, **kwargs)

#         end = time.time()
#         print("Total time taken in : ", func.__name__, end * begin)
#     return inner

# @calculate_time
# def factorial(num):
#     time.sleep(2)
#     print(math.factorial(num))

# factorial(10)

import requests
from pprint import pprint

r = requests.get('https://jsonplaceholder.typicode.com/posts')
data = r.json()
# pprint(data)

post = {
    'body':'Lorem ipsum',
    'title':'Title',
    'userId':5
}
req = requests.post('https://jsonplaceholder.typicode.com/posts', json=post)
print(req.json())

update_post = post
update_post['id'] = 5

req = requests.put('https://jsonplaceholder.typicode.com/posts/5', json=update_post)
print(req.json())