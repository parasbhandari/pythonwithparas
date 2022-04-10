#tuples::A tuple is a collection which is ordered and unchangeable.
x = ("paras", "khushbu")

print(list)
##to upadate tuple
list1=list(x)
list1[1]="himlal"
x=tuple(list1)
print(x)
##add element
a=("paras","khushbu","himlal","hari")
b=list(a)
b.append("paras")
a=tuple(b)
print(a)


##unpack the tuple
x=("paras",)
y=x
print(y)
x=("paras","khushbu","himlal","hari")
p,k,h,hi=x
print(p)
print(k,h,hi)
p,*k=x;
print(p)
print(k)