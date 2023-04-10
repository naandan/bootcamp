# print("Hello World")


# Percabangan
# a = 6
# b = 5
# if a == 5:
#     print("Sama")
# else:
#     print ("Tidak Sama")


# Konversi
# print(str(1))
# print(int("3"))
# print(float(3))


# Cek Tipe Data
# x = 5
# y = "john"
# print(type(x))
# print(type(y))


# Variabel Horizontal 
# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)


# Array to Variabel
# fruits = ["Apple", "Banana", "Cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)


# String Concatenation
# x = "Python"
# y = "is"
# z = "Awesome"
# print(x, y, z)
# print(x + y + z) Tanpa Spasi


# Penjumlahan Aritmatika 
# x = 5
# y = 10
# print(x + y)


# Tipe Data Concatenation
# x = 5
# y = "10"
# print(x, y)


# Function
# x = "awesome"
# def myfunc():
#     print("Ptyhon is "+  x)
# myfunc()


# Functional Scope
# x = "awesome"
# def myfunc():
#     x = "fantastic"
#     print("Ptyhon is "+  x)
# myfunc()
# print("Ptyhon is "+  x)


# Multiple line string
# a = """Python can be easy to pick up whether you're a first time programmer or you're
# experienced with other languages. The following pages are a useful first step to
#  get on your way writing programs with Python!"""


# Cek Value
# for x in "banana":
#     print(x)


# Array Length
# a = "Hello, World!"
# print(len(a))


# Cek Value
# txt = "Membentuk siswa-siswa yang unggul,berkarater serta memiliki kesiapan untuk bekerja maupun wirausaha"
# print("maupun" not in txt)
# if "maupun" in txt:
#     print("Yes")
# else:
#     print("No")


# Uppercase
# a = "Hello, World!"
# print(a.upper())


# Delete Whitespace
# a = "     Hello, World!   "
# print(a.strip())


# Replace Value
# a = "Hello, World! "
# print(a.replace("H", "J"))


# Variabel Separate
# a = "Hello! World"
# print(a.split("!"))


# ============= Problem Solving =============

# def sum_int_or_str(a, b):
#     return int(a) + int(b)

# assert(sum_int_or_str(1, '2')) == 3
# assert(sum_int_or_str(2, 2)) == 4




# def get_second_character(a):
#     if len(a) > 1:
#         return a[1]
#     else:
#         return 0

# assert(get_second_character("ab")) == "b"
# assert(get_second_character("a")) == 0




# cars = [
#     {
#         'brand': 'Toyota',
#     },
#     {
#         'brand': 'Honda',
#         'products': [
#             'Civic'
#         ]
#     }
# ]

# assert(car[0]['brand']) == 'Toyota'
# assert(cars[1]['products'][0]) == 'Civic'





# raw_cars = 'toyota,honda,indiacar'

# assert(raw_cars.split(',')) == ['toyota', 'honda', 'indiacar']

# def function_a(a):
#     return a.upper().split(',')

# assert(function_a(raw_cars)) == ['TOYOTA', 'HONDA', 'INDIACAR']

# # assert(raw_cars.upper().split(',')) == ['TOYOTA', 'HONDA', 'INDIACAR']





# raw_cars = 'toyota,honda,indiacar,indiacar,indiacar'

# raw_cars = raw_cars.split(',')

# raw_cars = set(raw_cars)

# raw_cars = list(raw_cars)

# assert(raw_cars) == ['toyota', 'honda', 'indiacar']





# raw_cars = 'toyota,honda,indiacar,indiacar,indiacar'

# raw_cars = raw_cars.split(',')

# raw_cars = set(raw_cars)

# raw_cars = len(raw_cars)

# assert(raw_cars) == 3