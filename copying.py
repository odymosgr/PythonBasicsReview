org = 5
cpy = org
cpy = 6

print(org)
print(cpy)




org = list(range(5))
cpy = org
cpy[0] = -10

print(org)
print(cpy)




import copy

org = list(range(5))
cpy = copy.copy(org)
cpy[0] = -10

print(org)
print(cpy)




# shallow copy, 1lvl deep
org = [[0,1,2,3,4], [5,6,7,8,9]]
cpy = copy.copy(org)
cpy[0][0] = -10
cpy.append([10,11])

print(org)
print(cpy)




# deep copy
org = [[0,1,2,3,4], [5,6,7,8,9]]
cpy = copy.deepcopy(org)
cpy[0][0] = -10
cpy.append([10,11])

print(org)
print(cpy)





print('---------- classes -----------')

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Company:
  def __init__(self, boss, eployee):
    self.boss = boss
    self.employee = eployee

p1 = Person('Alex', 27)
p2 = copy.copy(p1)

p2.age = 38

print(p1.age)
print(p2.age)

p3 = Person('Joe', 21)
company = Company(p1, p3)
# company_clone = copy.copy(company)
company_clone = copy.deepcopy(company)
company_clone.boss.age = 56

print(company_clone.boss.age)
print(company.boss.age)























