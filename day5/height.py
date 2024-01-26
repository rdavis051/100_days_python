# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# Don't change the code above

# Write your code below this row
cnt = 0
total_height = 0
for x in student_heights:
  cnt += 1
  total_height += x
  print(f'height {cnt} is {x}')
print (f'Total students: {cnt}')
print (f'Total height: {total_height}')
avg_height = round(total_height / cnt)
print (f'Average height: {avg_height}')
