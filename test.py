import json

characters = "\\"
path = 'temp.json'

with open('temp.json') as f:
    data = json.load(f)

#for x in range(len(characters)):
#    data = data.replace(characters[x],"")

with open(path, 'w') as f:
    json.dump(data,f)


with open('temp.json') as f:
    s = json.load(f)
print (data)
print (s)
print(type(s))