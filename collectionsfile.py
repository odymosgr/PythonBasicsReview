# collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter
a = "aaaabbbccdef"
my_counter = Counter(a)
print(my_counter)  # .keys() .values() .most_common(#how_many)
print(list(my_counter.elements()))


from collections import namedtuple
Point = namedtuple('Point',  'x,y')
pt = Point(1,-4)
print(pt.x, pt.y)



from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['b'] = 3
ordered_dict['c'] = 5
ordered_dict['d'] = 2
ordered_dict['a'] = 1
print(ordered_dict)




from collections import defaultdict
d = defaultdict(int)
d['b'] = 2
d['a'] = 'b'
print(d)
print(d['null'])



from collections import deque
d = deque()
d.append(1)
d.append(2)
d.appendleft(0)
print(d)
d.extendleft([4,5,6])
print(d)
print(d.popleft())
print(d)
d.rotate(1)
print(d)