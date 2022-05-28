number = int(input())

total_sum = 0

while True:
    a = int(input())
    total_sum += a
    if total_sum >= number:
        break
print(total_sum)
