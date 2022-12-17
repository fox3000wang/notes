# Numpy

> NumPy 是一个 Python 的科学计算库。它包含了一个强大的 N 维数组对象，可以帮助用户在 Python 中进行高效的数值计算。NumPy 数组可以使用各种数据类型，包括浮点数和复数，并提供了许多有用的数学函数和线性代数运算，这些函数可以直接作用于数组上。使用 NumPy，用户可以在 Python 中处理大型数据集，执行复杂的计算，并进行高级数据分析。

> 数据分析师在学习 NumPy 时，需要掌握一些基础的 NumPy 操作，如数组创建、索引和切片、数学运算和线性代数运算等。此外，还应该掌握一些高级的 NumPy 特性，如统计分析、随机数生成和矩阵分解等。在实际工作中，数据分析师可能会需要处理大量数据，所以还需要掌握一些高效的 NumPy 操作，如广播和矢量化计算、内存映射和数据处理管道等。总之，数据分析师要掌握 NumPy 的基本操作和高级特性，并能运用 NumPy 的高效特性来处理大量数据。

## 官方文档

https://numpy.org/doc/stable/

## 安装

```shell
# Best practice, use an environment rather than install in the base env
conda create -n my-env
conda activate my-env
# If you want to install from conda-forge
conda config --env --add channels conda-forge
# The actual install command
conda install numpy
```

```shell
# use pip
pip install numpy
```

## 基础

### NumPy Ndarray 对象

```py
numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
```

| 名称   | 描述                                                         |
| ------ | ------------------------------------------------------------ |
| object | 数组或嵌套的数列                                             |
| dtype  | 数组元素的数据类型，可选                                     |
| copy   | 对象是否需要复制，可选                                       |
| order  | 创建数组的样式，C 为行方向，F 为列方向，A 为任意方向（默认） |
| subok  | 默认返回一个与基类类型一致的数组                             |
| ndmin  | 指定生成数组的最小维度                                       |

```py
import numpy as np
a = np.array([1,2,3])
print (a)

# >> [1 2 3]
```

### 创建数组

- numpy.empty

> 创建指定大小的数组，数组元素以 0 来填充： numpy.zeros

> 创建指定形状的数组，数组元素以 1 来填充： numpy.ones

> 从已有的数组创建数组 numpy.asarray

> 用于实现动态数组 numpy.frombuffer

> 从数值范围创建数组 numpy.arange

## 切片和索引

```py
import numpy as np

a = np.arange(10)
s = slice(2,7,2)   # 从索引 2 开始到索引 7 停止，间隔为2
print (a[s])

# >> [2  4  6]

a = np.array([
    [1, 2, 3],
    [3, 4, 5],
    [4, 5, 6]])
print(a[..., 1])   # 第2列元素
print('---------------------')
print(a[1, ...])   # 第2行元素
print('---------------------')
print(a[..., 1:])  # 第2列及剩下的所有元素
print('---------------------')
print(a[1:, ...])   # 第2行及剩下的所有元素

# [2 4 5]
# ---------------------
# [3 4 5]
# ---------------------
# [[2 3]
#  [4 5]
#  [5 6]]
# ---------------------
# [[3 4 5]
#  [4 5 6]]
```

## 高级索引

### 整数数组索引

```py
# 获取数组中 (0,0)，(1,1) 和 (2,0) 位置处的元素。
import numpy as np

x = np.array([[1,  2],  [3,  4],  [5,  6]])
y = x[[0,1,2],  [0,1,0]]
print (y)

# > [1  4  5]
```

### 布尔索引

```py
import numpy as np
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
print (x[x >  5])
```

### 花式索引

```py
# 一维数组
import numpy as np
x = np.arange(9)
x2 = x[[0, 6]] # [0 6]

# 二维数组
x=np.arange(32).reshape((8,4))
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]
#  [16 17 18 19]
#  [20 21 22 23]
#  [24 25 26 27]
#  [28 29 30 31]]
print (x[[4,2,1,7]]) # 输出下表为 4, 2, 1, 7 对应的行


# 传入多个索引数组（要使用 np.ix_）
x=np.arange(32).reshape((8,4))
print (x[np.ix_([1,5,7,2],[0,3,1,2])])

# [[ 4  7  5  6]
#  [20 23 21 22]
#  [28 31 29 30]
#  [ 8 11  9 10]]
```

## 广播(Broadcast)

```py
import numpy as np

a = np.array([1,2,3,4])
b = np.array([10,20,30,40])
c = a * b
print (c) # [ 10  40  90 160]


a = np.array([[ 0, 0, 0],
           [10,10,10],
           [20,20,20],
           [30,30,30]])
b = np.array([0,1,2])
print(a + b)
# [[ 0  1  2]
#  [10 11 12]
#  [20 21 22]
#  [30 31 32]]


a = np.array([[ 0, 0, 0],
           [10,10,10],
           [20,20,20],
           [30,30,30]])
b = np.array([1,2,3])
bb = np.tile(b, (4, 1))  # 重复 b 的各个维度
# [[1 2 3]
#  [1 2 3]
#  [1 2 3]
#  [1 2 3]]
print(a + bb)
# [[ 1  2  3]
#  [11 12 13]
#  [21 22 23]
#  [31 32 33]]
```

**广播的规则:**

- 让所有输入数组都向其中形状最长的数组看齐，形状中不足的部分都通过在前面加 1 补齐。
- 输出数组的形状是输入数组形状的各个维度上的最大值。
- 如果输入数组的某个维度和输出数组的对应维度的长度相同或者其长度为 1 时，这个数组能够用来计算，否则出错。
- 当输入数组的某个维度的长度为 1 时，沿着此维度运算时都用此维度上的第一组值。

**简单理解：**

- 对两个数组，分别比较他们的每一个维度（若其中一个数组没有当前维度则忽略），满足：
- 数组拥有相同形状。
- 当前维度的值相等。
- 当前维度的值有一个是 1。

## 迭代数组

```py
import numpy as np

a = np.arange(6).reshape(2,3)
# [[0 1 2]
#  [3 4 5]]
b = np.nditer(a)
for x in b:
    print(x, end=", ")
# 0, 1, 2, 3, 4, 5,

c = np.nditer(a.T.copy(order='C')):
for x in c:
    print(x, end=", ")
# 0, 3, 1, 4, 2, 5, %
```

```py
import numpy as np
a = np.arange(0,60,5)
a = a.reshape(3,4)

for x in np.nditer(a, flags =  ['external_loop'], order =  'F'):
   print (x, end=", " )

# 原始数组是：
# [[ 0  5 10 15]
#  [20 25 30 35]
#  [40 45 50 55]]

# 修改后的数组是：
# [ 0 20 40], [ 5 25 45], [10 30 50], [15 35 55],

```

## 数组操作

- 修改数组形状
- 翻转数组
- 修改数组维度
- 连接数组
- 分割数组
- 数组元素的添加与删除

## 位运算
