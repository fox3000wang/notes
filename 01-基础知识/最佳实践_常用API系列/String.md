# String

## 常用方法

- 获取字符串中指定位置字符的办法
  - charAt
  - charCodeAt
  - String.fromCharCode
- 字符串查找和截取
  - substr
  - substring
  - slice
- 字符串转换为数组的方法
  - split
- 字符串查找是否包含某个字符
  - indexOf / lastIndexOf
  - includes
- 字符串替换
  - replace
- 字符串大小写转换
  - toLowerCase
  - toUpperCase

## 记忆方式:

- 方法的意义和作用
- 参数
- 返回值

字符串中无需记忆原始字符串是否改变，因为它是基本类型值，每一个操作都是直接操作值，对原始字符串不会产生任何影响
（数组之所以要记住是否改变，是因为数组是对象类型，操作的是堆内存，方法的执行很可能把原始堆内存中的信息改变了，所以需要记忆原始数组是否改变）

### 获取字符串中指定位置字符的办法

charAt(index) 方法从一个字符串中返回指定的字符。
charCodeAt(index)：在 charAt 的基础上，方法返回 0 到 65535 之间的整数，获取指定字符的 UNICODE 编码（ASCII 码表中的值）
String.fromCharCode([UNICODE 编码])：和 charCodeAt 对应，它是基于编码获取编码前的字符

```js
let str = 'welcome to zhufeng peixun！';
console.log(str[0]); //=>'w'
console.log(str.charAt(0)); //=>'w'
console.log(str[str.length - 1]); //=>'！'
console.log(str.charAt(str.length - 1)); //=>'！'
console.log(str[str.length]); //=>undefined
console.log(str.charAt(str.length)); //=>''

console.log(str.charCodeAt(0)); //=>119 （UNICODE编码，也就是值的十进制编码）
console.log(String.fromCharCode(119)); //=>'w'
```

### 字符串截取

substr(n,m)：从索引 n 开始截取 m 个字符
substring(n,m)：从索引 n 开始，找到索引为 m 处（不包含 m），找到部分截取到
slice(n,m)：和 substring 是以一样的，两个都是索引，只不过 slice 支持以负数作为索引
最后的 m 不写都是截取到字符串的末尾

```js
let str = 'welcome to zhufeng peixun！';
console.log(str.substr(3, 8)); //=>'come to '
console.log(str.substring(3, 8)); //=>come '
console.log(str.substring(3)); //=>substr&substring第二个参数不写都是截取到末尾  str.substring(0)：字符串克隆
console.log(str.substring(-6, -3)); //=>'' substring只能支持正常的索引
console.log(str.slice(-6, -3)); //=>'eix'  slice支持负数索引
// 负数索引也可以这样处理str.slice(str.length-6, str.length-3) => str.slice(20,23)
```

### 字符串查找是否包含某个字符

indexOf / lastIndexOf：获取当前字符在字符串中第一次或者最后一次出现位置的索引，如果字符串中不包含这个字符，返回结果是-1
includes 验证是否包含某个字符

```js
let str = 'welcome to zhufeng peixun！';
console.log(str.indexOf('e')); //=>1
console.log(str.lastIndexOf('e')); //=>20
if (str.indexOf('a') > -1) {
  // 包含字符a
}
if (str.includes('a')) {
  // 包含字符a
}
```

### 大小写转换

toLowerCase / toUpperCase：把字符串中的字符进行大小写转换

```js
let str = 'Welcome To ZHUFENG!';
console.log(str.toLowerCase()); //=>'welcome to zhufeng!'
console.log(str.toUpperCase()); //=>'WELCOME TO ZHUFENG!'
```

### 拆分字符串，转换成数组

split：和数组中的 join 方法对应，它是把字符串，按照指定的分隔符号，拆分成数组中的每一项，返回结果是一个数组

```js
let arr = [10, 20, 30, 40];
let str = arr.join('|');
// console.log(str); //=>'10|20|30|40'
console.log(str.split('|')); //=>["10", "20", "30", "40"]

let str = 'welcome to zhufeng peixun';
console.log(str.split(' ')); //=>以空格拆分  ["welcome", "to", "zhufeng", "peixun"]
console.log(str.split('')); //=>不指定任何分隔符 ["w", "e", "l", "c", "o", "m", "e", " ", "t", "o", " ", "z", "h", "u", "f", "e", "n", "g", " ", "p", "e", "i", "x", "u", "n"]
```

### 替换

replace(原始字符,新字符)：把字符串中原始字符替换成为新字符，在不使用正则的情况下，每次执行 replace 只能替换一个
一般需要配合正则表达式来使用

```js
let str = 'zhufeng2020zhufeng2021';
str = str.replace('zhufeng', '替换');
str = str.replace('zhufeng', '替换');
console.log(str); //=>'替换 2020 替换 2021'

str = str.replace('zhufeng', 'zhufengpeixun');
str = str.replace('zhufeng', 'zhufengpeixun');
console.log(str); //=>'zhufengpeixunpeixun2020zhufeng2021' 很多时候即使执行多次也不一定能够实现最后的效果，所以replace一般都是伴随正则出现的
str = str.replace(/zhufeng/g, 'zhufengpeixun');
console.log(str); //=>'zhufengpeixun2020zhufengpeixun2021'
```

### String.prototype.localeCompare()

localeCompare() 方法返回一个数字来指示一个参考字符串是否在排序顺序前面或之后或与给定字符串相同。

新的 locales 、 options 参数能让应用程序定制函数的行为即指定用来排序的语言。

locales 和 options 参数是依赖于具体实现的，在旧的实现中这两个参数是完全被忽略的。

```js
// The letter "a" is before "c" yielding a negative value
'a'.localeCompare('c');
// -2 or -1 (or some other negative value)

// Alphabetically the word "check" comes after "against" yielding a positive value
'check'.localeCompare('against');
// 2 or 1 (or some other positive value)

// "a" and "a" are equivalent yielding a neutral value of zero
'a'.localeCompare('a');
// 0
```

### match

使用正则表达式与字符串相比较。

### trim

从字符串的开始和结尾去除空格。参照部分 ECMAScript 5 标准。
