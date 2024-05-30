#!/usr/bin/env python
# coding: utf-8

# # Q1.What data type is each of the following (evaluate where necessary)?
# 5
# 5.0
# 5 > 1
# '5' 
# 5 * 2
# '5' * 2 
# '5' + '2'
# 5 / 2 
# 5 % 2 
# {5, 2, 1}
# 5 == 3
# Pi (the number)

# int 
# float 
# boolean
# string 
# int 
# string 
# string
# float 
# string
# set
# boolean
# float

# # Question 2
# Write (and evaluate) python expressions that answer these questions: a. How many letters are there in 'Supercalifragilisticexpialidocious'? b. Does 'Supercalifragilisticexpialidocious' contain 'ice' as a substring? c. Which of the following words is the longest: Supercalifragilisticexpialidocious, Honorificabilitudinitatibus, or Bababadalgharaghtakamminarronnkonn? d. Which composer comes first in the dictionary: 'Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein'. Which one comes last?

# In[3]:


print(len('Supercalifragilisticexpialidocious'))


# In[4]:


'ice' in 'Supercalifragilisticexpialidocious'


# In[5]:


len('Supercalifragilisticexpialidocious') 


# In[6]:


len("Honorificabilitudinitatibus")


# In[7]:


len("Bababadalgharaghtakamminarronnkonn")

# d. dictionary lists the words in alphabetic order 
First = Bartok
last = buxtehude
# In[ ]:





# # Question 3
# Implement function triangleArea(a,b,c) that takes as input the lengths of the 3 sides of a triangle and returns the area of the triangle. By Heron's formula, the area of a triangle with side lengths a, b, and c iss(s - a)(s - b)(s - c) , wheres = (a + b + c)/2 .
# 
# triangleArea(2,2,2) 1.7320508075688772

# In[8]:


import math 
def triangleArea(a,b,c):
   s =(a+b+c)/2 #perimeter of triangle
   area = math.sqrt(s * (s - a)*(s - b)*(s - c)) # area using heron's formula
   return area
print(triangleArea(2,2,2))


# In[ ]:





# # Question 4
# Write a program in python to separate odd and even integers in separate arrays. Go to the editor Test Data : Input the number of elements to be stored in the array :5 Input 5 elements in the array : element - 0 : 25 element - 1 : 47 element - 2 : 42 element - 3 : 56 element - 4 : 32 Expected Output: The Even elements are: 42 56 32 The Odd elements are : 25 47

# In[88]:


def separate_odd_even(arr):
    even_elements = []
    odd_elements = []
    for num in arr:
        if num % 2 == 0:       #check for input and output
            even_elements.append(num)
        else:
            odd_elements.append(num)
    return even_elements, odd_elements

num_elements = int(input("Input the number of elements to be stored in the array: "))

  
array = []                    #input
print(f"Input {num_elements} elements in the array:")
for i in range(num_elements):
    element = int(input(f"element - {i} : "))
    array.append(element)


even_elements, odd_elements = separate_odd_even(array)


print("The Even elements are:")          #output
print(" ".join(map(str, even_elements)))

print("The Odd elements are:")
print(" ".join(map(str, odd_elements)))


# # Question 5
# Write a function inside(x,y,x1,y1,x2,y2) that returns True or False
# depending on whether the point (x,y) lies in the rectangle with lower left corner (x1,y1) and upper right corner (x2,y2).

# In[82]:


def FindPoint(x1, y1, x2,y2, x, y) :
    if (x > x1 and x < x2 and
        y > y1 and y < y2) :
        return True
    else :
        return False
    
print(FindPoint(1,1,0,0,2,3))
print(FindPoint(-1,-1,0,0,2,3))


# In[ ]:





# # Question 6
# Use function inside() from part a. to write an expression that tests whether
# the point (1,1) lies in both of the following rectangles: one with lower left corner (0.3, 0.5) and upper right corner (1.1, 0.7) and the other with lower left corner (0.5, 0.2) and upper right corner (1.1, 2)

# In[83]:


def inside(x, y, x1, y1, x2, y2):
    return x1 <= x <= x2 and y1 <= y <= y2
point_x, point_y = 1, 1

# Rectangle 1
rect1_x1, rect1_y1 = 0.3, 0.5
rect1_x2, rect1_y2 = 1.1, 0.7

# Rectangle 2
rect2_x1, rect2_y1 = 0.5, 0.2
rect2_x2, rect2_y2 = 1.1, 2

# Check if the point (1, 1) is inside both rectangles
is_inside_both = (
    inside(point_x, point_y, rect1_x1, rect1_y1, rect1_x2, rect1_y2) and
    inside(point_x, point_y, rect2_x1, rect2_y1, rect2_x2, rect2_y2)
)

print(is_inside_both)  # Output: False


# In[ ]:





# # Question 7
# File bloodtype1.txt records blood-types of patients (A, B, AB, O or OO) at a clinic.
# Write a function bldcount() that reads the file with name name and reports (i.e.,
# prints) how many patients there are in each bloodtype.
# bldcount('bloodtype.txt')
# There are 10 patients of blood type A.
# There is one patient of blood type B.
# There are 10 patients of blood type AB.
# There are 12 patients of blood type O.
# There are no patients of blood type OO

# In[84]:


def bldcount(filename):
    
    with open(filename, 'r') as file:      # Read the file 
        data = file.read().split()         #split the file
    blood_types = ['A', 'B', 'AB', 'O', 'OO']
 
    counts = {blood_type: data.count(blood_type) for blood_type in blood_types}
    
    
    for blood_type, count in counts.items():
        if count == 0:
            print(f"There are no patients of blood type {blood_type}.")
        elif count == 1:
            print(f"There is one patient of blood type {blood_type}.")
        else:
            print(f"There are {count} patients of blood type {blood_type}.")


bldcount('bloodtype1.txt') #file name for output


# # Question 8
# Write a function curconv() that takes as input:
# 1. a currency represented using a string (e.g., 'JPY' for the Japanese Yen or
# 'EUR' for the Euro)
# 2. an amount
# and then converts and returns the amount in US dollars.
#  curconv('EUR', 100)
# 122.96544
#  curconv('JPY', 100)
# 1.241401
# The currency rates you will need are stored in file currencies.txt:
# AUD 1.0345157 Australian Dollar
# CHF 1.0237414 Swiss Franc
# CNY 0.1550176 Chinese Yuan
# DKK 0.1651442 Danish Krone
# EUR 1.2296544 Euro
# GBP 1.5550989 British Pound
# HKD 0.1270207 Hong Kong Dollar
# INR 0.0177643 Indian Rupee
# JPY 0.01241401 Japanese Yen
# MXN 0.0751848 Mexican Peso
# MYR 0.3145411 Malaysian Ringgit
# NOK 0.1677063 Norwegian Krone
# NZD 0.8003591 New Zealand Dollar
# PHP 0.0233234 Philippine Peso
# SEK 0.148269 Swedish Krona
# SGD 0.788871 Singapore Dollar
# THB 0.0313789 Thai Baht

# In[85]:


def curconv(currency, amount):
 
    exchange_rates = {}   #storing currency rates
    
    
    with open('currencies.txt', 'r') as file:
        for line in file:                            # Read the file
            parts = line.split()
            code = parts[0]
            rate = float(parts[1])
            exchange_rates[code] = rate
    
    
    if currency in exchange_rates:                   #conversion rate
        conversion_rate = exchange_rates[currency]
    
    
 
    amount_in_usd = amount * conversion_rate         #return amount in usd
    
    return amount_in_usd


print(curconv('EUR', 100))  # Output: 122.96544
print(curconv('JPY', 100))  # Output: 1.241401


# # Question 9 
# Each of the following will cause an exception (an error). Identify what type of
# exception each will cause

# In[86]:


R1 = 6 + 'aa'
print(R1)


# In[31]:


import math

result = math.sqrt(-1.0)


# In[30]:


list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 12 position is not available
item = list[12]


# In[32]:


print(x)


# In[33]:


with open('non_existent_file.txt', 'r') as file:
    content = file.read()


# # Question 10
# Encryption is the process of hiding the meaning of a text by substituting letters in the
# message with other letters, according to some system. If the process is successful, no
# one but the intended recipient can understand the encrypted message. Cryptanalysis
# refers to attempts to undo the encryption, even if some details of the encryption are
# unknown (for example, if an encrypted message has been intercepted). The first step
# of cryptanalysis is often to build up a table of letter frequencies in the encrypted text.
# Assume that the string letters is already defined as
# 'abcdefghijklmnopqrstuvwxyz'. Write a function called frequencies()
# that takes a string as its only parameter, and returns a list of integers, showing the
# number of times each character appears in the text. Your function may ignore any
# characters that are not in letters.
#  frequencies('The quick red fox got bored and went home.')
# [1, 1, 1, 3, 5, 1, 1, 2, 1, 0, 1, 0, 1, 2, 4, 0, 1, 2, 0, 2,
# 1, 0, 1, 1, 0, 0]
# frequencies('apple')

# In[90]:


def frequencies(text):
    
    letters = 'abcdefghijklmnopqrstuvwxyz'     #string of letters
      
 
    frequency_list = [0] * len(letters)           #frequencies of each letter
    
 
    text = text.lower()                         #convert to lower case
    
   
    for char in text:
                                              # Check if the character is a letter
        if char in letters:
            
            index = letters.index(char)
                                            
    frequency_list[index] += 1               #incrementing the list
    
    return frequency_list

frequencies('The quick red fox got bored and went home.')
[1, 1, 1, 3, 5, 1, 1, 2, 1, 0, 1, 0, 1, 2, 4, 0, 1, 2, 0, 2,
1, 0, 1, 1, 0, 0]
frequencies('apple')



# In[ ]:





# In[ ]:




