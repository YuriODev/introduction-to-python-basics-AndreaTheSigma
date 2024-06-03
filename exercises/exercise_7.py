# Exercise 7
# Your solution comes here
num = int(input("Enter a 4 digit number: "))
ones = num % 10
tens = (num // 10) % 10
hundreds = (num // 100) % 10
thousands = num // 1000
output = ones + tens + hundreds + thousands
print(output)