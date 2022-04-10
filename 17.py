#prime number
a=input("Enter the number to check the prime number")
for x in range(2,int(a),1):
    if(int(a)%x==0):
        print("number is not prime")
        break
        
if(x==int(a)): print("number is prime")
