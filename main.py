from collections import Counter

# 创建一个Counter对象
c = Counter(['a', 'b', 'a', 'c', 'b', 'a'])

# 统计元素的出现次数
print(c)  # 输出: Counter({'a': 3, 'b': 2, 'c': 1})

# 访问元素的出现次数
print(c['a'])  # 输出: 3
print(c['d'])  # 输出: 0

from collections import deque

# 创建一个deque对象
d = deque([1, 2, 3])

# 在右端添加元素
d.append(4)
print(d)  # 输出: deque([1, 2, 3, 4])

# 在左端添加元素
d.appendleft(0)
print(d)  # 输出: deque([0, 1, 2, 3, 4])

# 从右端删除元素
d.pop()
print(d)  # 输出: deque([0, 1, 2, 3])

# 从左端删除元素
d.popleft()
print(d)  # 输出: deque([1, 2, 3])

from collections import namedtuple

# 创建一个namedtuple类
Point = namedtuple('Point', ['x', 'y'])

# 创建一个Point对象
p = Point(1, 2)

# 访问字段值
print(p.x)  # 输出: 1
print(p.y)  # 输出: 2

from collections import defaultdict

# 创建一个默认值为0的defaultdict
d = defaultdict(int)

# 访问不存在的键，返回默认值0，并将该键添加到字典中
print(d['a'])  # 输出: 0
