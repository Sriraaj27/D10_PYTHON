"""
    list1=[[1,2,3],[3,4,5],[2,1,3]]
    give me the largest sum of all the nested lists
"""

# list1=[[10,20,30],[31,41,51],[2,1,3]]
# max_sum=0
# max_list=[]
# for i in list1:
#     sum=0
#     for j in i:
#         sum=sum+j
#     if sum>max_sum:
#         max_sum=sum
#         max_list=i
# print(f"Largest Sum amoung nested Lists is {max_sum} of {max_list}")    
# print(max_sum)

"""
    list2=[1,2,3,3,2,14,5,4,5,7] 
    output: remove duplicate values   
"""

"""Approach-1"""

# list2=[1,2,3,3,2,14,5,4,5,7]
# dt={}
# for i in list2:
#     if i in dt:
#         dt[i]+=1
#     else:
#         dt[i]=1
        
# # print(dt)
# for k,v in dt.items():
#     # print(v)
#     if v>1:
#         print(k,v)

"""Approach-2"""

# list2=[1,2,3,3,2,14,5,4,5,7]
# dt={}
# for i in list2:
#     if i in dt:
#         dt[i]+=1
#     else:
#         dt[i]=1
# print(list2)
# dup=[]
# for i in dt:
#     if dt[i]>1:
#         dup.append(i)
# print(dup)

""" 
sentence='python is a very powerful progremming language'
output should be 
opt=['python','is','a','very','powerful','progremming','language']
also amoung the strings in the output find the string whith highest length
"""

# sentence='python is a very powerful progremming language'
# # words=sentence.split()
# # print(words)
# word=''
# words=[]
# for i in sentence:
#     if i!=' ':
#         word+=i #in this word will store all chars until it hit a space then it goes to else
#     else:
#         words.append(word)
#         word=''#after the current loop is completed,we are emptying the cuurent word and initializing
#                 # current word and initializing it to 0 again
# words.append(word)
# print(words)

""" 
ip='aaabcccdde'
find the fisrt non repeating charater in the given string
"""

str='aaabcccdde'
temp=''
# for char in str:
    # if a in temp: