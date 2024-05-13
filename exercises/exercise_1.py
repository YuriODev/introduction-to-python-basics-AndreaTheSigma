# Exercise 1
# Your solution comes here
num1 = int(input("Enter a 5 digit number: "))
ones = (num1 // 10000) + ((num1 // 100) % 10) + (num1 % 10)
tens = ((num1// 1000) % 10) + ((num1 // 10) % 10)
print(str(ones) + str(tens))