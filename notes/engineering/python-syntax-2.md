## 1.lambda

lambda 是简单函数的简化写法，常见的是这样

```python
lambda x: x**2		# 等价于 def func(x): return x**2
```

不难看出，lambda主要是为了便于开发者写一些不需要复用的简单函数，也常常被用在库函数的参数中，例如sort()和sorted()函数，都可以传入function类型的参数用于自定义排序规则，在这里就可以使用lambda来简化开发

```python
person=[
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 40}]
sorted(person, key=lambda p: p["age"])	# 按年龄升序排序,降序需要使用sorted函数的reverse参数，改为True
```

lambda的简单用法大概就是这样了，复杂用法主要是与其他操作一起使用。



## 2.map/filter

map和filter两个函数是较为进阶的函数，可以用来代替推导式，不过一般在开发中推导式还是更加具有可读性的，所以这里的重点放在能够看懂使用这两个函数的场景

```python
list(map(str, nums))	# 将nums中所有元素转为字符串类型
list(filter(lambda x: x >= 2, nums))	# 只选择nums中大于等于2的元素
```

map和filter主要是用于对各种可迭代对象进行批量操作，自身返回的也是一个迭代器，所以map和filter可以进行链式处理



## 3.解包

解包是python中的重要操作，无论是赋值还是传参中都被广泛使用

```python
first, *middle, last = [1, 2, 3, 4]		# first=1, middle=[2, 3], last=4
# 将字典解包成为关键字参数，定义def func(**kwargs)→任何 key 都行，全部打包进 kwargs 字典;调用 func(**some_dict)→key必须和函数参数名一致，否则报错
def func(**kwargs)						
def wrapper(*args, **kwargs)			# 装饰器中使用用来接收所有类型所有个数的参数
```

解包本身并不复杂，*对于列表是将其变成零散的变量，对于字典是拆成零散的键，值便被丢弃了；**对于字典是将其变成关键字参数，形如port=8080。

解包的用处十分多样，在这里难以一一列举，但是在使用中肯定会强化对其的记忆的，此处不多赘述。



## 4.enumerate和zip

enumerate和zip也是两个较为常见的函数，尤其是enumerate，当我们在遍历中同时需要序号和元素的时候就会使用到

```python
for index, value in enumerate(list)
```

用形如这样的方法，我们可以从各种可迭代对象中获取其序号和值，例如：

```python
  # 字符串
  list(enumerate("abc"))         # [(0, 'a'), (1, 'b'), (2, 'c')]
  # 元组
  list(enumerate((10, 20, 30)))  # [(0, 10), (1, 20), (2, 30)]
  # range
  list(enumerate(range(3)))      # [(0, 0), (1, 1), (2, 2)]
  # 文件对象
  with open("data.txt") as f:
      for i, line in enumerate(f, start=1):
  # 字典
  d = {"a": 1, "b": 2, "c": 3}
  for i, key in enumerate(d):
      print(f"{i}: {key}")        # 只拿到 key
  # 0: a
  # 1: b
  # 2: c
  for i, (k, v) in enumerate(d.items()):
      print(f"{i}: {k}->{v}")
  # 0: a->1
  # 1: b->2
  # 2: c->3
  d = {"a": 1, "b": 2, "c": 3}
```

可以看出来，enumerate会将所有可以计数迭代的对象的序号取出，组成一个元组。

而zip函数可以用来同时遍历多个可迭代对象

```python
for l1, l2 in zip(list1, list2)
```



## 5.装饰器

装饰器与Java中的注解有些类似，都是在函数上加上一个@开头的东西，不过python中的装饰器也是函数，一般的定义如下

```python
def decorate(func):
    def wrapper(*args, **kwargs):
        # pre-process
        result = func(*args, **kwargs)
        # post-process
        return result
    return wrapper

@decorate  
def func()
```

装饰器中嵌套一个wrapper函数，在这个函数里面对被装饰函数进行前操作和后操作，也可以对被装饰函数的结果进行修改，使用时只需要在被修饰的函数上添加装饰器即可使用。

## 6.with open 文件操作

对于文件资源的操作我们一般使用with open来进行，with open会自动管理资源的释放，不需要显式close

```python
with open("file_dir", "operate_mode", encoding="") as f:
```

这样的语句之下便可以使用f进行各种文件操作，常用常见的为读写和大文件逐行操作

```python 
with open("file_dir", "r", encoding="") as f:
    context = f.read()
    
with open("file_dir", "w", encoding="") as f:		# 覆盖写，每次写之前清空文件
    f.write(something)
    
with open("file_dir", "a", encoding="") as f:		# 追加写，写入时在文件末尾追加
    
with open("file_dir", "operate_mode", encoding="") as f:
    for line in f:
        process(line)								# 对每行进行操作，不一次性加载qu'a
```

