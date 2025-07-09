"""
Set are similar to list but are unordered and cannot create duplicates. Use curly brackets

"""
my_set = {1,2,3,4,5,6,7,2,1,2,3}
print(my_set)
print(len(my_set))
print(type(my_set))

for i in my_set:
    print(i)

#remove
my_set.discard(3)
print(my_set)

#remove all
my_set.clear()
print(my_set)

# Add
my_set.add(10)
print(my_set)

my_set.update([7,8])
print(my_set)