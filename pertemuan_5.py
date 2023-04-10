# import datetime

# x = datetime.datetime.now()
# print(type(x))

# x = datetime.datetime.now()
# print(x.year)
# print(x.strftime("%A"))

# x = datetime.datetime(2020, 5, 17)
# print(x)

# x = datetime.datetime(2018, 6, 1)
# print(x.strftime("%B"))

# x = datetime.datetime.now()
# print(x.strftime("%d/%m/%Y"))

# arr_1 = [5, 78, 2, 0]

# assert(min(arr_1)) == 0
# assert(max(arr_1)) == 78

# assert(pow(5, 5)) == 3125


# try:
#   print(x)
# except:
#   print("An exception occurred")

# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")

# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")

# try:
#   f = open("demofile.txt")
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")



# import json

# # Terima / Import
# # some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'
# # parse x:
# y = json.loads(x)
# # the result is a Python dictionary:
# print(y["age"])

# # Kirim / Export
# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
# # convert into JSON:
# y = json.dumps(x)
# # the result is a JSON string:
# print(y)

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
# json.dumps(x, indent=4)
# json.dumps(x, indent=4, separators=(". ", " = "))
# json.dumps(x, indent=4, sort_keys=True)
# print(x)
# print(json.dumps(x))

# y = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
# print(type(y))
# print("DICT: ", y)
# print(y)

# y = json.dumps(y)
# print(type(y))
# print("JSON: ", y)
# print(y)

# y = json.loads(y)
# print(type(y))
# print("DICT: ", y)
# print(y)
# print(y['age'])


# f = open("demofile.txt")
# # f = open("demofile.txt", "rt")
# f = open("demofile.txt", "r")
# # print(f.readline())
# print(f.read())

# f = open("demofile2.txt", "w")
# f.write("Now the file has more content!")
# f.close()
# #open and read the file after the appending:
# f = open("demofile2.txt", "r")
# print(f.read())


# f = open("demofile3.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()

# #open and read the file after the overwriting:
# f = open("demofile3.txt", "r")
# print(f.read())

# import os
# # os.remove("demofile2.txt")
# if os.path.exists("demofile2.txt"):
#   os.remove("demofile2.txt")
# else:
#   print("The file does not exist")

f = open('json_read.txt')
json_string = f.read()
print(type(json_string))
print(json_string)

import json
json_string = json.loads(json_string)
print(type(json_string))
print(json_string)
print(json_string['name'])

users = [
    {
        'email' : 'nandan@gmail.com',
        'password' : '1234'
    },
    {
        'email' : 'nandan@gmail.com',
        'password' : '1234'
    },
]

users.append(
    {
        'email':'nandanramdani608@gmail.com',
        'password':'123321'
    }
)
# json_string = json.dumps(users)
# f = open('json_write.txt', 'w')
# f.write(json_string)
# f.close()

def dump_and_write(filename, data):
    json_string = json.dumps(data)
    f = open(filename, 'w')
    f.write(json_string)
    f.close()


dump_and_write('json_write.txt', users)

