#loop list
list=["paras","khushbu","himlal","hari"]
for x in range(len(list)):
    print(list[x])
    
    
newlist=[]
for x in list:
    if "a" in x:
        newlist.append(x)
print(newlist)
newlist=[x for x in list if "a" in x]
print(newlist)
#copy a list
new=newlist.copy()
print(new)
"""Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list"""