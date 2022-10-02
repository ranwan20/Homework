s = input("Please enter a string:")
n = 1
k = 1
i = 1
while i < len(s):
    if s[i] == s[i - 1]:
        k += 1
    else:
        k = 1
    if k > n:
        n = k
    i += 1

if n > 1:
    print("是")
else:
    print("否")
print(n)