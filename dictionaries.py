var = {}

print(var)
print(type(var))

var2 = {"fruit": "apple", "juice": "cranberry", "food": "spaghetti"}

print(var2)

print(var2["juice"])


for k, v in var2.items():
    print(k,v)
    
   
var2["drank"] = "patron"
print(var2)
  
var2["fruit"] = "grape"
print(var2)
  
var2["fruit"] = ["apple", "grape"]
print(var2)
print(var2['fruit'][0])

print(list(var2.keys()))
print(list(var2.values()))

print(dir(var2))

  
   
   
   
   
    #["apple", "grape"]