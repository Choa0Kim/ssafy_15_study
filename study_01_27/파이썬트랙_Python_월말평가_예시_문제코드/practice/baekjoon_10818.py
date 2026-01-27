N = int(input())
number = map(int, input().split())

for n in number :
    min_val = 0
    if n < number:
        min_val = n
for n in number:
    max_val = 0
    if n > number:
        max_val = n
print(min_val, max_val)
        