p=int(input("Enter First Number:"))
q=int(input("Enter Second Number:"))
r=int(input("Enter Third Number:"))
if(p>q and p>r):
    print(p,"is greater")
elif q>r and q>p:
    print(q,"is greater")
elif r>q and r>p:
    print(r,"is greater")    
else:
    print(r,q,r,"are equals")    
