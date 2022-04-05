'''
#if statement
a=10
if(a>0):
    print("positive integer") '''



'''a=-10
if(a>0):
    print("positive integer")
else:
    print("Not a positive integer")  '''




'''
#if-else statement
a=0
if(a>0):
    print("positive integer")
elif(a<0):
    print("Negative integer")
else:
    print("it's a zero") '''




'''
#if-elseif statement maximum of three
num1 = 10
num2 = 20
num3 = 30
if(num1>num2):
    if(num1>num3):
        print("num1 is greater")
    else:
         print("num3 is greater")
elif(num2>num3):
    print("num2 is greater")
else:
        print("num3 is greater")   '''



'''
#assigntment
a=input("please enter the value of a ")
if(((int(a) % 3) == 0) and ((int(a) % 5) == 0)):
    print("Zoom")
elif((int(a) % 5) == 0):
    print("Zap")
elif((int(a) % 3) == 0):
    print("Zip")
else:
    print("Invalid")   '''



'''
#while-loop
num=5
count=1
while count <= num:
    print("the current number is:",count)
    count += 1   '''

'''
#for-loop
for number in 1,2,3,4,5:
    print("The current number is",number)


start=1
end=10
step=2
for number in range(start,end,step):
    print("The current number is ",number)   '''




'''
#exercise
for number in range(1,5):
    print("The current number is ",number)
    print("----------------------")
for number in range(1,7,2):
    print("The current number is ",number)
    print("----------------------")
for number in range(5,0,-1):
    print("The current number is ",number)
    print("----------------------")'''



'''
#nested-loop
number_of_passengers=5
number_of_baggage=2
security_check=True
for passenger_count in range(1, number_of_passengers+1):
    for baggage_count in range(1,number_of_baggage+1):
        if(security_check==True):
            print("Security check of passenger:", passenger_count, "-- baggage:", baggage_count,"baggage cleared")
        else:
            print("Security check of passenger:", passenger_count, "-- baggage:", baggage_count,"baggage not cleared")


#nested-loop2
number_of_passengers=5
number_of_baggage=2
security_check=True
for passenger_count in range(1, number_of_passengers+1):
    baggage_count =1
    while (baggage_count<=number_of_baggage):
        if(security_check==True):
            print("Security check of passenger:", passenger_count, "-- baggage:", baggage_count,"baggage cleared")
        else:
            print("Security check of passenger:", passenger_count, "-- baggage:", baggage_count,"baggage not cleared")
        baggage_count+=1   '''




'''
#assignment
a=123
s=0
while(a>0):
    digit=a%10
    s=s+digit
    a=a//10
    
print(s) 
'''



'''
#break-pass-continue

for passenger in "A","A", "FC", "C", "FA", "SP", "A", "A":
    if(passenger=="FC" or passenger=="FA"):
        print("No check required")
        continue
    if(passenger=="SP"):
        print("Declare emergency in the airport")
        break
    if(passenger=="A" or passenger=="C"):
        print("Proceed with normal security check")
    print("Check the person")
    print("Check for cabin baggage")
    

#pass-command is a null statement
num=10
count=0
while(count <= num):
    if(count%2 == 0):
        pass
    else:
        print(count)
    count+=1  '''




'''
#leap-year
a=input("enter any year ")
if(((int(a)%4)==0)and((int(a)%100)!=0)or((int(a)%4)==0)):
    print("It's a leap year")
else:
    print("It's not a leap year") '''



'''
#prime number
n=input("Enter any number ")
i=2
flag=1
while(i<=(int(n))//2):
    if(int(n)%i==0):
        flag=0
        break
    i=i+1
if(flag==1):
    print("The given number is prime\n")
else:
    print("The given number is not a prime")   '''




'''
#fibonacci
n=input("Enter the value of n ")
i=0
f1=0
f2=1
while(i<int(n)):
    f3=f1+f2
    print(f1)
    f1=f2
    f2=f3
    i=i+1    '''
