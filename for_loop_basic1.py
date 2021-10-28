for x in range(0,151):
    print(x)
for x in range(5,1005,5):
    print(x)
for x in range(1,101):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)
sum = 0
for i in range(1,500000,2):
    sum += (i)
    print("The final sum is",str(sum))
for x in range(2018,0,-4): 
    print(x)
lowNum = 2
highNum = 20
mult = 2
for x in range(lowNum,highNum,mult):
    if x % 4 == 2:
        print(x)