import datetime
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)
# print(p1)





# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name}({self.age})"

# p1 = Person("John", 36)

# print(p1)




# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person("John", 36)
# p1.myfunc()




# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age

#   def myfunc(abc):
#     print("Hello my name is " + abc.name)

# p1 = Person("John", 36)
# p1.myfunc()







# class Person:

#     def __init__(self, first_name, last_name, age, address, hobby="Tidak Ada Hobby"):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.address = address
#         self.hobby = hobby

#     def my_full_name(self):
#         return self.first_name + " " + self.last_name

#     def my_hobby(self):
#         print("My hobby is " + self.hobby)


# person_1 = Person('John',
#                   'Doe',
#                   36,
#                   'Bandung')

# person_1.my_hobby()


# class Student(Person):

#     def __init__(self, nisn, first_name, last_name, age, address, hobby):
#         super().__init__(first_name, last_name, age, address, hobby)
#         self.nisn = nisn

#     def my_hobby(self):
#         return 'Hobi saya adalah ' + self.hobby

#     def data_diri_dict(self):
#         return {
#             'nama': self.my_full_name(),
#             'umur': self.age,
#             'hobby': self.my_hobby()
#         }


# student_1 = Student('1234', 'Chandra', 'Adipraja', 34, 'KAWALI', 'Code')

# student_1.my_hobby()

# print(student_1.data_diri_dict())


# class Mathematic:
#     def __init__(self):
#        self.value = 0

#     def increment(self):
#        self.value += 2
    
#     def decrement(self):
#        self.value -= 2

#     def add(self, a, b):
#         return a + b
    
#     def substraction(self, a, b):
#         return a - b
    
#     def multiply(self, a, b):
#         return a * b
    
# math1 = Mathematic()
# math2 = Mathematic()

# math1.increment()
# math1.increment()
# math1.decrement()

# print(math2.value)







class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        self.pintu = 'tertutup'
        self.mesin = 'mati'
    
    def bukaPintu(self):
        if self.pintu == 'tertutup':
            print('Pintu berhasil di buka')
            self.pintu = 'terbuka'
        else:
            print('Pintu telah terbuka')

    def tutupPintu(self):
        if self.pintu == 'terbuka':
            print('Pintu berhasil ditutup')
            self.pintu = 'tertutup'
        else:
            print('Pintu telah tertutup')

    def nyalakanMobil(self):
        if self.mesin == 'mati':
            print('Mobil berhasil di nyalakan')
            self.mesin = 'hidup'
        else:
            print('Mobil sudah di nyalakan')

    def matikanMobil(self):
        if self.mesin == 'hidup':
            print('Mobil berhasil di matikan')
            self.mesin = 'mati'
        else:
            print('Mobil sudah di matikan')


car1 = Car('Civic', 2023)
car1.bukaPintu()
car1.bukaPintu()
car1.tutupPintu()
car1.bukaPintu()
car1.tutupPintu()
print('')
car1.nyalakanMobil()
car1.nyalakanMobil()
car1.matikanMobil()
car1.matikanMobil()
car1.nyalakanMobil()
car1.matikanMobil()