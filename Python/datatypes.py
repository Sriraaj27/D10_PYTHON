"""" 
datatypes--> datatypes specifies the type of data that is being stored in a varibale
based on type of data/value, datatype can be classified into different types. they are,
1. number type---> int, float & complex
2. text type---> string
3. sequence type----> list, tuple, sets, dictionary
4. boolean type----> bool
5. none type---> None 

but, datatypes primarily are of two different types. they are,
1. primitive datatypes---> int, float, boolean, string and None
2. Non-primitive datatypes---> list, tuple, sets, dictionary 

int(integer)--> whole numbers like 0,1,2,3,..
float ----> decimal values like 2.3, 34.55 etc
complex--> combination of real and imaginary. foe example, "4+3j"
           (here we cant define complex numbers as 4+j3)
           4 is real part and 3 is imaginary part
string--> group of characters, assigned to variable by enclosing 
          them in either single of double quotes
list--> ordered collection of values seperted by comma and enclosed in square brackets([])
        lists accept heterogeneus data(all types of data)
tuples->tuples are also used to store ordered collection of vales enclosed in parathesis()
        tuples are also heterogenus in nature
set-->set is used to store unordered collection of values enclosed in "{ }"
        set doesn't allow duplicates, it only stores unique values
        set displays unordered random collections

"""


# x=2
# y=2.3
# z=4+3j
# print(type(x))
# print(type(y))
# print(type(z))


""""
we can perform multiple operations on strings some of the operations are,
1. finding length of string using len()
2. accessing specific characters of a string using index(+ and - index)
"""
""" String: """
# str1="Data Science"
# print(type(str1))

# print(len(str1)) #length of string
# print(str1[3]) #Accessing a character
# print(str1[-10])

"""" Lists: 
        operations on lists are: (create, read, update and delete)
        as lists are mutable--> they consume more memory and gives less performance
"""
# list1=[1,2.3,'hi','hello',[10,11,12]] #creating list
# print(list1) #reading list
# print(type(list1))
# print(len(list1)) #length of list
# print(list1[2]) #accessing list elements
# print(list1[3][4]) #accessing specific characters of list elements, we firts accesing list
# element that is at index 3 and in that element, we are accessing character that's index is 4
# print(list1[4][-1]) #Nested List Accessing
# list1[3]='welcome' #updating list elements
# print(list1)
# del list1[2] #Deleting list elements
# print(list1)

"""Type Conversion: """
# num=12520
# print(type(num))
# #print(num[2])#we cant access a digit from a number we have convert it into a string and the access it
# num1=str(num)
# print(type(num1))
# print(num1[2]) 

"""
tuples-->
        we can only perform create and read operations on tuple
        update and deleting specific elemnet of tuple is not possible
        we can delete entire tuple but not specific element    
        tuples allow positive and negative indexing
"""
# tup1=(1,2.3,'hello')#creating tuple
# print(tup1)#reading tuple
# print(type(tup1))
# print(tup1[2])#positive indexing of tuple elements
# print(tup1[-3])#negative indexing of tuple values
# # tup1[2]='welcome' #tuple doesn't allow updating
""" tuple to list conversion:"""
# tup2=(1,2.3,'hello')
# list2=list(tup2)
# print(type(tup2))
# print(type(list2))
""" Sizes of list and tuple:
        to check size of a varible, we use method that is "__sizeof__()"
        syntax: "variable_name.__size0f__()"
"""
# list1=[1,2,3]
# tup1=(1,2,3)
# print(list1.__sizeof__())
# print(tup1.__sizeof__())

""" Sets--->we cannot perform read, update and deletion of specific element as set is unordered 
            and unindexed
            when set stores the elements, it will generate hashing values to all the elements 
            when whole set is numbers then, set will arrange the numbers in an order using 
            hashing values
            hashing value is known using method--> "hash()"
            hashing value of a number is the number itself and hashing value of a string will be 
            different everytime it is used 
            sets use hashing for security purpose.
"""
# set1={1,2.3,'hi','hello'}
# print(set1)
# print(type(set1))
