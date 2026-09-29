# Question 1
# You have these 5 cities:
# London, Paris, Tokyo, Delhi, Sydney

cities=['London', 'Paris', 'Tokyo', 'Delhi', 'Sydney']
print(cities)

# Question 2 — Thinking # You have this list:
# cities = ['London', 'Paris', 'Tokyo', 'Delhi', 'Sydney']
# Task: Print only Tokyo.

cities = ['London', 'Paris', 'Tokyo', 'Delhi', 'Sydney'] #cities is a variable that stores a list of five cities.
print[2]#shows error
print(2)#shows error
print(cities[2]) 
# Lists use zero-based indexing, so index 2 refers to the third element,
# which is Tokyo. Therefore, cities[2] returns Tokyo.

#Practice — Question 3
# cities = ['London', 'Paris', 'Tokyo', 'Delhi', 'Sydney']
# Task: 
# Print Delhi using negative indexing.

print(cities[-2])#negative indexing doesnt contain 0 index number always starts from -1

# Question 6
# cities = ['London', 'Paris', 'Tokyo', 'Delhi', 'Sydney']
# Task: Change Paris to Berlin.

cities[1]='Berlin'# variable name [list index no]='value you want to replace'
print(cities)

#Question 7 — Thinking
# cities = ['London', 'Paris', 'Tokyo', 'Delhi', 'Sydney']
# Task:
# Change Sydney to Melbourne without using its positive index.

cities[-1]='Melbourne'# accessing the last valueof the list by 
#using negative index from the list and replacing it with new value.
print(cities)

#uestion 8
# cities = ['London', 'Paris', 'Tokyo', 'Delhi', 'Sydney']
# Task: Change Paris to Berlin, but this time use negative indexing.

