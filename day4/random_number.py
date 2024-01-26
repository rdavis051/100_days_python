import random

random_int = random.randint(1, 10)
print(random_int)
# random float between 0.0-1.0 (not including 1.0)
random_float = random.random()
print(random_float)

# If you wanted to create random float between 0-5, just mulitple the float by 5. 
# It will then be a float between 0.00000.. and 4.99999, but never greater than 5.
larger_float = random_float * 5
print(larger_float)
print("")
love_score = random.randint(1, 100)
print(f"Your love score is: {love_score}")

