
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])

# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")

# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)

# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])

# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1

# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

# thislist = ["apple", "banana", "mango"]

# thislist.pop(1)
# assert(thislist) == ["apple", "mango"]

# thislist.append('kiwi')
# assert(thislist) == ['apple', 'mango', 'kiwi']



# new_list = ['apple', 'apple', 'apple', 'apple',
#             'mango', 'kiwi', 'apple', 'apple', 
#             'apple', 'apple']

# assert(new_list[4:6]) == ['mango', 'kiwi']



# new_list = ['apple', 'apple', 'apple', 'apple',
#             'mango', 'kiwi', 'apple', 'apple',
#             'mango', 'kiwi', 'apple', 'apple',
#             'apple', 'apple']

# new = []
# for x in new_list:
#     if x != 'apple':
#         new.append(x)

# assert(new) == ['mango', 'kiwi', 'mango', 'kiwi']
# assert([x for x in new_list if x != 'apple']) == ['mango', 'kiwi', 'mango', 'kiwi']



# list1 = ['mango']
# list2 = ['apple']
# list1.extend(list2)
# list1 = list1 + list2
# list1 += list2

# list1 = [1, 4, 5, 6, 2, 4]
# list1.sort()
# print(list1)

# list1 = [1, 4, 5, 6, 2, 4]
# list1.sort(reverse=True)
# print(list1)

# list1 = [1, 4, 5, 6, 2, 4]
# list1.reverse()
# print(list1)

# list1 = [1, 4, 5, 6, 2, 4]
# assert([x for  x in list1 if x != 4]) == [1, 5, 6, 2]
# assert([x for  x in list1 if x == 4]) == [4, 4]

# list1 = [1, 4, 5, 6, 2, 4]
# list2 = list1.copy()
# list2.pop()

# print(list1, list2)


# list1 = [1, 4, 5, 7]
# list3 = list1.copy()
# list3.pop()
# assert(list3) == [1, 4, 5]



# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)



# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# (green, *tropic, red) = fruits

# print(green)
# print(tropic)
# print(red)


# cars = {
#     'brand': 'honda',
#     'product': 'civic'
# }
# e = cars.keys()
# print(list(e)[1])

# for key in cars.keys():
#     print(cars(key))

# assert(list(cars.keys())[1]) == 'product'
# print(cars.values())

# print(cars.get('year', None))
# print('Tidak akan dijalankan')

# if 'year' in cars:
#     print(cars['year'])

# cars.update(
#     {
#         'year': 2020,
#         'key2': 2121
#     }
# )

# cars['year'] = 2020
# print(cars)

# cars['brand'] = 'Toyota'
# print(cars)

# def my_function(fname):
#   print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil", "Refsnes")


# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")


# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# def full_name(lname, fname):
#     print(fname + ' ' + lname)

# full_name(fname='Emil', lname='Tobias')



# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")



# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")



# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)



# def my_function(x):
#   return 5 * x

# print(my_function(3))
# print(my_function(5))
# print(my_function(9))



# def myfunction():
#   pass


# def multiply_by_two(x):
#     return x * 2

# assert(multiply_by_two(3)) == 6


# def multiply_by_x(x, y = 2):
#     return x * y

# assert(multiply_by_x(3)) == 6
# assert(multiply_by_x(3, 1)) == 3

# user_input = input('Isi Umur : ')
# print(type(user_input))

# user_input = input('Input di kali dengan 2 : ')
# print(multiply_by_two(int(user_input)))

# how_many_input = input('Berapa kali ingin input data? ')
# i = 0
# while True:
#     if i == int(how_many_input):
#         break

#     user_input = input('Input dikali 2 : ')
#     print(multiply_by_two(int(user_input)))
#     i += 1



"""
Enter the number of students in your class: 3
Enter the name of student 1: Emil
Enter the grades of student 1 (comma-separated): 85,90,92
Enter the name of student 2: Tobiaz
Enter the grades of student 2 (comma-separated): 78,80,84
Enter the name of student 3: Refsnes
Enter the grades of student 3 (comma-separated): 92,95,98

Average grades:
Alice: 89.0
Bob: 80.67
Charlie: 95.0
"""

def totalGrades(grades):
    grade = 0
    grades = grades.split(',')
    for i in grades:
        grade += float(i)
    grade = grade/len(grades)
    return grade

how_many_input = input("Enter the number of students in your class: ")
students = []
for i in range(int(how_many_input)):
    name = input('Enter the name of student ' + str(i+1) + ': ')
    grades = input('Enter the grades of student '+ str(i+1) + ' (comma-separated) : ')
    students.append(
        {
            'nama' : name,
            'grade' : grades,
            'avg_grade' : totalGrades(grades)
        }
    )

print('Averange grade : ')
for z in students:
    print(z['nama'], ":", z['avg_grade'])
