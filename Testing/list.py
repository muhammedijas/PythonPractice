

name=[]
name.append('Ijas')
name.append('Test')

#insert can give location to add the list, which is the first argumnet
name.insert(1,'test0')

# you can also insert two lists,but it would come as list inside the main list. you can use extend to  merge both list
name1=[1,2,3]
name.extend(name1)

#to remove the last value from list. use pop, defaultly it would remove last item in the list
name.pop()

sorted=sorted(name)

name.index('Ijas',none)

#to check an item in list available in it or
print('Ijas' in Name)

#for getting index and value of list, use enumerate, also mention start value for it
for index,i in enumerate(name,start=1):
    print(index,i)

# to change the list to str, join only can used with string
name_str=',/'.join(name)

#name.reverse()
#name.sort()
#name.sort(reverse=True)

print(name)