## Python 3

# this is For Comments
 
print("Hello\nWorld") # \n for next line

print("Praneet\t Niranjan") # \t for tab space 

print("this is backslash \\") # \\ for backslash

print("Line A \\n Line B")  # to print \n between words

print("Line A \\t Line B ")

print(" \" \' ") # to print " or '  use \" ...

### Raw Strings:-

print(r"Line A \n Line B")  # by using r we reduce to write escape sequences

print(r"Line A \t Line B") # Example to not need to write the escape sequence

## To Print emoji 

print("\U0001F604")   # emoji code link : https://unicode.org/emoji/charts/full-emoji-list.html 

print(2/4)   # floating point division

print(4 // 2)  # integer point division

print(2**3)  ## two ki power 3 

print(round(2**0.5,4)) # round off

print(3%2)  ## modulo operator 

## Variable (names can't start with numbers or special symbols, can't use any special symbol within variables, can star with letters, _ )...Python is a dynamic language

s = "Praneet"
print(s)
            ## Dynamic language
s= 5
print(s) 

user_case_writing = "Praneet"  ## snake case writing (should be use in python)
camelUseCase = "Niranjan"      ## camel case writing  (uses in java)

## Strings in pyhton
## collection of characters inside double quotes or in single quotes

first_name = "Praneet"
Last_name = 'Niranjan'
print(first_name + " " + Last_name )

#print(first_name + 3) ## type error 
print(first_name + "3")

print(first_name + str(3)) ## by using str() function

print(first_name * 3) ## print number of times

# user input in python 3

name = input("type your name")
print(name)

## input function always take the input in string format

age = input("enter your age")
print("ur age is " + age)

## int() function to convert string into integer value

first = int(input("enter your first number:"))
second = int(input("enter your second number:"))
total = first + second
print("total sum is :" + str(total))


## str() = 4 --> "4",   int() = "4" -->4,  float() = "4" --> 4.0

# two or more variables in one line 

name, age = "Praneet" , 24
print("hello" +name + "ur age is " + str(age))

x=y=z=1
print(x+y+z)

## two or more input in one line 

name, age = input("Enter your name and age").split()  ## split by , is split(",")
print(name)
print(age)

## String Formatting

name = "Praneet"
age = 23

print("hello {} your age is {} ".format( name , age )) ## python 3

print(f"hello {name} your age is {age}")  ## pyhton 3.6

## String indexing

language = "Praneet"
print(language[2])
print(language[-1])  ## to print last character

## String slicing

lang = "Praneet"
print(lang[0:2])   ## lang[starting index: stoping index -1]

print("praneet"[2:6:2])   

print("praneet"[-1::-1]) ## to reverse a string

## Reverse a string in reverse order :

name = input("Enter your name :")
print("your name in reverse order: " + name[-1::-1])

## String Methods:

# len() method :- to give length of a string
print(len(name))

# lower() :- to lower the characters same as upper()
print(name.lower())

# title() :- to make strings in title format like first character will be capital and rest of them will be small
print(name.title())

# count() :- to count characters in a string
print(name.count(" "))


# strip() method: to clear the spaces around the string

name = "     Praneet     "
print(name.lstrip())  # To remove the left side spaces
print(name.rstrip())  # To remove the right side spaces
print(name.strip())   # To remove the unecessary spaces 


name.replace(" ", "")  # To remove the spaces between characters ex: "Pra   neet" or we can replace the anything by anything in a string

print(name.find("p")) # find position in strings

print(name.center('String_length_no. + * Count',"*" ))  # Ex: *Praneet* if center(9,"*") put or [**Praneet**] if center(11,"*")

## Strings are immutable in python

string = "Praneet" ## can't change to string = "Niranjan"
print(string[2])

## By using replace method we can change create new string by changing the old string but ol one still remain the same 
new_string = string.replace("t", "T")


string = string + "niranjan"  ## we can add characters to string 


## If conditions 

age = input("Enter your age")
age = int(age)

if age >=18:
    print("you are mataure and independent")   ## the space before print function is tab space which are required to reduce the need of {} these braces
elif age == 20:
    print("your age is 20")
else:
    print("age is greater than 20")    

if age == 18:
    pass         ## It means pass this step don't do anything


## Chcking two or more contions at the same time : operator = and & or 

name = " Praneet"
age = 29

if name == "Praneet" and age == 29:
    print("Conditions are true ")
else:
    print("Conditions are false") 

## In and(operator) both sides condition should be true and In or(operator) one side condition should be true        


  

######################################################################

## in keyword

name = "Niranjan"

if 'a' in name:
    print("a is present in name")



##### To check String is empty or not:

name = input("enter your string: ")

if name: 
    print(f"your string is : {name}")
else:
    print("you didn't type any string:")    


######### Loops

## While loop
i = 1
while i<=10:
    print(f"hello world {i}")
    i = i + 1

### Question of counting characters in input string : 
## solution: 

string = input("Enter your string: ")  # Praneet Niranjan
s = string.lower()
i=0
temp = ""
while i < len(s):
    if s[i] not in temp:
        temp += s[i]
        print(f"{s[i]} :  {s.count(s[i])}")
    i = i + 1


######## For Loop
## For loop with range function

for i in range(10):
    print("python 3")

## Break and Continue statements...

for i in range(10):
    if i == 5:
        break   ## after loop will break and then stop operations after that.
    print(i)

for i in range(10):
    if i == 5:
        continue    ## this step skip this instance and then continue the remaining operations...
    print(i)


#### Modify or number prediction game .....

## Modify number guesing  game:

import random
r = random.randint(1,100)   ## to take a random number ...

n = int(input("Enter you number: "))
g = 0
while True:
    if  r == n:
        print(f"You are win !!! The number of times u searched are: {g}")
        break
    else:
        if n < r:
            print("Too low")
            n = int(input("Enter number again: "))
            g = g+1
        else:
            print("Too high")
            g= g+1 


##############################################################################################################33
## DRY:- Don't repeat yourself...
## The above code is Rewritten by removing some repeated lines... Like ..

while True:
    if  r == n:
        print(f"You are win !!! The number of times u searched are: {g}")
        break
    else:
        if n < r:
            print("Too low")
        else:
            print("Too high")
    
    n = int(input("Enter number again: "))
    g = g+1


########################################################################################################################
## Step Argument in Range function :

for i in range(1,10,2):     ### to print odd numbers between 1 to 10 and to print even change the third argument..
    print(i)



########## For loop in python where strings are iterable....

name = "Praneet"

for i in name:
    print(i)

###### or sum of input numbers as a string 

number = input("Enter your number:")
total = 0
for i in number:
    total += int(i)

print(f"your sum is : {total}")  


################## Functions...

def add(a,b):
    return a+b

total = add(9,8)
print(total)


######## Palindrom question :

string = input("Enter your string: ")
rev = string[-1::-1]  ## or string[::-1]

if (string == rev):
    print(True)

else:
    print(False)

 ##### Fabonacci series...

n = int(input("Enter the number:"))
def fibonacci_ser(n):
    if n == 1:
        print(0)
    elif n == 2:
        print(0,b, " ")
    else:
        print(a)
        print(b)
        for i in range(n-2):
            c = a + b
            print(c)
            a = b
            b = c

#####  Default parameters:

def default_parameters(first_name, Last_name= 'unknown', age = None ):
    print(f"First Name {first_name}")
    print(f"Last_Name{Last_name}")
    print(age)
    
#### In above function the defualt parameters should be last element not the middle one 
#####  otherwise ... default_parameters(first_name, 25 ) = it gives error!!
 

## Global variable

x = 5

def fun():
    global x
    x = 7
    return x


print(fun())
print(x)    

###############################################################################################
## Lists in pyhton: Data structure which is Ordered collection of items ..and can store anything(int, float, string...)

numbers = [1,2,3,4,5,'Praneet',7,8]
print(numbers)

### By Using append method, add elements in a list !!
fruits =[]
fruits.append('mango')
fruits.append('apple')
fruits.append('orange')
print(fruits)

fruits.insert(1, 'grapes')  ## insert element at first position in a list !!!

fruits1 = ['apple', 'grapes']
fruits2 = ['mango', 'orange']

fruits = fruits1 + fruits2  ### Concatenation of lists!!

fruits = fruits1.extend(fruits2) ## Extend of lists!!

fruits = fruits1.append(fruits2)  ## List append another list ex : ['p','r','a', ['n','r','a']]

### pop() method of lists !!

fruits.pop() ## By default it will delete last element !!
fruits.pop(1) ## delete first element !!

fruits.remove('apple') ## if don't know the index, then remove method delete the element by name !!

fruits.count('grapes')  ## count the string number of times in a list !!

number = [1,5,3,2,7,3,24,9]
number.sort()  ## sort the number 

## Sorted method sort the list for instance not original one 

print(sorted(number))    ## This is sorted list !!
print(number)  ## original list remain the same !!

#### Like above we can use clear, copy, reverse... methods with lists !!!

(fruits1 == fruits2)  ## check equality !!
(fruits1 is fruits2)  ## check the objects are on the same memory space or not !! ex: = fruits1 = called as object




##################################################################################################################

# Split method: Converting strings into lists !!

info = 'Praneet Niranjan'.split()
print(info)    # prints like that : = ['Praneet', 'Niranjan']


# Join method: Converting Lists element into strings !!

info = ['Praneet', 'Niranjan']
print(','.join(info))   ## Join the strings by ',' 

######################################################################################################################


#### list vs array:
 
# c, c++, java : array int, string 

# List - store any data / flexible

# python array module - fix data type

# numpy arrays - Binding with c libraries (It's a type of module used in data science, ml, big data etc)

# javascript array = python List / flexible 

#######################################################################################################################

### List Vs Strings

# strings are immutable
# Lists are mutable

s = "string"
t = s.title()
print(t)   ## if print(s) : the string will remain same becoz of immutable !!


l = ['word1','word2','word3']
l.pop()    # It will change the original list by removing last element from list

 
 #### For Loop in python :

fs = ['A','O','G','M']
 
for f in fs:
     print(f)

####### List inside List : 

matrix = [[1,2,3],[4,5,6],[7,8,9]]  ## 2D List
# 3 items --> 3 List 
# print(matrix[1])  ## => [4,5,6]

for i in matrix:
    print(i)     ## =>   [1,2,3]
                 ##      [4,5,6]
                 ##      [7,8,9] 

### To print sublist :

for sublist in matrix:
    for i in sublist:
        print(i)


## To print any element inside the matrix:
print(matrix[2][1])  ## => 8


## type function:
s = 'Praneet' 
print(type(s))
print(type(matrix))   ### List type ka...

#########################################################

number = [1,2,3,4,5,6,7,8,9,10]

def function(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative    

print(function(number))


#### function of squares of each number :

num = [1,2,3,4,5,6,7,8,9,10]

def square(l):
    lst = []
    for i in l:
        lst.append(i*i)
    return lst 

print(square(num))

#### function of reverse of list using append method :

def revv(l):
    rev = []
    n = len(l)
    for i in l:
        rev.append(n-i)
    return rev

print(revv(num))


##### function which reverse the strings inside the list...

num = ['abc','defm','efgkl','hisj']

def Rev(l):
    m = []
    for i in l:
        r = rev(i)
        m.append(r)
    return m            

def rev(n):
    return(n[::-1])

print(Rev(num))


###### function to print the list containing odd and even lists together!!

num = [1,2,3,4,5,6,7,8,9,10]

def OE(l):
    f,e,o = [],[],[]
    for i in l:
        if (i%2==0):
            e.append(i)
        else:
            o.append(i)
    f.append(e)
    f.append(o)
    return f

print(OE(num))

## function to find common elements

n1 = [1,2,3]
n2 = [5,3,7,8,1]

def common(a,b):
    n=[]
    for i in a:                    ### Here we reduce to process the two for loops by one loop!!!!
        if i in b:
            n.append(i)
        else:
            continue
    return n

print(common(n1,n2))  


##################################################################################


### Mini and Maxi numbers in a List !! By Using the defaults functions...

num = [1,2,3,4,5,6,7,8,9,10]
print(min(num))                          
print(max(num))

def greatest_difference(num):
    print(max(num)-min(num))

###################################################################################

# Tuple data structure
# Tuple can store any data type
# most important tuples are immutable, once tuple is created you can't update
# data inside tuple


# no append, no insert, no pop, no remove
days = ('monday','tuesday')
# tuples are faster than lists

# Methods:-
# count, index 
# len function
# slicing
print(days[:2])








# looping in tuples
# tuple with one element 
# tuple without parenthesis
# tuple unpacking
# list inside tuple
# some functions that you can use with tuples


mixed = (1,2,3,4.0)

# for loop and tuple
for i in mixed:


# tuple without parenthesis
guitars = 'yamaha','baton rouge','taylor'
# print(type(guitars))

 
# tuples unpacking
gu = ('Maneli jamal','Eddie van', 'andrew foy')
gu1, gu2, gu3 = (gu)
# print(gu)

# list inside tuples
fav = ('southern magnolia',['Tokyo Ghoul Theme','landscape'])
fav[1].pop()
fav[1].append("We made it")
# print(favorites)

## we can use min,max and sum function!!!

#####################################################################################
# function returning two values
def func(int1, int2):
     add = int1 + int2
     multiply = int1*int2
     return add, multiply

# print(func(2,3))
add, multiply = func(2,3)
print(add)
print(multiply)

#####################################################################################

# something more about tuples , list, str

# nums = tuple(range(1,11))
nums = str((1,2,3,4,5,6,7,8,9,10))

# output = "(1,2,3,4,5,6,7,8,9,10)"

print(nums)
print(type(nums))

###########################################################################################

# Dictionaries:- unordered collections of data in key : value pair !!
# Use:- Becoz of limitatioins of lists, lists are not enough to represent real data!!

# Ex:= user = ['Harshit', 24, ['coco', 'Kimi no na wa'],['awakening', 'fairy tale']]
# this list contains user name, age, fav movies, fav tunes
# you can do this but this is not a good way to do this.

# how to create dictionaries:
user = {'name': 'Harshit' , 'age': 24}

# print(user)
# print(type(user))
	 


#########################################################
# which type of data a dictionary can store ?
# Anything
# numbers, string, list, dictionary

user_info = {
  'name' : 'harshit',
  'age' : 24,
  'fav_movies' : ['awakening', 'fairy tale'],
  'fav_tunes': ['coco', 'Kimi no na wa'],
}

print(user_info['fav_movies'])


# How to access data from dictionary
# NOTE- There is no indexing because of unordered collection of data !!
user['name']

## How to add data to empty dictionary
user_info2 = {}
user_info2['name'] = 'mohit'

print(user_info2)

###################################################################################
## There is a difference between list, tuples and dictionaries and we can verify by ([],() and {}) these respectively!!!

##############################################################################################################

## dictionary example:

def cube_finder(n):
  cubes = {}
  for i in range(1,n+1):
     cubes[i] = i**3
  return cubes

print(cube_finder(10))    ### Output: = {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000}


#######################################################################################################################

## word counter

def word_counter(s):
    count = {}
    for char in s:
        count[char] = s.count(char)
    return count

print(word_counter('Praneetn'))

##############################################################################################33333

# Set data type
# unordered collection of unique items

s= {1,2,3,2}
# print(s)

l= [1,2,3,4,5,6,3,2,4,5,7,8,1]
# remove duplicate
s2 = set(l)
print(s2)

s.add(4)           ## we can add element in a set
s.add(5) 
s.remove(3)        ## same as Remove
s.discard(6)       ## No error given, if present in a set it will remove otherwise no error given like remove
s.clear()          ## To clear set
s1 = s.copy()      ## To copy set 
print(s)


## We can't store lists or dictionaries in set{}
########################################################################

s1 = {1,2,3,4}
s2 = {3,4,5,6}

# union
# {1,2,3,4,5,6}

union_set = s1 | s2
print(union_set)

# intersection

intersection = s1 & s2
print(intersection)

##########################################################################
# list comprehension
# with the help of list comprehension we can create of list in one line

# create a list of squares from 1 to 10
squares = []
for i in range(1,11):
    squares.append(i**2)
print(squares)

# comprehension method:

square2 = [i**2 for i in range(1,11)]
print(square2) 


def reverse_string(l):
    return([name[::-1] for name in l])

##############################################################################

## comprehensionn method with if statement :!!
 
num = list(range(1,11))
n= []

n = [i for i in num if i%2==0]
print(n)

##############################################################################

# list comprehension with if else
nums = [1,2,3,4,5,6,7,8,9,10]
# output:-
# new_list = [-1,4,-3,8]  ## odd = -i or even = i*2

new_list2 = [i*2 if (i%2==0) else -i for i in nums]
print(nums)


############## list comprehension in nested list

example = [[1,2,3], [1,2,3], [1,2,3]]

nested_comp = [[i for i in range(1,4)] for j in range(3)]

######################################################################################
# dictionary comprehension
# square = {1:1, 2:4, 3:9}

square = {f"square of {num} is":num**2 for num in range(1,11)}
for k,v in square.items():
   print(f"{k} : {v}")

string = "Harshit"
for i in string:
    print(i)
# {'H' : 1, 'a' : 1}
word_count = {char:string.count(char) for char in string}
print(word_count)                									


######## dictionary comprehension with if else 
# d = {1:'odd', 2:'even'}

odd_even = {i:('even' if i%2==0 else 'odd') for i in range(1,11)}
print(odd_even)

####################################################################################

# *Operator makes functions flexible

# *operator
# *args                => we can pass any number of arguments by using this parameter!!!

def total(a,b):
    return a+b

#(1,2,3,4,5,65)

def all_total(*args):    ######## * operator makes the args input elements as in tuple 
    total =0
    for num in args:
        total += num
    return total

print(all_total(1,2,3,4))  


########## *args with normal parameter

def multiply_nums(*args):
    multiply = 1
    for i in args:
       multiply *= i
    return multiply

print(multiply_nums(1,2,3))


##### *args with normal parameter

def multiply_nums(num, *args): ### we have to pass the normal argument compulsary !! *args is optional according to requirement 
    multiply = 1
    print(num)
    print(args)
    for i in args:
        multiply *= i
    return multiply

print(multiply_nums(2,2,3)) 

############################################################3


def multiply_nums(*args):
    multiply = 1
    for i in args:
       multiply *= i
    return multiply

nums = [1,2,3,4]
print(multiply_nums(nums))  ### output = it gives the list as it is by multiplying by 1

## TO Remove this constraint and unpack the list...

print(multiply_nums(*nums))  ## by putting *operator before nums variable !!


####################################################################################
# Kwargs (keyword argument)
# **kwargs (double star operator)

# kwargs as a parameter
def func(**kwargs):
    print(kwargs)
    print(type(kwargs))   ## It's a dictionary class type 

func(first_name = 'Praneet', last_name= 'Niranjan')

########################### It gives the output in a form of key value pair !!

def func(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} : {v}")

func(first_name = 'Praneet', last_name = 'Niranjan')
 
## Dictionary unpacking  

d = {'name': 'Praneet', 'age':23} 
func(d)


###################################################################################################################33

# funtions with all parameters
# very important to understand 

# PADK

# parameters
# args
# default parameters
# Kwargs

def func(name, *args, last_name = 'unkown', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

func('Praneet', 1,2,3, a=1, b=2)


####################################################################################################################
## example of kwargs argument:

def func(l,**kwargs):
   if kwargs.get('reverse_str')== True:
        return[name[::-1].title() for name in l]
   else:
        return [name.title() for name in l]

names = ['harshit','mohit']
print(func(names,reverse_str = True))


####################################################################################################################

# args vs kwargs:

def add(*args):
  # 1,2,3,4
  total =0
  for num in args:
      total += num
  return total

# print(add(1,2,3,4))

##################################
# kwargs - keyword arguments , **
def func(**kwargs):
    print(kwargs) # gather as dictionary
    print(type(kwargs))

func(name = 'harshit', age =24 )
# *args, **kwargs, normal parameter, default parameter 

## The order of arguments is : PAKD [parameter, *args, **kwargs, Default]

####################################################################################3333


# lambda expression (anonymous function)

def add(a,b):
    return a+b


add = lambda a,b : a+b 
print(add(2,3))

## Lambda functions have no name known as anonymous function and uses in (buitl in, map, reduce, filters ...etc)

## Example:
   
def is_even(a):
    return(a%2==0)  ## a%2==0 --> True, False

print(is_even(5))

### By using lambda expression
 
iseven2 = lambda a : a%2==0
print(iseven2(4))


def last_char(s):
    return s[-1]

last_char = lambda s : s[-1]
print(last_char('Praneet'))


# lambda with if, else
 
def func(s):
    return(len(s) > 5)
    

func = lambda s : len(s) > 5 

print(func('adfdjcn')) 


###########################################################################
# enumerate functon: we use enumerate funtion with for loop to track position of our 
# item in iterable

# How we can do this without enumerate function
names = ['abc','abcdef','Praneet']
# 0 --> 'abc'

pos = 0
for name in names:
    print(f"{pos} ----> {name}")
    pos += 1

# with enumerate function

for pos, name in enumerate(names):
    print(f"{pos} -----> {name}")



############################# Example for enumerate:

# Define a function that take two arguments:
# 1.) list containing string
# 2.) string that want to find in your list
# and this function will return the index of string in your list and 
# if string is not present then return -1

names = ['avd','amncn','Praneet']
def find_pos(l,target):
    for pos, name in enumerate(l):
        if(name==target):
           return pos
    return -1

print(find_pos(names,'Praneet'))  

######################################################################################

# map function

numbers = [1,2,3,4,5]

# By lambda function:

squares = list(map(lambda a:a**2, numbers))
print(squares)

# By using List Comprehension:

squares_new = [i**2 for i in numbers]
print(squares_new)


## By using the append method:

my_list = []
for num in numbers:
    my_list.append(square(num))

print(my_list)

##################################################################################
### filter function

def is_even(a):
    return a%2==0

numbers = [3,4,2,1,5,6,8,9,10]

evens = tuple(filter(lambda a: a%2==0, numbers))
print(list(evens)) 

new_evens = [i for i in numbers if i%2==0]
print(new_evens)

#####################################################################################

## iterator vs iterables

numbers = [1,2,3,4] # tuples, string -- iterables
squares = map(lambda a:a**2, numbers) # iterator

for i in numbers:
    print(i)


### This is how for loop works:

number_iter = iter(numbers)
print(next(number_iter))  #--> 1
print(next(number_iter))  #--> 2
print(next(number_iter))  #--> 3

###################################################################################################
# Zip function: by example

user_id = ['user1','user2','user3']
names = ['Praneet','Niranjan','PN']
last_names = ['anahcdd','njni','cdcndsc']

# ('user1', 'Praneet'), ('user2', 'Niranjan')...
print(list(zip(user_id, names, last_names))) # we can't change it to dict becoz dict are tuples with two argument

# example = [('a',1), ('b',2)]
# print(dict(example))


l1 = [1,3,5,7]
l2 = [2,4,6,8]

l = [(1,2),(3,4),(5,6),(7,8)]
# * operator with zip

l1, l2 = list(zip(*l)) # *operator with zip to unpack list or tuples
print(l1)
print(l2) 

new_list =[]
for pair in zip(l1,l2):
    new_list.append(max(pair))

print(new_list)



# define a function take any no of lists containing number
# [1,2,3], [4,5,6], [7,8,9]
# return average
# (1+4+7)/3 , (2,5,8)/3, (3,6,9)/3


def average_finder(*args):
    average =[]
    for pair in zip(*args):
        average.append(sum(pair)/len(pair))
    return average

print(average_finder([1,2,3],[4,5,6],[7,8,9]))

# OR funcn in one lines
average_finder = lambda *args: [sum(pair)/len(pair) for pair in zip(*args)]
#####################################################################################################

# any, all function

numbers1 = [2,4,6,8,10]
numbers2 = [1,2,3,4,5,6]

print(all([num%2 ==0 for num in numbers1])) ## Return True if all are true 

print(any([num%2 ==0 for num in numbers1])) ## Return True if any true occure
##################################################################################################

# any all function

def my_sum(*args):
    # args =()
    if all([(type(arg)== int or type(arg)==float) for arg in args]):
        total =0
        for num in args:
            total += num
        return total
    else:
        return "wrong input"

print(my_sum(1,2,3,4,8.9,'Praneet',['Niranjan']))


    
###########################################################################################################33


# advance sorted algorithm:

fruits = ['grapes','mango','apple']   ## Lists are mutable
# sort
# fruits.sort()
print(fruits)


fruits2 = ('grapes','mango','apple')
print(sorted(fruits))                  ## tuples are immuatble


fruits3 = {'grapes','mango','apple'}
print(sorted(fruits3))

guitars = [
     {'model': 'yamaha f310','price': 8400},
     {'model': 'faith naptune','price': 5000},
     {'model': 'faith apollo venus', 'price': 35000},
     {'model': 'taylor 814ce', 'price': 450000}
]

print(sorted(guitars, key = lambda d:d['price']))
print(sorted(guitars, key = lambda d:d['price'], reverse=True))  ## reverse the output means in increasing order 


####################################################################################################################

# doc strings : we use triple single quotes or triple double quotes for docstring !!

print(add._doc_)

# len, sum, max, min, sorted
print(len._doc_)
print(sum._doc_)

###################################################################################################################

## Pass function as argument:

# map
def square(a):
    return a**2

l = [1,2,3,4]
print(list(map(square,l)))

# made by lambda expression:

print(list(map(lambda a: a**2, l)))

## made our own function:

def my_map(func,l):
    new_list = []
    for item in l:
        new_list.append(func(item))
    return new_list


### by list comprehension:

def my_map(func,l):
    return [func(item) for item in l]   


print(my_map(lambda a: a**3, l))

#####################################################################################################

## Function returning functionn:   or closures or first class

def outer_func():
    def inner_func():
        print('inside inner func')
    return inner_func

var = outer_func()
var()   ## this will call the inner_func otherwise, we have to put parenthesis after inner_func() in return of outer_func()

## function returning function (closure) practice

def to_power(x): # x = 3
    def  calc_power(n): # n=2
         return n**x
    return calc_power

#Ex:
cube = to_power(3)
print(cube(2))

square = to_power(2)
print(square(4)) 


###################################################################################################

## Decorators - enhance the functionality of other functions
# @ use for decorator functions !!!

def decorator_function(any_function):
    def wrapper_function():
        print('this is awesome function')
        any_function()
    return wrapper_function


# this is awesome function

@decorator_function  # shortcut        now u can call the function func1() directly without any var variable below !!
def func1():
    print('this is function 1')

# this is awesome function

@decorator_function  # shortcut
def func2():
    print('this is function 2')

var = decorator_function(func1)
var() 
       

########################################################################################################
## To pass an argument in decorators functions !!


def decorator_function(any_function):
    def wrapper_function(*args, **kwargs):
        print('this is awesome function')
        return any_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def func(a):
    print(f'this is function with argument {a}')

func(7)        

@decorator_function
def add(a,b):
    return a+b

print(add(4,5))
####################################################################################

from functools import wraps
def decorator_function(any_function):
    @wraps(any_function)
    def wrapper_function(*args, **kwargs):
        """ this is wrapper function """
        print('this is awesome function')
        any_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def add(a,b):
    ''' this is add function '''
    return a+b

print(add._doc_)
print(add._name_)         


###########################################################################################3

## Decorators practice :


## question:
# output
# you are calling add function
# This function takes two numbers as parameters and return their sum
# 9


from functools import wraps
def print_function_data(function):
    @wraps(function)
    def wrapper_function(*args, **kwargs):
        print(f"You are calling {function._name_}")       
        print(f"{function._doc_}")
        any_function(*args, **kwargs)
    return wrapper

@decorator_function
def add(a,b):
    ''' this function takes two numbers as arguments and return their sum '''
    return a+b

print(add(4,5))

###################################################################################################

# generators
# generators are iterators

# iterator, iterable

l = [1,2,3]  # iterable

for i in l:
    print(i)

for num in map(lambda a : a**2, l):    # iterator
    print(num) 

####################################################################################################

# create your first generator with generator function
# 1.) generator function

# 10 , 1 to 10

def nums(n):
    for i in range(1,n+1):
        yield(i) 

print(nums(10)) 

########################################################################################
# create your first generator with generator function
# 1.) generator function

# 10 , 1 to 10

def nums(n):
    for i in range(1,n+1):
        yield(i) 

## yield is a keyword so you don't have to write i in parenthesis because it's not a function, i mean you can also write as 'yield i' instead of 'yield(i)'

print(nums(10))


# memory in generators are less consuming and more efficiently worked...
# memory (list) - [.................................]
# memory (gen) - (2)


## Create generator for even number: example ::
def nums(n):
    for i in range(1,n+1):
        if i%2==0:
            yield(i)
        else:
            continue    


for num in nums(20):    ## without for loop to print the generators will not generate numbers and print also!!!
    print(num)          ## That's how memory will be managed well !!




################################################################################
## Generator Comprehension : 

square = (i**2 for i in range(1,11))  # if instead of parenthesis square brackets are there then it will be list comprehension!!
print(square)

####################################################################################################
# list vs generator
# memory usage, time
# when to use list, when to use generator


t1 = time.time()
l = [i**2 for i in range(10000000)] # 10 million   ## 400 mb memory consume at one point of time
print(time.time() - t1)  ## print the time taken by list generator to generate numbers !!



g = (i**2 for i in range(10000000)) # 10 million   ## approx no memory consumed due to generators generate one element at one point of time!!

## if same time method used for above genrator it gives : 0.0 sec and in list : 4.93 sec approx !!

##################################################################################################################
## OOPS in python : 

# Objectives:
# What is class
# how to create an class
# What is INIT Method , constructor
# What are attributes , Instance variables
# How to create our object

class Person:
    def __init__(self,first_name,last_name,age):
        # instance variables
        print('init method // constructor get called')
        self.Person_first_name = first_name  ## Person_first_name is an instance variable name
        self.last_name = last_name
        self.age = age

p1 = Person('Praneet', 'Niranjan', 23) 
p2 = Person('Ppp', 'Nddd', 25) 

print(p1.Person_first_name)  ## Example of instance variable names
print(p2.first_name)

#########################################################################################
## instance methods
class Person:
     def __init__(self,first_name,last_name,age):
         self.first_name = first_name
         self.last_name = last_name
         self.age = age
     
     def full_name(self):
        return f"{self.first_name} {self.last_name}"


p1 = Person('Praneet','Niranjan', 25)
p1.full_name()   
print(Person.full_name(p1))

############################################################################################
## Change class variable
## How to print name space for objects
## What if we use self instead of class name for class variables


class Laptop:
      discount_percent = 10
      def __init__(self, brand, model_name, price):
      # instance variables
        self.brand = brand
        self.model_name= model_name
        self.price = price
        self.laptop_name = brand + ' ' + model_name

      def apply_discount(self):
          # self.price
          off_price = (Laptop.discount_percent/100)*self.price
          return (self.price - off_price)


laptop1 = Laptop('hp', 'au114tx', 63000)
laptop2 = Laptop('apple', 'macbook pro', 230000)
print(laptop1.apply_discount())         ### output : = 56700.0

## After discount percentage will be zero :
Laptop.discount_percent = 0 
print(laptop1.apply_discount())   ## output : = 63000
 
print(laptop1.__dict__)    ### output : = print All the instance variables
## {'brand': 'hp', 'model_name': 'au114tx', 'price': 63000, 'laptop_name': 'hp au114tx'}

## For Laptop 2 ex:
laptop2.discount_percent = 50
print(laptop2.__dict__)
print(laptop2.apply_discount())


###########################################################################################3
# class methods
# Difference between class methods and instance methods

class Person:
      count_instance = 0
      def __init__(self, first_name,last_name,age):
          Person.count_instance += 1
          self.first_name = first_name
          self.last_name = last_name
          self.age = age
      
      @classmethod
      def from_string(cls, string):
         first,last,age = string.split(',')
         return cls(first,last,age)



      @classmethod                        ## Class Method !!             
      def count_instances(cls):
          return f"You have created {cls.count_instance} of {cls.__name__} class" 

      def full_name(self):
          return f"{self.first_name} {self.last_name}"

      def is_above_18(self):
          return self.age > 18
#######################################################################################
     # Static method :
      @staticmethod
      def hello():
         print('hello, static method called')



p1 = Person('Praneet','Niranjan', 10)
p2 = Person('PT','NN', 24)
print(Person.count_instances())  ## We can access count_instances() by using object or instances 
print(p1.count_instance())


p3 = Person.from_string('Praneet,Niranjan,23')
print(p3.full_name())
  
Person.hello()
#########################################################################33
###  Encapsulation : Data and their functions are encapsulate in a class 
                     # Ex: instance variables and their instance methods !!

class Phone:
    def __init__(self, brand, model_name,price):
        self.brand = brand
        self.model_name = model_name
        self.price = price

    def make_a_call(self, phone_name):
        print(f"calling {phone_number} ...") 
   
    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def send_message(self):            ## Abstraction: user can send message
        pass  ## hello            

##############################################################################

## Abstraction : To hide complexities from user 

# Ex:
l = [1,3,5,2,7,8,9,1]   ## list class already defined in python
l.sort()                ## sorting can be done in many ways but we don't know the complexities behind it
print(l)                

## Note: The above example shows the abstraction and it can't be done without encapsulation !!!

#########################################################################################################333


## In Python everything is public !! unlike in other programming languages (private,public and protected) 
# _name = conversion of Private naming (underscore)
self._price = price  ## Indicate it's a private instance/method for devlopers 


# __name__  # dunder/magic methods



#############################################################################################
### Having problems solved them using getter, setter decorator

class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self._price = max(price,0)   ## To avoid negative values
    #   self.complete_specification = f"{self.brand} {self.model_name} and price is {self._price}" 


    @property                                         # it will help to call as a variable not as a function 
    def complete_specification(self):                 # it will print or give updated values instead of initial values as in above init method
        return f"{self.brand} {self.model_name} and price is {self._price}" 


    @property
    def price(self):
      return self._price

    @price.setter
    def price(self,new_price):
        self._price = max(new_price,0)  
    
    ## Note : still you can set negative value using _price but now atleast we have a better way to set values


    def make_a_call(self, phone_number):
        print(f"calling {phone_number}...")

    def full_name(self):
        return f"{self.brand} {self.model_name}"

phone1 = Phone('Nokia', '1100', 1000)
phone1._price = 500
print(phone1.price)               # Due to making of @property function above  
print(phone1.complete_specification)    # Due to property keyword !!


 
#####################################################################################################
### Inheritance !!

class Phone:    ## Base class / Parent class
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name= model_name
        self._price = max(price,0)   ## To avoid negative values
    #   self.complete_specification = f"{self.brand} {self.model_name} and price is {self._price}" 

    def make_a_call(self, phone_number):
        print(f"calling {phone_number}...")

    def full_name(self):
        return f"{self.brand} {self.model_name}"


class Smartphone(Phone): # derived / child class
    def __init__(self, brand,model_name,price, ram, internal_memory,rear_camera):
        # two ways
      #  Phone.__init__(self,brand,model_name,price)  # uncommon way
       
        super().__init__(brand,model_name,price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

 
phone = Phone('nokia','1100',1000)
smartphone = Smartphone('onePlus','5', 30000, '6 GB', '64 GB', '20 MP')
print(phone.full_name())
print(smartphone.full_name() + "and price is {smartphone._price}") 

#################################################################################################################

## Multilevel inheritance : Yes, we can derived one more class from another class !!

## The above code of class Phone as it is and add one more class called as : Smartphone2 

class Smartphone2(Phone): # derived / child class
    def __init__(self, brand,model_name,price, ram, internal_memory,rear_camera):
        # two ways
      #  Phone.__init__(self,brand,model_name,price)  # uncommon way
       
        super().__init__(brand,model_name,price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

    def full_name(self):        ## Method overriding  
        return f"{self.brand} {self.model_name} and price is {self.price}"

class FlagshipPhone(Smartphone2):         # Derived / Child class      
     def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera,front_camera):
         super().__init__(brand,model_name,price,ram,internal_memory,rear_camera)
         self.front_camera = front_camera




oneplus = FlagshipPhone('oneplus','5', 30000, '6 GB', '64 GB', '20 MP','16 MP')
print(oneplus.full_name())    ## overrided method will be called due to method resolution order !!

sm = Smartphone2('oneplus', '200', 50000,'20GB','64GB', '5MPX')
print(sm.full_name() + " " +  f"and price is {sm._price}")

##############################################################################################
# Method Resolution Order : - Priority given to first parent class like : In above class FlagshipPhone class call full_name method of SmartPhone class

##############################################################################################
# isinstance: to check whether the selected object is an instance of class or not 

print(isinstance(oneplus,FlagshipPhone))   ## Return True
print(isinstance(oneplus,Smartphone2))     ## Return True 
print(isinstance(oneplus,Phone))           ## Return True

##############################################################################################################

# issubclass: To check class is subclass of another class or not
# issubclass(subclass, class)

print(issubclass(Smartphone,Phone))       ## Return True

##############################################################################################################

## Multiple inheritance : Generally we don't use multiple inheritance in python

# Multiple Inheritance

class A:
     
     def class_a_method(self):
         return 'I\'m just a class A method'
     
     def hello(self):
         return 'hello from class A'

class B:
     
     def class_b_method(self):
         return 'I\m just a class B method'

     def hello(self):
         return 'hello from class B' 

class c(A,B):
     pass

instance_c = c()
print(instance_c.class_a_method())
print(instance_c.class_b_method())  
print(help(c))    # To check the method resolution
print(c.mro)       
print(c.__mro__)

#####################################################################################################
## Operatoor overloading :..

def __add__(self, other):
    return self.price +other.price


ph = Phone('nokia', 500, 433)
ph1 = Phone('oneplus', 600, 5444)
print(ph + ph1)                    # It will add both the objects by using above default function(add)

## We can do multiplication, subtraction, addition, division ..etc like that above !!!

########################################################################################################
# Polymorphism ka example operator overloading hai like: ek operator ka multiple use 

a = 7 + 8
print(a)

b = 'ffk' + 'abcd'
print(b)

###########################################################################################################

# str , repr

def __str__(self):
    return f'{self.brand} {self.model} and price is {self.price}'

def __repr__(self):
    return f'Phone(\'{self.brand}\', \'{self.model}\', {self.price})'

#####################################################################################################################
# Raise Error: 
def add(a,b):
    if (type(a) is int) and (type(b) is int):
        return a+b
    raise TypeError('OOPs you are passing wrong data type to function') 

print(add('2','3'))

#####################################################################################################################3
class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        return 'this is animal sound'


class Dog(Animal):
    def __init__(self,name,breed):
         super().__init__(name)
         self.breed = breed


class Cat(Animal):
     def __init__(self,name,breed):
         super().__init__(name)
         self.breed = breed

doggy = Dog('boony', 'pug')
print(doggy.sound())
#################################################################################################3333
## Exception handling
## try except else finally

while True:
    try:
        age = int(input('Enter your age: ')) # seven # 7
        break
    except ValueError:
        print('invalid input....')
    except:
        print('unexcepted error....')    
    else:
        print(f'the age is {age}')
        break
    finally:
        print('This function will always run either error occured or not !!')

# if age< 18:
#     print('you can\'t play this game.')
# else:
#     print('you can play this game.')

#####################################################################################################
# python custom exceptions
# Q- why custom exceptions?
# A - To increase the readability of code.

# example
class NameTooshortError(valueError):
      pass

def validate(name):
    if len(name) < 8:
       raise NameTooshortError('name is too short')

username = input('Enter your name:')
validate(username)
print(f'hello {username}')

#############################################################################################
# Python debugging :

import pdb  # to import the debugging class

pdb.set_trace()   ## To set from we want to debug the code 

name = input('Please type your name:')
age = input('Please type your age: ')
print(f'hello {name} your age is {age}')
age2 = int(age) + 5
print(f'{name} you will be {age2} in next five years')

# L(l)  : To check the pointer
# n     : To execute the pointed line  
# c     : To execute the whole code
# q     : quit the pdb

###################################################################################################s













