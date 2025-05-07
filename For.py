name="Narendra"
count=0
for nm in name:
    count=count+1
    print("Hi Singh")
print("Count is=",count)

print("===============For Demo==================")
for i in range(10):
     print(i+1,"Ram Ram")


print("===============Even Number==================")
print("Even Numbers:",end=' ')
for i in range(0,20,2):
     print(i," ",end=' ')     

print('\n',"===============Odd Number==================")
print("Odd Numbers:",end=' ')
Ototal=0
for i in range(1,20,2):
     print(i," ",end=' ')
     Ototal=Ototal+1
print('\n',"Total Odd Numbers:",Ototal)
