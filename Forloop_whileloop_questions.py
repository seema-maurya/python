
# For Loops:
# Question 1: Write a program to print the squares of numbers from 1 to 10 using a for loop.
for i in range(1, 11):
    print(i**2)



#Question 2: Write a program to iterate through a list of fruits and print each fruit with its index.

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)


#Question 3: Create a for loop that prints the even numbers between 1 and 20.


for i in range(1, 21):
    if i % 2 == 0:
        print(i)


#Question 4: Write a program to calculate the sum of all numbers from 1 to 100 using a for loop.

total = 0
for i in range(1, 101):
    total += i
print("Sum:", total)


# Question 5: Create a for loop that prints each character of a given string on a new line.

string = "Hello"
for char in string:
    print(char)





# While Loop

#Question 1: Write a program that uses a while loop to print numbers from 1 to 5.

i = 1
while i <= 5:
    print(i)
    i += 1


#Question 2: Create a while loop that asks the user to enter a password until the correct password is entered.

correct_password = "mypassword"
entered_password = ""
while entered_password != correct_password:
    entered_password = input("Enter the password: ")
print("Access granted!")


#Question 3: Write a program that calculates the factorial of a number entered by the user using a while loop.

num = int(input("Enter a number: "))
factorial = 1
i = 1
while i <= num:
    factorial *= i
    i += 1
print("Factorial:", factorial)


#Question 4: Create a while loop that continues to prompt the user for input until they enter "exit".

user_input = ""
while user_input != "exit":
    user_input = input("Type something (or 'exit' to stop): ")


#Question 5: Write a program that uses a while loop to count down from 10 to 1 and then prints "Lift off!"


count = 10
while count > 0:
    print(count)
    count -= 1
print("Lift off!")
