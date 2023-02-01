# Lists: ordered, mutable, allows duplicate elements

mylist = ["bananana", "ch-cherry", "aaaaple"]
print(mylist)

mylist2 = list()
print(mylist2)

item = mylist.pop()
print(item)
print(mylist)


# mylist.remove("ch-cherry")
# mylist.clear()

numlist = [4,3,2,-1,-10,848]
# numlist.sort()
new_numlist = sorted(numlist)
print(numlist)
print(new_numlist)


# concat lists with '+'
multilist = [0,1]*10
print(multilist)
sublist = multilist[1:4]
print(sublist)
# sublist = [2,0,2]
# print(sublist)
# print(multilist)

# how to create a different copy of a list 
# (in list2=list1, both vars reffere to the same list)

list_cpy = mylist.copy()
list_cpy = list(mylist)
list_cpy = mylist[:]

nums = [1, 2, 3, 4, 5]
nums_squared = [i*i for i in nums]
print(nums)
print(nums_squared)