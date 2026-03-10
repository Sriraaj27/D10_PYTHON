""" Vowels in Name"""

# name=input("Enter Your Name: ")
# for char in name:
#     if char in 'aeiouAEIOU':
#         print(char)

""" String as input to check the string is even length or odd
    split it into equal halfs
    check if two halfs are having equal vowels or not
    
"""

""" Method - 1 """

# name=input("Enter a Word: ")
# if len(name)%2==0:
#     name1=''
#     name2=''
#     for i in range(0,len(name)):
#         if i%2==0:
#             name1+=name[i]
#         else:
#             name2+=name[i]
#     print(name1,name2)
#     vowels1=0
#     vowels2=0
#     for char in name1:
#         if char in 'aeiouAEIOU':
#             vowels1=vowels1+1
#     for char in name2:
#         if char in 'aeiouAEIOU':
#             vowels2=vowels2+1
#     if vowels1==vowels2:
#         print("String is Even Lengthed and Both Divided String have Equal No. of Vowels")
#     else:
#         print("String is Even Lengthed, but Divided Strings Doesn't have Equal No. of Vowels")
# else:
#     print("{name} is Odd Lenghted")
    
""" Method - 2 """

# s='nisith'
# s_s1=0
# s_s2=0
# if len(s)%2==0:
#     s1=s[:len(s)//2]
#     s2=s[len(s)//2:]
#     for i in range(len(s1)):
#         if s1[i] in 'AEIOUaeiou':
#             s_s1+=1
#         elif s2[i] in 'AEIOUaeiou':
#             s_s2+=1
#     if s_s1==s_s2:
#         print("Both Equal")
        
""" Given a string, count the frequency of each character 
    ex: "aaabbbccdddaa"
    output as: a5b3c3d4(as string)
"""

s='aaabbbccdddaa'
d={}
for char in s:
    if char in d:
        d[char]+=1
    else:
        d[char]=1

for k, v in d.items():
    print(f"{k}{v}",end='')