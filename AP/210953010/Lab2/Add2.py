l1 = [1, 2, 3, 4, 5]
l2 = [2, 3, 4, 5, 6]
union = []
for i in l1:
    union.append(i)
for i in l2:
    if i not in union:
        union.append(i)
print(union)

intersection = []
for i in l1:
    if i in l2:
        intersection.append(i)

print(intersection)
diff = []
for i in l1:
    if i not in l2:
        diff.append(i)
print(diff)
