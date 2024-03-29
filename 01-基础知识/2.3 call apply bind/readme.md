# call apply bind 改变 this 指向

# THIS 的几种情况

- 事件绑定
- 函数执行
  - 自执行函数
  - 回调函数
  - ...
- 构造函数执行
- 基于 call/apply/bind 改变函数中的 this
- 箭头函数中没有自己的 this，所用到的 this 是使用其上下文中的

## call

### 方法重用

- call() 方法是预定义的 JavaScript 方法。
- 它可以用来调用所有者对象作为参数的方法。
- 通过 call()，您能够使用属于另一个对象的方法。
- 本例调用 person 的 sum 方法，并用于 obj

简洁的说法就是：改变调用方法的 this 指向

```js
Function.prototype.call = function call(context) {
  // this->fn
  // context->obj
  // ...
};

window.name = 'WINDOW';

const obj = {
  name: '弱智青年',
  age: 11,
  left: 2,
  right: 3,
};

function fn(x, y) {
  console.log(this, x + y);
}

const person = {
  sum: function () {
    return this.left + this.right;
  },
};

fn(); //this->window
obj.fn(); //Uncaught TypeError: obj.fn is not a function
fn.call(obj);

console.log(person.sum.call(obj));
```

### 帮助理解

就是 obj 和 person 毛线关系都没有, 互相没有依赖
obj 呢就可以看做一个弱智青年，他左边口袋有 2 块钱，右边口袋有 3 块钱，他不知道自己总共有多少钱
这个时候呢，好心人 person，他有计算能力, 这个 sum 可以帮助这个 obj 计算他自己口袋里 总共有多少钱
这个能力不是，通过 obj 传递 left，而是改变调用方法的 this 指向

## call 的原理

- fn.call(obj); //this->obj
- fn 先基于\_\_proto\_\_找到 Function.prototype.call
- 把 call 方法执行的时候，call 方法内部实现了一些功能：
  - 会把 fn 执行
  - 让 fn 中的 this 变为第一个实参值

```js
fn.call(obj, 10, 20); //this->obj x->10 y->20
fn.call(); //this->window 严格模式下 undefined
fn.call(null); //this->window 严格模式下 null 「传递的是 undefiend 也是如此」
fn.call(10, 20); //this->10「对象」 x->20 y->undefined
```

## apply

apply 的作用和细节上和 call 一样，只有一个区别：传递给函数实参的方式不一样

```js
fn.call(obj, 10, 20);
fn.apply(obj, [10, 20]);
```

- 最后结果和 call 是一样的
- 只不过 apply 方法执行的时候要求：
  - 传递给函数的实参信息都要放置在一个数组中
  - 但是 apply 内部也会向 call 方法一样
  - 把这些实参信息一项项的传递给函数

## 实战

### 需求：获取数组中的最大值

```js
let arr = [10, 30, 15, 36, 23];

// 先排序
{
  arr.sort(function (a, b) {
    return b - a; // 从大到小排序
  });
  let max = arr[0];
  console.log('数组中的最大值是:' + max);
}

// 假设法
{
  let max = arr[0];
  for (let i = 1; i < arr.length; i++) {
    let item = arr[i];
    if (item > max) {
      max = item;
    }
  }
}

// reduce版假设
{
  let max = arr.reduce((result, item) => {
    return item > result ? item : result;
  });
}

// 借用Math.max
{
  Math.max(10, 30, 15, 36, 23); // ->36 获取一堆数中的最大值
  Math.max([10, 30, 15, 36, 23]); // ->NaN 传递一个数组是不行的
  let max = Math.max(...arr); // 使用ES6的运算展开符
}

// 基于apply
{
  let max = Math.max.apply(null, arr);
}

// 字符串拼接
{
  // 把当前的数组变成这样一个字符串 'Math.max(10, 30, 15, 36, 23)'
  let str = `Math.max(${arr})`;
  let max = eval(str);
}
```

### 需求：把类数组集合转换为数组集合

```js
/**
 * arguments:实参集合,它是一个类数组,不是Array的实例
 * 所以不能直接调用Array.prototype上的方法
 * 但是结构和数组非常的相似,都是索引+length
 */

// 常规办法
function sum() {
  let arr = [];
  for (let i = 0; i < arguments.length; i++) {
    let item = arguments[i];
    arr.push(item);
  }
  return arr.reduce((result, item) => item + result);
}

function sum() {
  //Array.from:可以把一个类数组(或者Set)转换为数组
  let arr = Array.from(arguments);

  // 基于展开运算符把类数组中的每一项拿出来，分别赋值给数组
  let arr = [...arguments];

  return arr.reduce((result, item) => item + result);
}
function sum(...arr) {
  // 基于剩余运算符获取的实参集合本身就是一个数组
  return arr.reduce((result, item) => item + result);
}

//
Array.prototype.slice = function slice() {
  // 重写内置的slice，实现浅克隆
  // this->ary
  let arr = [];
  for (let i = 0; i < this.length; i++) {
    let item = this[i];
    arr.push(item);
  }
  return arr;
};
let ary = [10, 20, 30];
let newAry = ary.slice(); //不传递或者传递0 -> 数组的浅克隆
console.log(newAry, newAry === ary);

function sum() {
  let arr = [].slice.call(arguments);
  return arr.reduce((result, item) => item + result);
}
```

### bind

- 事件绑定的时候方法是没有执行的，只有事件触发，浏览器会帮助我们把方法执行
- this->body
- x->MouseEvent 事件对象「浏览器不仅帮助我们把方法执行，而且还把存储当前操作的信息的事件对象传递给函数」
- y->undefined
- document.body.onclick = fn;

- 设置一个定时器（此时绑定的函数没有执行，此时只是绑定一个方法），1000MS 后，浏览器会帮助我们把 fn 执行
- this->window
- x->undefined
- y->undefined
- setTimeout(fn, 1000);

#### 我们期望:不论是事件触发，还是定时器到时间，执行对应的方法时，可以改变方法中的 this，以及给方法传递实参信息

- 直接下属这种操作办法是不可以的：call/apply 在处理的时候，会把函数立即执行，也就是在事件绑定或者设置定时器的时候，fn 就执行了，而不是等待事件触发或者定时器到时间后再执行 “立即处理的思想”

  - document.body.onclick = fn.call(obj, 10, 20);
  - setTimeout(fn.call(obj, 10, 20), 1000);

- 预先处理思想「柯理化函数」
  我们绑定方法的时候(不论是事件绑定还是设置定时器)，先绑定一个匿名函数，事件触发或者达到时间，先把匿名函数执行，在执行匿名函数的时候，再把我们需要执行的 fn 执行，此时就可以基于 call/apply 改变 this 和参数信息了

```js
document.body.onclick = function (ev) {
  //this->body
  fn.call(obj, 10, 20, ev);
};
setTimeout(function () {
  //this->window
  fn.call(obj, 10, 20);
}, 1000);
```

- bind 相当于 call/apply 来讲，并不会把函数立即执行，只是实现处理了要改变的 this 和参数，一切的执行还是按照原有的时间或者触发节点进行

```js
document.body.onclick = fn.bind(obj, 10, 20);
setTimeout(fn.bind(obj, 10, 20), 1000);
```

### 箭头函数

```js
let obj = {
  name: '箭头函数',
  age: 11,
  fn: function () {
    // this->obj
    return () => {
      this.name = 'jiantou2020';
      console.log(this);
    };
  },
};
let f = obj.fn();
f.call(100);
```

- 箭头函数没有 this（方法执行的时候不存在初始 this 这一项操作）
- 所以基于 call/apply 操作它都是无用的，没有 this，改啥？

```js
let obj = {
  name: '箭头函数',
  age: 11,
  fn: function () {
    // this->obj
    let that = this;
    return function () {
      // this->window
      // 如果需要改变 obj.name，可以用 that 替换 this
      that.name = 'jiantou2020';
      console.log(this);
    };
  },
};
let f = obj.fn();
f();
```
