#  ***    ****    ****   ****   *****
# *   *   *   *  *       *   *  *
# *****   ****   *       *   *  ****
# *   *   *   *  *       *   *  *
# *   *   ****    ****   ****   *****

# *****   ****   *   *  *****    *** 
# *      *       *   *    *       *  
# ****   * ***   *****    *       *  
# *      *   *   *   *    *     * *  
# *       ****   *   *  *****    **  

# *   *  *      *   *  *   *   ***   
# *  *   *      ** **  **  *  *   *  
# ***    *      * * *  * * *  *   *  
# *  *   *      *   *  *  **  *   *  
# *   *  *****  *   *  *   *   ***   

# ****    ***   ****    ****  *****  
# *   *  *   *  *   *  *        *    
# ****   *   *  ****    ***     *    
# *      *  **  *  *       *    *    
# *       ****  *   *  ****     *    

# *   *  *   *  *   *  *   *  *   *  
# *   *  *   *  *   *   * *    * *   
# *   *  *   *  * * *    *      *    
# *   *   * *   ** **   * *     *    
# ***     *    *   *  *   *    *    

# *****                              
# *                               
# *                                
# *                                 
# *****



# A


# num = 5

# for i in range(num):
#     for j in range(num):
#         if i == num//2  or (j == 0 or j == num - 1) and i!=0 or i == 0 and (j!=0 and j!=num - 1):
#             print(end="*")
#         else:
#             print(end=" ")
#     print()


# # Output

#  *** 
# *   *
# *****
# *   *
# *   *



# # B

# num = 5

# for i in range(num):
#     for j in range(num):
#         if i == 0 and j!=num -1 or i == num//2 and j!=num -1 or i == num - 1 and j!=num -1 or j == 0:
#             print(end="*")
#         elif j == num - 1 and i != 0 and i!= num -1 and i != num//2:
#             print(end="*")
#         else:
#             print(end=" ")
#     print()


# # Output

# # **** 
# # *   *
# # **** 
# # *   *
# # **** 


# # c


# num = 5
# for i in range(num):
#     for j in range(num):
#         if j == 0 and i != 0 and i != num - 1 :
#             print(end="*")
#         elif (i == 0 or i == num - 1 ) and j != 0:
#             print(end="*")
#         else:
#             print(end=" ")
#     print()


# # Output

# #  ****
# # *    
# # *    
# # *    
# #  ****


# # D

# num = 5

# for i in range(num):
#     for j in range(num):
#         if (i == 0 or i == num -1) and j!=num - 1:
#             print(end="*")
#         elif (j == 0 or j == num -1) and i != 0 and i != num - 1 :
#             print(end="*")
#         else:
#             print(end=" ")
#     print()

# # # Output

# # **** 
# # *   *
# # *   *
# # *   *
# # **** 

# # E

# num = 7

# for i in range(num):
#     for j in range(num):
#         if i == 0 and j!=num -1 or i == num//2 and j!=num -1 or i == num - 1 and j!=num -1 or j == 0:
#             print(end="*")
#         else:
#             print(end=" ")
#     print()

# # Output

# # **** 
# # *    
# # **** 
# # *    
# # **** 


# # F

# num = 5
# for i in range(num):
#     for j in range(num):
#         if j == 0:
#             print(end="*")
#         elif i == 0 or i == num // 2:
#             print(end="*")
#         else:
#             print(end=" ")
#     print()


# # # Output

# # *****
# # *    
# # *****
# # *    
# # *    


# # G

# num = 5
# for i in range(num):
#     for j in range(num):
#         if (i == 0 or i == num - 1) and j != 0:
#             print(end="*")
#         elif i != 0 and i != num - 1 and j == 0:
#             print(end="*")
#         elif i != 0 and i != num - 1 and j == num - 1 and i >= num // 2:
#                     print(end="*")
#         elif j != 0 and j!= num - 1 and j >= num//2 and i == num//2:
#             print(end="*")
#         else:
#             print(end=" ")
#     print()

# # # Output


# #  ****
# # *    
# # * ***
# # *   *
# #  ****


# # H

# num = 5
# for i in range(num):
#     for j in range(num):
#         if j == 0 or j == num - 1 or i == num//2:
#             print(end="*")
#         else:
#             print(end=" ")
#     print()

# # # Output


# # *   *
# # *   *
# # *****
# # *   *
# # *   *


# # I

# num = 5
# for i in range(num):
#     for j in range(num):
#         if i == 0 or i == num - 1 or j == num//2:
#             print(end="*")
#         else:
#             print(end=" ")
#     print()

# # Output

# # *****
# #   *  
# #   *  
# #   *  
# # *****



# # J

# num = 5
# for i in range(num):
#     for j in range(num):
#         if j == num//2+1:
#             print(end="*")
#         elif i == 0 and j!=0 and j!=1:
#             print(end="*")
#         elif i > num // 2 and i - j == 2:
#             print(end="*")
#         else:
#             print(end=" ")
#     print()

# # Output

# #  ***
# #    * 
# #    * 
# #  * * 
# #   ** 

# # K

# num = 5
# for i in range(num):
#     for j in range(num):
#         if j == 0:
#             print(end="*")
#         elif (i + j == num - 1 or i == j ) and j >= num // 2 :
#             print(end="*")
#         elif j < num // 2 and i == num // 2:
#             print(end="*")
#         else:
#             print(end=" ")
#     print()


# # Output

# # *   *
# # *  * 
# # ***  
# # *  * 
# # *   *

# # L

# num = 5
# for i in range(num):
#     for j in range(num):
#         if j == 0 or i == num - 1:
#             print(end="*")
#         else:
#             print(end=" ")
#     print()

# # Output

# # *    
# # *    
# # *    
# # *    
# # *****


# # M

# num = 5
# for i in range(num):
#     for j in range(num):
#         if j == 0 or j == num - 1:
#             print(end="*")
#         elif i == j and i <= num // 2:
#             print(end="*")
#         elif i + j == num - 1 and i <= num // 2:
#             print(end="*")
#         else:
#             print(end=" ")
#     print()


# # Output

# # *   *
# # ** **
# # * * *
# # *   *
# # *   *



# # N


# num = 5
# for i in range(num):
#     for j in range(num):
#         if j == 0 or j == num - 1:
#             print(end="*")
#         elif i == j:
#             print(end="*")
#         else:
#             print(end=" ")
#     print()

# # Output

# # *   *
# # **  *
# # * * *
# # *  **
# # *   *


# O 

# num = 5
# for i in range(num):
#     for j in range(num):
#         if (j == 0 or j == num - 1) and (i != 0 and i != num - 1):
#             print(end="*")
#         elif (i == 0 or i == num - 1) and (j != 0 and j != num - 1):
#             print(end="*")
#         else:
#             print(end=" ")
#     print()

# Output

#  *** 
# *   *
# *   *
# *   *
#  *** 



# # S


# num = 5
# for i in range(num):
#     for j in range(num):
#         if i == 0  and j !=0 :
#             print(end="*")
#         elif i == num - 1 and j != num - 1:
#             print(end="*")
#         elif j == 0 and i < num // 2 and i !=0 :
#             print(end="*")
#         elif j == num - 1 and i > num // 2 and i !=num - 1 :
#                     print(end="*")
#         elif  i == num // 2 and (j!=0 and j!=num - 1) :
#             print(end="*")
#         else:
#             print(end=" ")
#     print()



# # Output

# #  ****
# # *    
# #  *** 
# #     *
# # **** 



# # P 


# num = 5

# for i in range(num):
#     for j in range(num):
#         if i == 0 and j!=num - 1 or j == 0 or i == num //2 and j!=num - 1:
#             print(end="*")
#         elif i < num // 2 and j == num - 1 and i != 0:
#             print(end="*")
#         else:
#             print(end=" ")
#     print()


# # Output

# # **** 
# # *   *
# # **** 
# # *    
# # *    