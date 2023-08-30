fname = input("ENter file name: ")
f = open(fname, "w")
print("Enter the text(Press q to exit)")
while True:
    n = input()
    if n == "q":
        break
    f.writelines(n + "\n")
f.close()
f = open(fname, "r")
x = f.read()
f.close()
data = dict()
f = open(fname, "r")
line_number = 1
line = f.readline()
while line:
    line = line.strip()
    l1 = []
    l2 = []
    l1 = line.split()
    for word in l1:
        l2.append(len(word))
    data[line_number] = l2
    line = f.readline()
    line_number += 1
f.close()
print("Data is: ", data)

frequency = {}
f = open(fname, "r")
while True:
    char = f.read(1)
    if not char:
        break
    if char.isalpha():
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
print(frequency)
