# Exercise 4
# Your solution comes here
num = int(input())
dig1 = num // 1000
dig2 = (num % 1000) // 100
dig3 = (num % 100) // 10
dig4 = num % 10
diff = abs((dig1 - dig4) + (dig2 - dig3))
print(max(1 - diff, 0))