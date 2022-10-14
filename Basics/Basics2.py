"""
print("hello")
#here are the comments

a=3
#python has no return type
print(a)

Str = 'hello world'
print(str)


b, c, d = 5, 5.4, "great"
print(b)
print(c)
print(d)

print("{} {}".format("Value is", b))

print(type(b))
print(type(c))

#list
values =[1,2,"rahul",4,4.5]
#list is  a data type that alows multiple values and can be different data types
print(values[0])  #1
print(values[-1])
print(values[1:3])
values.insert(3,"akash")
print(values)
values.append("ens")
print(values)

values[2]="RahuL"
print(values)
del values[0]
print(values)


#tuple
#same as list data type but immutable
val=(1,2,"akash",4)
print(val[1])



#dictionary
dic = {"a":2 ,4:"abc" , "c":"hello"}
print(dic[4])
print(dic["c"])

#dic creation
dict={}
dict["firstname"] =["Akash"]
dict["Lastname"] = ["Patra"]
print(dict)


#loops
greet="good morning"
if greet=="morning":
    print("condtn matchjeds")
else:
    print("dont match")
print("code cmplete")

#for loop
obj=[2,3,5,7]
for i in obj:
    print(i*2)

#sum of first 5 natueral no 1+2+3+4+5=15
summation = 0
for j in range(1,6):
    summation=summation+j
print(summation)

#range(i,j)  => i to j-1

for k in range(1,10,2):
    print(k)
print("**********************************")
for m in range(0,10,2):
    print(m)

#while loops
it=10
while it>1:
    if it==9:
        it=it-1
        continue
    if it==3:
        break
    print(it)

    it=it-1



#functions


def GreetMe(name):
    print("good morning"+name)

def AddIntegers(a,b):
    print(a+b)

GreetMe("Rahul Shetty")
AddIntegers(2,3)
"""

