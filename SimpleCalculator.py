n=int(input("Enter a Number:"))
d=int(input("Enter a Number:"))
s=input("Operator:")
if(s=="+"):
    print("Answer=",n+d)
elif(s=="-"):
    print("Answer=",n-d)
elif(s=="*"):
    print("Answer=",n*d)
elif(s=="/"):
    print("Answer=",n/d)
elif(s=="//"):
    print("Answer=",n//d)
elif(s=="%"):
    print("Answer=",n%d)
else:
    print("Please Enter a Valid Operator")
