# *args **kwargs
# arg decomposition

print('2 x 7 = ', 2*7)
print('2^10 = ', 2**10)

# lists, tuples, strings
zeros = (0, 1) * 10
print(zeros)
print('Test_'*10)

first, *middle, last = zeros
print(first)
print(middle)
print(last)


my_tuple = (1,2,3)
my_list = [4,5,6]
my_set = {7, 8, 9}

new_list = [*my_tuple, *my_list, *my_set]
print(new_list)

d1 = {'a':1, 'b':2}
d2 = {'c':3, 'c':4}
dnew = {**d1, **d2}
print(dnew)