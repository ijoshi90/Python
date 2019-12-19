"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 19-12-2019 at 11:07
"""

def to_upper_case(s):
    return str(s).upper()

def print_iterator(it):
    for x in it:
        print(x, end=' ')
    print('')  # for new line

#print(to_upper_case("akshay"))

#print_iterator("joshi")

# map() with string
map_iterator = map(to_upper_case, 'abc')
print(type(map_iterator))
print_iterator(map_iterator)

# Map iterator with tuple
map_iterator = map(to_upper_case, (1, "ab", "xyz"))
print_iterator(map_iterator)

# Map with list
map_iterator = map(to_upper_case, [1, 2, "Aksh"])
print_iterator(map_iterator)

# Converting map to list, tuple or set
map_iterator = map(to_upper_case, ['a,b', 'b', 'c'])
my_list = list(map_iterator)
print (type(my_list))
print(my_list)

map_iterator = map(to_upper_case, ['a', 'b', 'c'])
my_set = set(map_iterator)
print(type(my_set))
print(my_set)

map_iterator = map(to_upper_case, ['a', 'b', 'c'])
my_tuple = tuple(map_iterator)
print(type(my_tuple))
print(my_tuple)

# Map with
list_numbers = [1, 2, 3, 4]
mapite = map(lambda x: x * 2, list_numbers)
print(type(mapite))
for i in mapite:
    print(i)

# Map with multiple arguments
list_numbers = [1, 2, 3, 4]
tuple_numbers = (5, 6, 7, 8)

mapitnow = map(lambda x,y : x * y, list_numbers, tuple_numbers)
for each in mapitnow:
    print("From multiple arguments in lambda : {}".format(each))