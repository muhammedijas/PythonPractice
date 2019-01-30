a={'name':'ijas','couses':['math','bio']}
# default is none
print(a.get('sub'))

print(a.get('sub','Not found'))

a['Age']=32
print(a)


age_var=a.pop('Age')
print(a)
print(a.keys())
print(a.values())

#to  make key value pairs
print(a.items())


for key in a:
    print(key)


for key,value in a.items():
    print(key,value)