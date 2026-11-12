numbers = [1,2,4,3,5,6,7,8]
n=9

# for i in range(1,n+1):
#     if i not in numbers:
#         print("Missing number: ",i)
#         break


sum = 0
osum = n*(n+1)/2
for i in numbers:
    sum += i
    # print(sum)

miss = int(osum - sum)
print("Missing value: ",miss)




























# check = False
# for i in range(1,n+1):
#     for j in numbers:
#         if i == j:
#             check = True
#     if check:
#         check = False
#     else:
#         print("Missing number: ",i)
#         break