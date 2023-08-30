n = int(input("Enter the size of list:"))
l1 = []
l2 = []
print("Enter the numbers of first list")
for i in range(n):
    l1.append(int(input()))
print("The numbers in the list are: ", l1)
print("Enter the numbers of second list")
for i in range(n):
    l2.append(int(input()))
l3 = [x for x in l1 if x % 2 != 0] + [x for x in l2 if x % 2 == 0]
print("The odd numbers in the list one and even numbers in list two  are: ", l3)
