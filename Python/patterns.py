for a in range(3):                # 1 2 3
    for b in range(1,4):          # 2 3 4
        print(a+b,end=' ')        # 3 4 5
    print()

print("---------------")
for i in range(3):                      # a b c
    for j in range(1,4):                # b c d
        print(chr(i+j+96),end=' ')      # c d e
    print()

print("--------------")

for x in range(3):                      # A B C
    for y in range(1,4):                # B C D
        print(chr(x+y+64),end=' ')      # C D E
    print()    