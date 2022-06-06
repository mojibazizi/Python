JIbfranchise = {'name': 'Mojib', 'age': 20, 'from': 'Calgary'}

#we can use the built-in .get function  to get the value 
#print(JIbfranchise.get('name'))

#another way to do it 

#we can get a value for a given key by using brackets
#print(JIbfranchise['name'])

#the .get function is good to use, incase the key doesn't exist

#print(JIbfranchise['state'])  ## KeyError will be generated if 'state' doesn't exist

#print(JIbfranchise.get('state')) # this will return 'None' ( a null value) if 'state' doesn't exist

#print(JIbfranchise.get('state', 'Jib')) #this will return a default 'Jib' if state doesn't exist

JIbfranchise['Sibling'] = 'Mosawer'

#Dictionaries can include other dictionaries or lists as values

#Or we can add the key value pairs from one dictionary to another using the built-in dictionary update method. 

person_attributes = {'martial status': 'single'}

JIbfranchise.update(person_attributes)

print(JIbfranchise)