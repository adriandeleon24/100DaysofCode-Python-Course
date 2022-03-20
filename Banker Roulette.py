import random

# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

num_of_items = len(names)
random_name = random.randint(0, num_of_items - 1)
sponsor = names[random_name] 
print( sponsor + " is going to buy the meal today!")