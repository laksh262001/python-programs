'''
#passport
observe1="What's happening!!"
def passport_check(passport_no):
    observe4="actual copied to formal"
    observe5="func. execution starts"
    if(len(passport_no)==8):
        if(passport_no[0]>="A" and passport_no[0]<="Z"):
            status="valid"
        else:
            status="invalid"
    else:
        status= "invalid"
    observe6="func. execution ends"
    return status
observe2="function with formal arg."
observe3="calling with actual arg."
passport_status=passport_check("M9993471")
print("Passport is",passport_status)
#observe1,2,3,4,5,6 are temporary variables used to explain this concept   '''




'''
#square of a number
def find_square(n):
    return n*n

n=float(input("Please enter any number "))
        
sq = find_square(n)
        
print("The square of a given number {0}={1}".format(n,sq))  '''





'''
#sum of n numbers
def sum_of_n_natural_numbers(num):
    if(num == 0):
        return num
    else:
        return (num + sum_of_n_natural_numbers(num - 1))
    
number = int(input("Please Enter any Number: "))

total_value = sum_of_n_natural_numbers(number)

print("Sum of Natural Numbers from 1 to {0} =  {1}".format(number, total_value))    '''






'''
def change_number(num):
    num+=10
def change_list(num_list):
    num_list.append(20)
num_val=10
print("****effect of pass by value****")
print("num_val before function call:", num_val)
change_number(num_val)
print("num_val after function call:", num_val)
print("-----------------------------------------------")
val_list=[5,10,15]
print("****effect of pass by reference****")
print("val_list before function call:", val_list)
change_list(val_list)
print("val_list after function call:", val_list)   '''






'''
def display1(flight_number, seating_capacity):
    print("Flight Number:", flight_number)
    print("Seating Capacity:", seating_capacity)
print("code-1: positional arguments")
display1("FN789",200)
#Uncomment and execute the below function call statement and observe the output
#display1(300,"FN123")
def display2(flight_number, seating_capacity):
    print("Flight Number:", flight_number)
    print("Seating Capacity:", seating_capacity)
print("-------------------------------------------------")
print("code-2: keyword arguments")
display2(seating_capacity=250, flight_number="FN789")
def display3(flight_number, flight_make="Boeing", seating_capacity=150):
    print("Flight Number:", flight_number)
    print("Flight Make:", flight_make)
    print("Seating Capacity:", seating_capacity)
print("-------------------------------------------------")
print("code-3: default arguments")
display3("FN789","Eagle")
#Uncomment and execute the below function call statements one by one and observe the output
#display3("FN234")
#display3("FN678","Qantas",200)
def display4(passenger_name, *baggage_tuple):
    print("Passenger name:",passenger_name)
    total_wt=0
    for baggage_wt in baggage_tuple:
        total_wt+=baggage_wt
    print("Total baggage weight in kg:", total_wt)
print("-------------------------------------------------")
print("code-4: variable argument count")
display4("Jack",12,8,5)
#Uncomment and execute the below function call statements one by one and observe the output
#display4("Chan",20,12)
#display4("Henry",23)            '''






'''
wt_limit=30
def baggage_check(baggage_wt):
    extra_baggage_charge=0
    if not(baggage_wt>=0 and baggage_wt<=wt_limit):
        extra_baggage=baggage_wt-wt_limit
        extra_baggage_charge=extra_baggage*100
    return extra_baggage_charge
def update_baggage_limit(new_wt_limit):
    wt_limit=new_wt_limit
    print("This airline now allows baggage limit till",wt_limit,"kgs")
print("This airline allows baggage limit till",wt_limit,"kgs")
print("Pay the extra baggage charge of",baggage_check(35),"rupees")
update_baggage_limit(45)
print("Pay the extra baggage charge of",baggage_check(35),"rupees")   '''


'''
#factorial
def factorial(num):#function definition
    
    fact=1;
    i=1
    while i<=int(num):
        fact=fact*i
        i=i+1
    return fact
    
num=input("Enter a number..");

result=factorial(int(num))

print("factorial of the number: %d" %result)

factorial(int(num))#function call     '''





'''
# Python program to check if number is Palindrome

def isPalindrome(n):  #user-defined function
    # calculate reverse of number
    reverse = 0
    reminder = 0
    while(n != 0):
        remainder = n % 10
        reverse = reverse * 10 + remainder
        n = int(n / 10)
    return reverse

# take inputs
num = int(input('Enter the number: '))

# calling function and display result
reverse = isPalindrome(num)
if(num == reverse):
  print(num,'is a Palindrome')
else:
  print(num,'is not a Palindrome')     '''



'''
import math

def divided_sum_val(my_val) :

   res = 0
   for i in range(2, int(math.sqrt(my_val)) + 1) :

      if (my_val % i == 0) :

         if (i == int(my_val / i)) :
            res = res + i
         else :
            res = res + (i + int(my_val / i))
   return (res + 1)

def check_amicable(x, y) :

   if (divided_sum_val(x) != y) :
      return False

   return (divided_sum_val(y) == x)

first_num = 220
second_num = 288
print("The numbers are :")
print(first_num)
print(second_num)
if (check_amicable(first_num, second_num)) :
   print ("The given numbers are amicable in nature")
else :
   print ("The given numbers are not amicable in nature")   '''








   




