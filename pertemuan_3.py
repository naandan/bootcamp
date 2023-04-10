# import mathemathic

# print(mathemathic.multiply_by_two(4))


# from mathemathic import multiply_by_two, operators

# print(multiply_by_two(3))
# print(operators)

thisdict = [
 	 {
         "brand": "Ford",
         "model": "Mustang",
         "year": 2000
  	 },
 	 {
         "brand": "Honda",
         "model": "Civic",
         "year": 1945
  	 },
 	 {
         "brand": "Toyota",
         "model": "Alphard",
         "year": 2018
  	 },
     {
         "brand": "Lamborghini",
         "model": "Aventador",
         "year": 1976
  	 }
]
for t in len(thisdict):
    # print(t)
	if thisdict[t-1]['brand'] == "Toyota":
    	    thisdict[t-1]['model'] = '2000'

print(thisdict)
# print(type(len(thisdict)))
# print(range(len(thisdict)))