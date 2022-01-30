import readline


print("Loading the file")
f = open("test.txt")
print(f)
lines = f.readlines()
print(lines)

sum_1 = 0
for item in lines:
    sum_1 = sum_1 + int(item)
    print("The sum is:", sum_1)

print("The sum is also:", sum([int(x) for x in lines]))
