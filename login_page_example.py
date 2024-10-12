# login page example:
name = input("Enter username for login :")
password = input("Enter your password :")
if(name == "seema" and password == "12345"):
    print(f"Welcome  {name} to DIYA application")
else:
        print("Invalid login, please try again")


print("---------------------------------------------------------------------")
num = 5
if num > 10:
   print("greater")
else :
    print("smaller")


print("----------------Guess the number---------")
num = int(input("Enter your numbers :"))
if num == 0:
    print("it is not zero")
elif num > 10 :
    print("greater, please try again")
elif num < 10 :
    print("smaller , please try again")
elif num == 10 :
    print("it's correct, you won!")
else :
    print("please try again")


print("-------------------------Even/Odd-----------------")
for num in range(1,100) :
   if num % 2 ==0 :
    print(f" {num} is even")
else :
    print(f" {num} is odd")
