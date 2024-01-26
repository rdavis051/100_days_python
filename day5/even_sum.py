# Get the sum of all even number up to 1000

target = int(input()) # Enter a number between 0 and 1000

# Do not change the code above

# Write you code here

total = 0 
for number in range(0, target + 1, 2):
    total += number
print(total)

