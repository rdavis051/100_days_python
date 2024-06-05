import pandas

# with open("file1.txt") as file1:
#     list1 = file1.readlines()
#
# with open("file2.txt") as file2:
#     list2 = file2.readlines()
#
# print(list1)
# print(list2)

# result = [int(num) for num in list1 if num in list2]
# print(result)

## This is Dictionary Comprehension examples

# stucture #

#new_dict = {new_key:new_value for (key, value) in dict.items() if test}

#student_scores = {new_key: new_value for item in list}

# Examples
# sentence = input()
# words = sentence.split()
# print(words)
# result = {word:len(word) for word in words}
# print(result)

####################
# def c_to_f(temp_c):
#     temp_f = (temp_c * 9/5) + 32
#     return temp_f
#
# weather_c ={
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24
# }
#
# weather_f = {day: c_to_f(temp) for (day, temp) in weather_c.items()}
# print(weather_f)

###############
# iteration of a loop over pandas

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# # looping through dictionaries
# for (key, value) in student_dict.items():
#     print(key)
#     print(value)
#
# print()

# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
#
# print()
# Loop through data frame using for-loop - doesn't give us much info that makes sense when reading
# for (key, value) in student_data_frame.items():
#     print(value)

# Loop through rows of a data frame
# for(index, row) in student_data_frame.iterrows():
#     print(row)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(data)
#print(data.to_dict())
#print(nato_pa.letter)
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
#print(phonetic_dict)

word = input("Please enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)