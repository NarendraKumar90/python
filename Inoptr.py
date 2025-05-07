l1=[1,2,3,4,5]
print("Square is:")
for i in l1:
    print(i,"=",i*i)


print("==================Nested For loop==================")
for i in range(1,5,1):
    print("======================Table Of",i,"======================")
    for j in range(1,11,1):
        print(i,"*",j,"=",i*j)
