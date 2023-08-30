import random
keys = int(input("Enter the number of keys: "))
dictionary = {}
for i in range(keys):
    key = random.randint(1, 99)
    value = input(f"Enter the value for key {key}: ")
    dictionary[key] = value
print(dictionary)
num_list = []
concat = ""
string = input("Enter a string to be searched : ")
present = False
special = ""
for value in dictionary.values():
    try:
        num = float(value)
        num_list.append(num)
    except ValueError:
        if string == value:
            present = True
        is_special = all(char in "!@#$%^&*()[]/?`~<>" for char in value)
        if is_special:
            special = value
        concat += value
avg = sum(num_list) / len(num_list)
print("The average of the numbers are: ", avg)
print("The concatenated string is: ", concat)
if present == True:
    print("The string ", string, " is present in the dictionary")
else:
    print("The string ", string, " is not present in the dictionary")
if special == "":
    print("There are no strings with special characters")
else:
    print("The string with special characters is: ", special)
