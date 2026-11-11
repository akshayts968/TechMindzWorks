
# # # Sort the list

# z = [11,-1,0,-88,999,300,-100,4,2,600]
# for i in range(len(z)):
#     for j in range(i+1,len(z)):
#         if z[i] > z[j]:
#             temp = z[j]
#             z[j] = z[i]
#             z[i] = temp

# print(z)

# # Output
# # [-100, -88, -1, 0, 2, 4, 11, 300, 600, 999]



# Count Divisor
# data = input("Enter values: ")
# z = data.split()
# l = int(z[0])
# r = int(z[1])
# k = int(z[2])
# count = 0
# for i in range(l,r+1):
#     if i % k == 0:
#         count += 1

# print(count)

# Output
# Enter values: 1 10 1
# 10