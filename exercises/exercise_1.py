# Exercise 1
# Your solution comes here
number = int(input("Enter a 5 digit number: "))
ones = number % 10
hundreds = number // 100
ten_thousands = (number // 10000) % 10
sum_of_digits = ones + hundreds + ten_thousands
print(f"The sum of the 1st, 3rd and 5th numbers is {sum_of_digits}")
