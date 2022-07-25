# 1st Nasive

dictionary = {}
 
keys = ['apple','mango','banana','lemon']
values = [1,2,3,4]
 
for key, value in zip(keys, values):
    dictionary[key] = value
print(dictionary)

# 2nd Efficient way
                        
dictionary = {}

keys = ['apple','mango','banana','lemon']

for idx, value in enumerate(keys):
	dictionary[idx] = value
print(dictionary)
