bills = [10,5,5,5,10,20]
check = True
remain = [0,0,0]


for i in bills:
    if i == 5:
        remain[0] += 1
    elif i == 10:
        if remain[0] > 0:
            remain[0]-=1
            remain[1] += 1
        else:
            check = False
            break
    else:
        if remain[1] > 0 and remain[0] > 0:
            remain[0] -= 1
            remain[1] -= 1
            remain[2] += 1
        elif remain[0] > 2:
            remain[0] -= 3
            remain[2] += 1
        else:
            check = False
            break

print(check)
print(remain)