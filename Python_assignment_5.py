#Q-1 Python program to print all negative numbers in a range
# Python program to print negative Numbers in given range
  
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
  
# iterating each number in list
for num in range(start, end + 1):
      
    # checking condition
    if num < 0:
        print(num, end = " ")

#Q-2 Remove multiple elements from a list in Python
# Python program to remove multiple
# elements from a list
 
# creating a list
list1 = [11, 5, 17, 18, 23, 50]
 
# Iterate each element in list
# and add them in variable total
for ele in list1:
    if ele % 2 == 0:
        list1.remove(ele)
 
# printing modified list
print("New list after removing all even numbers: ", list1)

#Q-3 write a Python program to Remove empty List from List
# Python3 code to demonstrate 
# Remove empty List from List
# using list comprehension
  
# Initializing list 
test_list = [5, 6, [], 3, [], [], 9]
  
# printing original list 
print("The original list is : " + str(test_list))
  
# Remove empty List from List
# using list comprehension
res = [ele for ele in test_list if ele != []]
  
# printing result 
print ("List after empty list removal : " + str(res))

#Q-4 write a Python program to Cloning or Copying a list
# Python program to copy or clone a list
# Using the Slice Operator
def Cloning(li1):
    li_copy = li1[:]
    return li_copy
   
# Driver Code
li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)

#Q-5 write a Python program to Count occurrences of an element in a list
 # Python code to count the number of occurrences
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count
 
# Driver Code
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occurred {} times'.format(x, countX(lst, x)))

#Q-6 write a Python program to Remove empty tuples from a list
# Python program to remove empty tuples from a 
# list of tuples function to remove empty tuples 
# using list comprehension
def Remove(tuples):
    tuples = [t for t in tuples if t]
    return tuples
  
# Driver Code
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), 
          ('krishna', 'akbar', '45'), ('',''),()]
print(Remove(tuples))

#Q-7 write a Python program to Program to print duplicates from a list of integers
# Python program to print
# duplicates from a list
# of integers
def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated
 
# Driver Code
list1 = [10, 20, 30, 20, 20, 30, 40,
         50, -20, 60, 60, -20, -20]
print (Repeat(list1))

#Q-8 write a Python program to find Cumulative sum of a list
# Python code to get the Cumulative sum of a list
def Cumulative(lists):
    cu_list = []
    length = len(lists)
    cu_list = [sum(lists[0:x:1]) for x in range(0, length+1)]
    return cu_list[1:]
 
# Driver Code
lists = [10, 20, 30, 40, 50]

#Q-9 write a Python program to Sum of number digits in List
# Python3 code to demonstrate
# Sum of number digits in List
# using loop + str()
 
# Initializing list
test_list = [12, 67, 98, 34]
 
# printing original list
print("The original list is : " + str(test_list))
 
# Sum of number digits in List
# using loop + str()
res = []
for ele in test_list:
    sum = 0
    for digit in str(ele):
        sum += int(digit)
    res.append(sum)
     
# printing result
print ("List Integer Summation : " + str(res))

#Q-10 write a Python program to Break a list into chunks of size N
my_list = ['geeks', 'for', 'geeks', 'like',
           'geeky','nerdy', 'geek', 'love',
               'questions','words', 'life']
  
# Yield successive n-sized
# chunks from l.
def divide_chunks(l, n):
      
    # looping till length l
    for i in range(0, len(l), n): 
        yield l[i:i + n]
  
# How many elements each
# list should have
n = 5
  
x = list(divide_chunks(my_list, n))
print (x)

#Q-11 write a Python program to Sort the values of first list using second list
# Python program to sort
# one list using
# the other list
 
def sort_list(list1, list2):
 
    zipped_pairs = zip(list2, list1)
 
    z = [x for _, x in sorted(zipped_pairs)]
     
    return z
     
 
# driver code
x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
y = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
 
print(sort_list(x, y))
 
x = ["g", "e", "e", "k", "s", "f", "o", "r", "g", "e", "e", "k", "s"]
y = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
 
print(sort_list(x, y))