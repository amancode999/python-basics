# # what is a list ?
# array/list is a collection where it stores multiple values or elements at one place.
#for example:

numbers=[10,20,30,40]# these num are stored in variable named as numbers.
#1.how to call out the single element ?
#answer is by typing its index number 
print(numbers[0])# 0 is index no. of 10.
print(numbers[1])
print(numbers[2])
print(numbers[3])

#2.how to change its element from one to another.

product=['mouse','keyboard','monitor','printer']

product[3]='cpu'
print(product)

#3.how to add in list ?

#syntax :- variable name.append(what to add ?)it will add auto in the end by default.
# for example:-
fruits=['orange','apple','watermelon']
fruits.append('kiwi')
fruits

#4.how to add some element
# at particular position ?

#will use insert function.

fruits.insert(1,'banana')
fruits

#5. how to remove ?

fruits.remove('watermelon')
fruits

#from index delete

fruits.pop(2)
fruits

#6. sorting from ascending to descending
#variable name.sort()

fruits.sort()
print(fruits)

# 7.reverse as name suggest will reverse the output

fruits.reverse()
print(fruits)

n=[1,2,3,4]
n.reverse()
print(n)

#count()
numbers = [10, 20, 10, 30, 10]

print(numbers.count(10))

#indexing
fruits = ["Apple", "Mango", "Banana", "Orange"]

print(fruits.index("Banana"))

#in 

print('Mango' in fruits)
print('kiwi' in fruits)

#slicing
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])

#list + numbers + if

nos= [5, 15, 25, 35]

for no in nos:
    if no >20:
        print(no)