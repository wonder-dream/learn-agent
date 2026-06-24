# 推导式

## 1.列表推导式

用于快速生成列表及其内容，常见格式如下

```python
[x for x in something if something]
```

此处的 x 可以是各种形式，可以后缀各种函数操作，并且和后续 for 后面的 x 不需要是一样的格式，可以是

```python
[x.upper() for x in texts if not x.isdigit()]
```

推导式也可以使用多个

```python
[(x ** y) for x in range(10) for y in range(0,10,2)]
```

也可以嵌套(此处 y 只起到计数用)

```python
[[x for x in range(10)] for y in range(10)]
```

## 2.字典推导式

与列表推导式相似的，用于快速生成字典，常见格式如下

```python
{k: v for k, v in d.items()}
{k: v for k in something for v in something}
```

注意事项也与列表推导式大差不差，此处不再赘述。值得注意的是，列表推导式和字典推导式的嵌套使用是一个重难点，形如

```python
[{"key01": value01, "key02": value02} for value01 in something for value02 in something]
```

初次理解会稍微难一些，这也是语法糖的一大缺点，但是使用得当可以节省时间

## 3.集合推导式

大致与字典推导式相似，不过可以理解为只有 key 没有 value

```python
{x for x in something}
```

不重复的列表，或者没有 value 的字典



# 列表操作

## 1.切片

切片是python列表常见的简化操作，可以用简洁的方式做到一些需要遍历的事情，标准写法为：

```python
lst_part = lst[start:end:step]
```

其中 start 和 end 可为范围内的正负值，正值就是正常序号，负值为倒数，例如 -1 为倒数第一个也就是最后一个，在 python 中表示范围取值的绝大部分都是前闭后开区间。

step 是步长，也就是取当前元素后下一个元素在哪里取，默认为 1，也就是依次取出，设置为 >1 的值时，例如 2，就是每两个取一个，也就是跨一个取值。

切片还可以用来做切片赋值

```python
lst = [1, 2, 3, 4]
lst[1:3] = [9, 9]
lst = [1, 9, 9, 4]
```

## 2.增删改查

列表常用的操作就是增删改查，但是有多种方式的增删改查

```python
lst = []

# 1.append 添加元素
lst.append(1)		# [1]
lst.append([1])		# [[1]]

# 2.extend 添加元素
lst.extend(1)		# [1]
lst.extend([1, 2])	# [1, 2]

# 3.insert 插入元素
lst = [1, 2, 3, 4]
lst.insert(1, 5)	# [1, 5, 2, 3, 4]

# 4.pop 取出并删除元素，默认删除最后一个元素
lst = [1, 2, 3, 4]
lst.pop()			# [1, 2, 3]
lst.pop(1)			# [1, 3, 4]

# 5.remove 删除第一个取值匹配的元素
lst = [1, 2, 2, 4]
lst.remove(2)		# [1, 2, 4]

# 6. del lst[i] 按索引删除
lst = [1, 2, 3, 4]
del lst[0]			# [2, 3, 4]
del lst[:]			# []
del lst				# 列表对象被删除

# 7. clear 清空列表
lst = [1, 2, 3, 4]
lst.clear()			# []

# 8. x in lst x 是否在 lst 中
lst = [1, 2, 3, 4]
1 in lst			# True
0 in lst			# False

# 9. count 元素出现几次
lst = [1, 2, 3, 4, 4]
lst.count(1)		# 1
lst.count(4)		# 2

# 10.index 元素第一次出现的索引
lst = [1, 2, 3, 4, 4]
lst.index(4)		# 3

# 11.sum/max/min
lst = [1, 2, 3, 4]
sum(lst)			# 10
max(lst)			# 4
min(lst)			# 1

# 12.any/all
lst = [1, 2, False, 4]
any(lst)			# True
all(lst)			# False

# 13.enumerate(list) 同时取索引和值
lst = ["Bob", "Alice", "Mark"]
for index, value in enumerate(lst):
    print(index, value)					# 0 Bob    1 Alice   2 Mark
    
# 14.sorted(list)/list.sort()
# sorted(list) 返回新的排序后的列表，不改变原列表
lst = [2, 1, 3]
lst_sorted = sorted(lst)
print(lst)					# [2, 1, 3]
print(lst_sorted)			# [1, 2, 3]

# list.sort() 在原列表处排序，不返回新列表
lst = [2, 1, 3]
lst_sorted = sorted(lst)
print(lst)					# [1, 2, 3]
print(lst_sorted)			# None
```

# 字典操作

## 1.CRUD

```python
# 1.get 安全取值，不改变字典
d.get(k)		# 存在返回value，不存在返回None
d.get(k, 0)		# 存在返回value，不存在返回0

# 2.del 删除键值对
del d[k]

# 3.同时遍历键值
for k, v in d.items()

# 4.遍历key
for k in d.keys()

# 4.遍历value
for v in d.values()

# 5.合并字典
d1 | d2				# 重复 key 右边 value 覆盖左边

# 6.update
d.update(d2)		# 把 d2 批量更新进来，原地修改

# 7.pop
d.pop(k, default)	# 取出并删除，不存在则返回默认值

# 8.setdefault
d.setdefault(k, default) # key不存在就设置默认值，注意和get不同，这个设置会改变字典

# 9.copy 浅拷贝
d.copy()			# 生成一个新字典，不影响原字典

# 10.zip拼接列表成为字典
dict(zip(keys, vals))	# 合并成key: value 

# 11.字典解包
**d 				# 用于传参或者合并，传参需要key和形参名称一样，合并 {**d1, **d2}
```

