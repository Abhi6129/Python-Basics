"""
lists
used to store multiple items in a single var.
Lista are created using Square Brackets  " [] "
"""
list=['aplle','banana','cherry']
print(list)
"""
list items are:
ordered ,changeable & allow duplicate values
items are indexed
index starts from [0]

Ordered
as lists are ordered so the items have a defined order and the order will not change
so if we add a new item to the list the item will be placed at the end of the list


Changeable
lists are changeable i.e we can change,add & remove items after a list is created

Duplicates
as lists are indexed so it can have items with same value

#ex:
list2=['apple','banaan','cherry','apple','cherry']#repeated values
print(list2)

#list Length
#to determine the no, of items in alist we use "len()"   Function
print(len(list2))

#list Items
#list items can be of any data type
list3=['apple','banana','cherry']#Strings
list4=[1,5,3,4]#int
list5=[True,False,True]#boolean
print(list3)
print(list4)
print(list5)
#list can have different data types
list6=['abc',35,True,69,'fcuk']#mixture of data types
print(list6)


#type()
#from Pythons Persepective Lists are defined as objects with data type 'list'
#<class 'list'>
#ex:
mylist=['apple','banana','cherry']
print(type(mylist))   #output:-<class 'list'>

#list() constructor
#it is possible to use "list()" constructor when creating a new list
thislist = list(("apple","banana","cherry"))
print(thislist)
#output=['apple','banana','cherry']
"""

"""
Python Collections [Arrays]
there are 4 collection data types 
1.List
2.Tuple
3.Set
4.Dictionary

list can be ordered and changeable & allowss duplicate members
Tuple is ordered and unchangeable & allows duplicate members
set is Unchangableand unindexed and no duplicate members but we can add/remove items
dictionary is unordered and no duplicate members but changeable
"""
#Accesing items from list
#we can access by index no.
thislist=['apple','banana','cherry','asdf','ghjk','mnbv','poil']
print(thislist[2])

#negative indexing
#in this we start counting from end
#-1 refers to lat item , -2 refers to second last item
print(thislist[-2])

#Range of Indexes
#we can specify a new range of indexes
print(thislist[:6])#start to end
print(thislist[2:])#2 to end

#range of indexes works the same for negative indexes as well
# checking the items
if 'santra' in thislist:
    print("yes, 'santra' is in the list")
else:
    print("invalid")
#inserting
thislist[0]="santra"
print(thislist)

thislist[1:4]=['apple','gendu','mali']
print(thislist)
#inserting without replacing existing values
thislist.insert(2,"watermelon")
print(thislist)
print(len(thislist))

