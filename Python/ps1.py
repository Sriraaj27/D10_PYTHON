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
    and extra: find the most frequent character
"""

# s='aaabbbbccdddaabbb'
# d={}
# for char in s:
#     if char in d:
#         d[char]+=1
#     else:
#         d[char]=1
# max_char=''
# max_count=0
# for key,value in d.items():
#     if value>max_count:
#         max_char=key
#         max_count=value
# for k, v in d.items():
#     print(f"{k}{v}",end='')
# print()
# print(f"Most Repeating Character is {max_char} and its frequency is {max_count}")

"""
Move the Zeros to the end of the list
l=[1,0,9,2,0,1]
"""

""" Method - 1 """
# l=[1,0,9,2,0,1]
# l1=[]
# l2=[]
# for i in l:
#     if i==0:
#         l1.append(i)
#     else:
#         l2.append(i)
# print(l2+l1)

""" Method - 2 """
l=[1,0,9,2,0,1]
print(sorted(l,reverse=True))