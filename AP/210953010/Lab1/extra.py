n = int(input("Enter the number of employees: "))
list = []
for i in range(n):
    list.append(tuple(input("Emp_id name salary dob: ").split(" ")))
sorted_list = sorted(list, key=lambda x: int(x[0]))
print(sorted_list)
