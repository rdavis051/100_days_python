#fruits = eval(input())
fruits = ["Apple", "Pear", "Orange"
          ]
# do not change the code above

# TODO: Catch the exceptions and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")


# Do not change the code below
make_pie(0)