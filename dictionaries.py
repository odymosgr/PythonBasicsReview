# Dictionary: Key-Value pairs, Unordered, Mutable

mydict = {"name": "Max", "age": 25, "city": "New York", "lucky_number": 36}
print(mydict)

mydict2 = dict(name="Mary", age = 22, city="Boston")

value = mydict["name"]
print(value)

mydict["email"] = "coolmax@ror.md"
mydict["email"] = "prof_max@gmail.com"
print(mydict)

del mydict["email"] # or mydict.pop("email")

for key in mydict:
  print(key, mydict[key], sep= " = ")
# also possible to use mydict.keys() or mydict.values()
# or k, v in d.items():

mydict_cpy = mydict.copy() #or dict(mydict)

mydict.update(mydict2)
print(mydict)

# keys in dictionaries must be immutable, that means we can use also numbers, tuples
