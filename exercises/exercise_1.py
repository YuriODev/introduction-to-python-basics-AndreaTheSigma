# Exercise 1
# Your solution comes here
num = int(input("Enter a 5 digit number: "))
ones = (num // 10000) + ((num // 100) % 10) + (num % 10)
tens = ((num // 1000) % 10) + ((num // 10) % 10)
print(str(ones) + str(tens))