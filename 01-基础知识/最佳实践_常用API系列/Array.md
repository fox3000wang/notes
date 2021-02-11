# 数组常用 API

## 废弃不用的

```js
const legcay = [1, 2, 3];
delete legcay[1];
console.log(legcay);
legcay.length--;
console.log(legcay);
```

# 基础

- 记忆的方式：
  _ 1.方法的意义和作用
  _ 2.参数（执行方法的时候传递的内容）
  _ 3.返回值（执行完方法返回的结果）
  _ 4.原始数组是否改变

## 增删改的五个方法

### push pop shift unshift

```js
let cats = ['Bob'];
cats.push('Willy'); // ['Bob', 'Willy']
cats.push('Puff', 'George'); // ['Bob', 'Willy', 'Puff', 'George']

let cats = ['Bob', 'Willy', 'Mini'];
cats.pop(); // ['Bob', 'Willy']

let cats = ['Bob'];
cats.unshift('Willy'); // ['Willy', 'Bob']
cats.unshift('Puff', 'George'); // ['Puff', 'George', 'Willy', 'Bob']

let cats = ['Bob', 'Willy', 'Mini'];
cats.shift(); // ['Willy', 'Mini']
```

## splice

```js
/*
 * splice : 实现数组的增加、删除、修改
 * @params
 * n,m 都是数字 从索引n开始删除m个元素(m 不写，是删除到末尾)
 * @return
 * 把删除的部分用新数组存储起来返回 */

let ary = [10, 20, 30, 40, 50, 60, 70, 80, 90];
let res = ary.splice(2, 4);
console.log(ary); // [ 10, 20, 70, 80, 90 ]
console.log(res); // [ 30, 40, 50, 60 ]

// 删除最后一项和第一项 等价于pop 和 unshift
let a = [10, 20, 30, 40, 50, 60, 70, 80, 90];
a.splice(ary.length - 1);
a.splice(0, 1);
console.log(a);

// 清空数组
a.splice(0);
```

```js
/*
 * splice : 实现数组的增加、修改
 * @params
 * n,m,x 从索引n开始删除m个元素，用x占用删除的部分
 * n,0,x 从索引n开始，一个都不删，把x放到索引n的前面(左边)
 * @return
 * 把删除的部分用新数组存储起来返回 */

let ary = [10, 20, 30, 40, 50];
let res = ary.splice(1, 2, 'tom', 'jim');
console.log(res); // [ 20, 30 ]
console.log(ary); // [ 10, 'tom', 'jim', 40, 50 ]

// 向数组末尾追加 = push
ary.splice(ary.length, 0, 'foo');
console.log(ary); // [ 10, 'tom', 'jim', 40, 50, 'foo' ]

// 向数组开始追加 = shift
ary.splice(0, 0, 'bar');
console.log(ary); // ['bar', 10, 'tom', 'jim', 40, 50, 'foo']

// 向数组中插入
ary.splice(5, 0, 'fox');
console.log(ary);
```

## 数组的查询/克隆 slice

```js
/*
 * slice(n,m) 实现数组的查询
 * 从索引n开始，查找到索引为m处（不包含m）
 * 把查找到的内容以新数组的方式返回，原始数组不变
 */
let arr = [10, 20, 30, 40, 50, 60, 70];
let result = arr.slice(2, 5);
console.log(result, arr); //=>result=[30, 40, 50]  arr=[10, 20, 30, 40, 50, 60, 70]
```

## 数组拼接 concat

```js
/*
 * concat：实现数组拼接，
 * 把多个数组（或者多个值）最后拼接为一个数组
 * 原始的数组都不会变，返回结果是拼接后的新数组
 */
let arr1 = [10, 20, 30];
let arr2 = [50, 60, 70];

let arr = arr1.concat('boy', arr2);
console.log(arr); //=>[10, 20, 30, "boy", 50, 60, 70]
```

## 转字符串

- join
  - join() 方法用于把数组中的所有元素转换一个字符串。
  - 元素是通过指定的分隔符进行分隔的。

```js
/* 把数组转化为字符串：
 *   1. toString()：把数组中的每一项按照“逗号分隔”，拼接成对应的字符串
 *   2. join([char])：指定分隔符
 * 原始数组都不会改变
 */
let arr = [10, 20, 30, 40, 50, 60, 70];
console.log(arr.toString()); // '10,20,30,40,50,60,70'
console.log(arr.join()); // 等价于toString
console.log(arr.join('+')); // '10+20+30+40+50+60+70'
console.log(eval(arr.join('+'))); // 280 用于数组求和
```

## 获取数组中指定项的索引 indexOf includes

```js
/*
 * 获取数组中指定项的索引
 *  indexOf([item])：获取当前项在数组中第一次出现位置的索引
 *  lastIndexOf([item]) ：获取当前项在数组中最后一次出现位置的索引
 *  includes：验证数组中是否包含这一项，返回TRUE/FALSE
 * 原始数组不变
 */
let arr = [10, 20, 30, 10, 20, 10, 30];
console.log(arr.indexOf(20)); //=>1
console.log(arr.lastIndexOf(20)); //=>4
console.log(arr.indexOf(40)); //=>-1 如果数组中不包含这一项，则返回结果是-1

// =>基于这个特征来验证数组中是否包含某一项
if (arr.indexOf(40) > -1) {
  // 数组中包含这一项
}
console.log(arr.includes(40));
```

## reverse

把原始数组倒过来排列，返回的结果是排列后的原始数组，原始数组改变

## 排序 sort

把原始数组按照规则进行排序，原始数组会改变（返回结果也是改变后的原始数组）

```js
let arr = [12, 23, 110, 34, 2, 4, 9];
arr.sort((a, b) => a - b); // A-B 升序
console.log(arr); //=>[2, 4, 9, 12, 23, 34, 110]
arr.sort((a, b) => b - a); // B-A 降序
console.log(arr); //=>[ 110, 34, 23, 12, 9, 4, 2]
```

## 迭代

```js
/*
 * 数组中常用的迭代方法（遍历数组中每一项的）
 * forEach([函数])：遍历数组中的每一项
 * （数组中有多少项，函数会相继被执行多少次），每一次执行函数，都可以在函数中获取到当前遍历的这一项和对应的索引
 */
let arr = [10, 20, 30, 40, 50];
let total = 0;
arr.forEach(item => (total += item));
console.log(total); //150

/*
 * map：把原来数组中每一项的值替换成为新值，最后存储在一个新的数组中，但是原始数组是不变的
 *   forEach是不支持返回值的，而map可以在forEach的基础上支持返回值
 */
let arr = [10, 20, 30, 40, 50];
let total = 0;
let result = arr.map(item => item * 10);
console.log(result); // [ 100, 200, 300, 400, 500 ]
```

## reduce

### 定义和用法

- reduce() 方法接收一个函数作为累加器，数组中的每个值（从左到右）开始缩减，最终计算为一个值。
- reduce() 可以作为一个高阶函数，用于函数的 compose。
- 注意: reduce() 对于空数组是不会执行回调函数的。

### 语法

| 参数         | 描述                                   |
| ------------ | -------------------------------------- |
| total        | 必需。初始值, 或者计算结束后的返回值。 |
| currentValue | 必需。当前元素                         |
| currentIndex | 可选。当前元素的索引                   |
| arr          | 可选。当前元素所属的数组对象。         |

| 参数         | 描述                                                                                                                                              |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| initialValue | 可选,作为第一次调用 callback 函数时的第一个参数的值。 如果没有提供初始值，则将使用数组中的第一个元素。 在没有初始值的空数组上调用 reduce 将报错。 |

```js
array.reduce(function(total, currentValue, currentIndex, arr), initialValue)
```

```js
const arr = [10, 20, 30, 40];

let result = arr.reduce((result, item, index) => {
  console.log(`${result}, ${item}, ${index}`);
  return result;
});
console.log(result);
// 10, 20, 1
// 10, 30, 2
// 10, 40, 3
// 10

const arr = [10, 20, 30, 40];

let result = arr.reduce((result, item, index) => {
  console.log(`${result}, ${item}, ${index}`);
  return result + item;
});
console.log(result);

// 10, 20, 1
// 30, 30, 2
// 60, 40, 3
// 100
```

## find

find() 方法返回数组中满足提供的测试函数的第一个元素的值。否则返回 undefined。

```js
const array1 = [5, 12, 8, 130, 44];

const found = array1.find(element => element > 10);

console.log(found); // expected output: 12
```

## filter

filter() 方法创建一个新数组, 其包含通过所提供函数实现的测试的所有元素。

```js
const words = [
  'spray',
  'limit',
  'elite',
  'exuberant',
  'destruction',
  'present',
];

const result = words.filter(word => word.length > 6);

console.log(result); // ["exuberant", "destruction", "present"]
```

## every

every() 方法测试一个数组内的所有元素是否都能通过某个指定函数的测试。它返回一个布尔值。

> 注意：若收到一个空数组，此方法在一切情况下都会返回 true。

```js
const isBelowThreshold = currentValue => currentValue < 40;

const array1 = [1, 30, 39, 29, 10, 13];

console.log(array1.every(isBelowThreshold)); // true
```

## some

some() 方法测试数组中是不是至少有 1 个元素通过了被提供的函数测试。它返回的是一个布尔值。

> 注意：如果用一个空数组进行测试，在任何情况下它返回的都是 false。

```js
const array = [1, 2, 3, 4, 5];

// checks whether an element is even
const even = element => element % 2 === 0;

console.log(array.some(even)); // true
```

## map

map() 方法创建一个新数组，其结果是该数组中的每个元素是调用一次提供的函数后的返回值。

```js
const array1 = [1, 4, 9, 16];

// pass a function to map
const map1 = array1.map(x => x * 2);

console.log(map1);
// expected output: Array [2, 8, 18, 32]
```

---

## 小结

- 原始数组不变

  - slice
  - concat
  - toString
  - join

- 原始数组变化的
  - push
  - pop
  - shift
  - unshift
  - splice
  - reverse
