# Make a function that raises the first number to the power of the second number. 
# Both numbers are positive integers. 

# Solution
def power (x,y):
    z = x**y
    return z

# Test
assert(power(2,3) == 8)
assert(power(1,0) == 1)
assert(power(0,0) == 1)
