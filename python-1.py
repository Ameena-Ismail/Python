# Basic
for x in range(0,151):
print(x) 



#Multiples of Five
for x in range(5,1000,5):
print(x)
 



#Counting, the Dojo Way
for x in range(1,101):
    print(x)
    if x%5==0:
       print("coding")
    else:
        print("Dojo")



#Whoa. That Sucker's Huge

sum=0
for x in range(0,500000):
    if x%2==1:
        sum=sum+x

print(sum)


#Countdown by Fours
for x in range(2018,0,-1):
    if x%4==0:
        print(x)



#Flexible Counter
lownum=5
highnum=10
mult=2

for x in range(lownum,highnum):
    if x%mult==0:
        print(x)
