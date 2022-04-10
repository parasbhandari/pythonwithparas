#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Dictionary is a collection which is ordered** and changeable. No duplicate members.  
from ast import List


list=["paras",True,3,6]
print(list)   
list.insert(3,"paras")   
print(list) 
list.append("khushbu")
print(list)    
list2=["hari","himlal","chandra"]
list.extend(list2)
print(List)
list.pop(3)
print(list)
list.remove("khushbu")
print(list)
list.clear()
print(list)