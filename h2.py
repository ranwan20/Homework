l = [1,2,3,4,5]
for i in range(len(l) - 1,-1,-1):
    print(l[i],end = " ")
print()

i = len(l) - 1
while i >= 0:
    print(l[i],end = " ")
    i = i - 1
print()

print(l[::-1])