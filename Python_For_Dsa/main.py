# variables are dynamically typed
n = 0
print("n =",n)

n = "abc"
print("n =",n)

# multiple assignments

n,m = 1, "abc"
print("n =",n)
print("m =",m)

n,m,z = False, "abc", 3.14
print("n =",n)
print("m =",m)
print("z =",z)

# Increment and Decrement
n = n + 1
n = n - 1
n+= 1
n-= 1
# n++ bad syntax in python

# If statements don't require parentheses
# or curly braces
n = 1
if n > 2:
    n -= 1
elif n == 2:
    n *= 1
else:
    n += 2

# Parentheses are needed for multi-line conditions
if (n > 2
    and m < 3):
    print("Condition met")

# while loops
n=0
while n < 5:
    print("n =", n)
    n += 1

# looping from i = 0 to 4
for i in range(5):
    print("i =", i)

# looping from i = 2 to 5
for i in range(2, 6):
    print("i =", i) 

# looping from i = 5 to 2 with step
for i in range(5, 1, -1):
    print("i =", i)

# Division is decimal by default
print(5/2)  # Output: 2.5

# Integer division with //
print(5//2)  # Output: 2

# Careful: most languages round towards zero by default
# so negative numbers will round down
print(-5//2)  # Output: -3

# Modulus operator
print(5%2)  # Output: 1

