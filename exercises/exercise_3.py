# Exercise 3
# Your solution comes here
um = int(input("Enter a number of seconds:   "))
hours = (num // 3600) % 24
minutes = (num // 60) % 60
seconds = num % 60
print(f"{hours}:{minutes:02d}:{seconds:02d}")