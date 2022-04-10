##dictionary
thisdictionay={
    
    "paras":"5",
    "khushbu":"4",
    "himalal":"2"
    }
print(thisdictionay["paras"])
print(thisdictionay.get("paras"))
thisdictionay["hari"]=55
print(thisdictionay)
#thisdictionay.upadate({"chandra": 41})
print(thisdictionay)
for x in thisdictionay.keys():
    print(x)
for x in thisdictionay.values():
    print(x)
for x, y in thisdictionay.items():
   print(x,y)
paras=dict(thisdictionay)
print(paras)
    