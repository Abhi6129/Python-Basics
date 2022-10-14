#print("hello py")


#Indentation
#if 5>2:
 #  print("Five is gretater than two!")


#cooments
""" this is a multi line comment
x=5
y="Hello world"
print(x)
print(y)
"""
#This is a single line comment

"""
#Variables
x=4   #x is of type int
x="Sally"  #x is of type str
print(x)

#casting
x=str(3)   # x will be '3'
y=int(3)   # y will be 3
z=float(3) # z will be 3.0
print(x)
print(y)
print(z)


#Type() Function
a=10     #<class 'int'>
b="mcd"  #<class 'str'>
print(type(a))
print(type(b))


#Case-Sensitive-the variable names are case sensitive
a=5
A="bsdk"
print(a)
print(A)

#Variables can have short name or descriptive names 
name must start with letter or underscore character
cannot strt with a number
can only contain alpha numeric charcaters and underscore
variable names are case sensitive

myvar="Jphn"
my_var="John"
myVar="John"
MYVAR="JOHN"
myvar2="John"

naming styles
camel case= myVariableName[starting letter of first word is small and remaing capital]
pascal case= MyVariableName[starting letter of each word is capital]
snake case= my_variable_name[each word is seperated by an underscore]


#Many values to multiple variables
x,y,z="Orange","banana","Cherry"
print(x)
print(y)
print(z)


#one value to multiple variables
x=y=z="mcd"
print(x)
print(y)
print(z)

#unpacking a collection
fruits = ["apple","cherry","lime"]#Tuples
x,y,z = fruits#assigning values in list to variables
print(x)
print(y)
print(z)


#Output Variables
x="Py is cool"
print(x)

a="py"
b="is"
c="cool"
print(a,b,c)#py is cool is printed with spaces
print(a+b+c)#pyiscool is printed with no spaces

#for numbers the + character works as a mathematical operator
v=20
n=10
print(v+n)

#if we try to combine a string and a number with + operator we get an error


#we are creating a variable outside of a function and using it inside of the function
x="aws"                     #global var
def myfunc():               #function
    print("cloud means " +x) #calling the global var

myfunc()                     #calling the function

#Data Types
#str,int,float,complex,list,tuple,range,dict,set,frozenset,bool,bytes,bytearray,memoryview,NoneType
a="hw" #string
b=20 #int
c=20.5 #float
d=1j #complex
e=["a","b","c"] #list
f=("a","b","c") #tuple
g=range(6)
h={"n":"m","o":"p"} #dict
i={"a","b","c"} #set
j=frozenset({"a","b","c"})
k=True #bool
l=b'hello' #bytes
m=bytearray(5)
n=memoryview(bytes(5))
o=None
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)
print(l)
print(m)
print(n)
print(o)

#there are 3 numeric types :int,float,complex
x=1    #int
y=2.8  #float
z=1j   #complex
print(type(x))
print(type(y))
print(type(z))

#type conversion

#int to float
a=float(x)
#float to int
b=int(y)
#int to complex
c=complex(x)

print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

#Random number
import random
print(random.randrange(1,10))

#Python casting
#int
a=int(1)
b=int(2.9)
c=int("4")
#float
d=float(1)
e=float(2.9)
f=float("6")
g=float("6.1")
#str
h=str("s1")
i=str(2)
j=str(3.0)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
"""
#strings
#multiline
a="""lorem ipsum"""
print(a)
#srtring as array
b="hello world"
print(b[0])
#string looping
for x in "banana":
    print(x)


