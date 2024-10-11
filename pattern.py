# for i in range(5):
#     for j in range(5-i-1):    # pyramid
#         print(' ',end='')
#     for j in range(i+1):
#         print('*',end=' ')
#     print()




# for i in range(4,-1,-1):    # Inverted pyramid    inverted+pyramid=Diamond
#     for j in range(5-i-1):
#         print(' ',end='')
#     for j in range(i+1):
#         print('*',end=' ')
#     print()

                                            # 1 

                                            # 2 3 
                                            # 4 5 6 
                                            # 7 8 9 10 
                                            # 11 12 13 14 15  
# c=0                                       
# for i in range(5):
#     for j in range(i+1):
#         c+=1
#         print(c,end=' ')
#     print()

# num = 65                          # character printing with number in a pattern

# for i in range(26):
#     for j in range(i+1):
#         print(chr(num),end=' ')
#         num+=1
#     print()




# 7 7 7 7 7 7 7

# 6 6 6 6 6 6

# 5 5 5 5 5 

# 4 4 4 4 

# 3 3 3 

# 2 2 

# 1

# for i in range(7,-1,-1):
#     for j in range(i,0,-1):
#         print(i,end=' ')
#     print()




# 1 1 1 1 1 1 1

# 2 2 2 2 2 2

# 3 3 3 3 3 

# 4 4 4 4 

# 5 5 5

# 6 6

# 7
# m=0
# for i in range(7,-1,-1):
#     m+=1
#     for j in range(i,0,-1):
#         print(m,end=' ')
#     print()

c=0                              # not done
for i in range(3):
    for j in range(c+1):
        c+=2
        print('*',end=' ')
    print()