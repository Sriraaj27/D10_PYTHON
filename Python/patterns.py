# for i in range(3):                # 1 2 3
#     for j in range(1,4):          # 2 3 4
#         print(i+j,end=' ')        # 3 4 5
#     print()

for i in range(3):
    for j in range(1,4):
        print(chr(j+96),end=' ')
    print()
    

for x in range(1,4):
    for y in range(1,4):
        print(chr(y+64),end=' ')
    print()    