## JS 篇

### 说几条写JavaScript的基本规范

* 不要在同一行声明多个变量
* 请是用 ===/!== 来比较`true/false `或者数值
* 使用对象字面量替代`new Array`这种形式
* 不要使用全局函数
* `Switch` 语句必须带有`default` 分支
* `If `语句必须使用大括号
* `for-in` 循环中的变量 应该使用`let` 关键字明确限定作用域，从而避免作用域污染

### 绕不过去的闭包

* 闭包就是能够读取其他函数内部变量的函数
* 闭包是指有权访问另一个函数作用域中变量的函数，创建闭包的最常见的方式就是在一个
* 函数内创建另一个函数，通过另一个函数访问这个函数的局部变量,利用闭包可以突破作用链域
* 闭包的特性：
  * 函数内再嵌套函数
  * 内部函数可以引用外层的参数和变量
  * 参数和变量不会被垃圾回收机制回收
* 优点：能够实现封装和缓存等
* 缺点：消耗内存、使用不当会内存溢出，
* 解决方法：在退出函数之前，将不使用的局部变量全部删除

### 说说你对作用域链的理解

* 作用域链的作用是保证执行环境里有权访问的变量和函数是有序的，作用域链的变量只能向上访问，变量访问到`window`对象即被终止，作用域链向下访问变量是不被允许的。
* 简单的说，作用域就是变量与函数的可访问范围，即作用域控制着变量与函数的可见性和生命周期

### JavaScript原型，原型链 ? 有什么特点？

* 每个对象都会在其内部初始化一个属性，就是`prototype` (原型)，当我们访问一个对象的属性时,如果这个对象内部不存在这个属性，那么他就会去`prototype` 里找这个属性，这个`prototype` 又会有自己的`prototype` ，于是就这样一直找下去，也就是我们平时所说的原型链的概念
* 关系：`instance.constructor.prototype = instance._<em>proto</em>_`
* 特点：`JavaScript` 对象是通过引用来传递的，我们创建的每个新对象实体中并没有一份属于自己的原型副本。当我们修改原型时，与之相关的对象也会继承这一改变当我们需要一个属性的时，`Javascript` 引擎会先看当前对象中是否有这个属性， 如果没有的,就会查找他的`Prototype` 对象是否有这个属性，如此递推下去，一直检索到`Object`内建对象

### 请解释什么是事件委托/事件代理

* 事件代理`（ Event Delegation ）`，又称之为事件委托。是`JavaScript` 中常用的绑定事件的常用技巧。顾名思义，“事件代理”即是把原本需要绑定的事件委托给父元素，让父元素担当事件监听的职务。事件代理的原理是`DOM`元素的事件冒泡。使用事件代理的好处是可以提高性能
* 可以大量节省内存占用，减少事件注册，比如在`table `上代理所有`td 的 click` 事件就非常棒
* 可以实现当新增子对象时无需再次对其绑定

### Javascript如何实现继承？

* 构造继承
* 原型继承
* 实例继承
* 拷贝继承
* 原型`prototype `机制或`apply 和 call` 方法去实现较简单，建议使用构造函数与原型混合方式

```java copyable
function Parent(){
this.name = 'wang';
}
function Child(){
 this.age = 28;
}
Child.prototype = new Parent();//继承了Parent，通过原型
var demo = new Child();
alert(demo.age);
alert(demo.name);//得到被继承的属性
复制代码
```

### 谈谈This对象的理解

* `this `总是指向函数的直接调用者（而非间接调用者）
* 如果有`new` 关键字，`this` 指向`new` 出来的那个对象
* 在事件中，` this` 指向触发这个事件的对象，特殊的是，`IE`中的`attachEvent 中的this` 总是指向全局对象`Window`

### 事件模型

> `W3C` 中定义事件的发生经历三个阶段：捕获阶段（` capturing` ）、目标阶段
> （`targetin`）、冒泡阶段（ `bubbling `）

* 冒泡型事件：当你使用事件冒泡时，子级元素先触发，父级元素后触发
* 捕获型事件：当你使用事件捕获时，父级元素先触发，子级元素后触发
* `DOM` 事件流：同时支持两种事件模型：捕获型事件和冒泡型事件
* 阻止冒泡：在`W3c` 中，使用`stopPropagation()` 方法；在IE下设置`cancelBubble =true`
* 阻止捕获：阻止事件的默认行为，例如`click - a`后的跳转。在`W3c `中，使用`preventDefault()` 方法，在 IE 下设置`window.event.returnValue = false`

### new操作符具体干了什么呢?

* 创建一个空对象，并且`this` 变量引用该对象，同时还继承了该函数的原型
* 属性和方法被加入到`this` 引用的对象中
* 新创建的对象由`this` 所引用，并且最后隐式的返回`this`

### Ajax原理

* `Ajax` 的原理简单来说是在用户和服务器之间加了—个中间层( AJAX 引擎)，通过`XmlHttpRequest` 对象来向服务器发异步请求，从服务器获得数据，然后用`javascript`来操作`DOM` 而更新页面。使用户操作与服务器响应异步化。这其中最关键的一步就是从服务器获得请求数据
* `Ajax `的过程只涉及`JavaScript 、 XMLHttpRequest 和 DOM 。 XMLHttpRequest`是`ajax`的核心机制

### 如何解决跨域问题?

> 首先了解下浏览器的同源策略 同源策略 `/SOP（Same origin policy）` 是一种约定，由Netscape公司1995年引入浏览器，它是浏览器最核心也最基本的安全功能，如果缺少了同源策略，浏览器很容易受到 `XSS 、 CSFR `等攻击。所谓同源是指`"协议+域名+端口"`三者相同，即便两个不同的域名指向同一个ip地址，也非同源

* 通过`jsonp`跨域

```java copyable
var script = document.createElement('script');
script.type = 'text/javascript';
// 传参并指定回调执行函数为onBack
script.src = 'http://www.....:8080/login?user=admin&callback=onBack';
document.head.appendChild(script);
// 回调执行函数
function onBack(res) {
 alert(JSON.stringify(res));
}

复制代码
```

* `document.domain + iframe`跨域

```java copyable
//父窗口：(http://www.domain.com/a.html)
<iframe id="iframe" src="http://child.domain.com/b.html"></iframe>
<script>
 document.domain = 'domain.com';
 var user = 'admin';
</script>

//子窗口：(http://child.domain.com/b.html)
document.domain = 'domain.com';
// 获取父窗口中变量
alert('get js data from parent ---> ' + window.parent.user);
复制代码
```

* `nginx`代理跨域
* `nodejs`中间件代理跨域
* 后端在头部信息里面设置安全域名

### 说说你对AMD和Commonjs的理解

* `CommonJS` 是服务器端模块的规范，`Node.js` 采用了这个规范。`CommonJS` 规范加载模

块是同步的，也就是说，只有加载完成，才能执行后面的操作。`AMD`规范则是非同步加载
模块，允许指定回调函数

* `AMD` 推荐的风格通过返回一个对象做为模块对象，`CommonJS `的风格通过对

`module.exports 或 exports `的属性赋值来达到暴露模块对象的目的

### js的7种基本数据类型

`Undefined 、 Null 、Boolean 、Number 、String 、Bigint 、Symbol`
[感谢：字符搬运工 同学纠正](https://juejin.cn/user/501033034600989)

### 介绍js有哪些内置对象

* `Object` 是`JavaScript `中所有对象的父对象
* 数据封装类对象：`Object 、 Array 、 Boolean 、 Number 和 String`
* 其他对象：`Function 、 Arguments 、 Math 、 Date 、 RegExp 、 Error`

### JS有哪些方法定义对象

* 对象字面量：`var obj = {}`;
* 构造函数：`var obj = new Object()`;
* Object.create():`var obj = Object.create(Object.prototype);`

### 你觉得jQuery源码有哪些写的好的地方

* `jquery` 源码封装在一个匿名函数的自执行环境中，有助于防止变量的全局污染，然后通过传入`window` 对象参数，可以使`window `对象作为局部变量使用，好处是当`jquery `中访问`window`对象的时候，就不用将作用域链退回到顶层作用域了，从而可以更快的访问`window`对象。同样，传入`undefined `参数，可以缩短查找`undefined` 时的作用域链
* `jquery `将一些原型属性和方法封装在了`jquery.prototype `中，为了缩短名称，又赋值给了`jquery.fn `，这是很形象的写法
* 有一些数组或对象的方法经常能使用到，`jQuery` 将其保存为局部变量以提高访问速度
* `jquery `实现的链式调用可以节约代码，所返回的都是同一个对象，可以提高代码效率

### null，undefined 的区别

* `undefined` 表示不存在这个值。
* `undefined `:是一个表示"无"的原始值或者说表示"缺少值"，就是此处应该有一个值，但是还没有定义。尝试读取时会返回`undefined`
* 例如变量被声明了，但没有赋值时，就等于`undefined`
* `null` 表示一个对象被定义了，值为“空值”
* `null `: 是一个对象(空对象, 没有任何属性和方法)
* 例如作为函数的参数，表示该函数的参数不是对象；
* 在验证`null` 时，一定要使用 === ，因为 == 无法分别`null 和 undefined`

### 谈谈你对ES6的理解

* 新增模板字符串（为`JavaScript` 提供了简单的字符串插值功能）
* 箭头函数
* `for-of `（用来遍历数据—例如数组中的值。）
* `arguments` 对象可被不定参数和默认参数完美代替。
* `ES6 `将`promise` 对象纳入规范，提供了原生的`Promise `对象。
* 增加了`let 和 const` 命令，用来声明变量。
* 还有就是引入`module` 模块的概念

[更多ES新语法：阮一峰的ES入门：https://es6.ruanyifeng.com/#docs/style](https://es6.ruanyifeng.com/#docs/style)

### 面向对象编程思想

* 基本思想是使用对象，类，继承，封装等基本概念来进行程序设计
* 易维护
* 易扩展
* 开发工作的重用性、继承性高，降低重复工作量。
* 缩短了开发周期

### 如何通过JS判断一个数组

* `instanceof` 运算符是用来测试一个对象是否在其原型链原型构造函数的属性

```js copyable
var arr = [];
arr instanceof Array; // true
复制代码
```

* `isArray`

```js copyable
Array.isArray([]) //true
Array.isArray(1) //false
复制代码
```

* `constructor` 属性返回对创建此对象的数组函数的引用，就是返回对象相对应的构造函数

```js copyable
var arr = [];
arr.constructor == Array; //true
复制代码
```

* `Object.prototype`

```js copyable
Object.prototype.toString.call([]) == '[object Array]'
// 写个方法
var isType = function (obj) {
 return Object.prototype.toString.call(obj).slice(8,-1);
 //return Object.prototype.toString.apply([obj]).slice(8,-1);
}
isType([])  //Array
复制代码
```

### 异步编程的实现方式

* 回调函数
  * 优点：简单、容易理解
  * 缺点：不利于维护，代码耦合高
* 事件监听(采用时间驱动模式，取决于某个事件是否发生)
  * 优点：容易理解，可以绑定多个事件，每个事件可以指定多个回调函数
  * 缺点：事件驱动型，流程不够清晰
* 发布/订阅(观察者模式)
  * 类似于事件监听，但是可以通过‘消息中心‘，了解现在有多少发布者，多少订阅者
* `Promise`对象
  * 优点：可以利用`then`方法，进行链式写法；可以书写错误时的回调函数；
  * 缺点：编写和理解，相对比较难
* `Generator`函数
  * 优点：函数体内外的数据交换、错误处理机制
  * 缺点：流程管理不方便
* `async`函数
  * 优点：内置执行器、更好的语义、更广的适用性、返回的是`Promise`、结构清晰。
  * 缺点：错误处理机制

### 对原生Javascript了解方向

数据类型、运算、对象、`Function`、继承、闭包、作用域、原型链、事件、 `RegExp `、`JSON` 、 `Ajax `、 `DOM` 、 `BOM `、内存泄漏、跨域、异步装载、模板引擎、`前端MVC `、路由、模块化、 `Canvas `、 `ECMAScript`

### sort 快速打乱数组

```js copyable
var arr = [1,2,3,4,5,6,7,8,9,10];
arr.sort(()=> Math.random() - 0.5)
//利用sort return 大于等于0不交换位置，小于0交换位置
// [5, 8, 4, 3, 2, 9, 10, 6, 1, 7]
复制代码
```

### 数组去重操作

* `ES6 Set`
* `for`循环`indexOf`
* `for`循环`includes`
* `sort`

[详细操作前往：https://juejin.cn/post/6844904035619700750](https://juejin.cn/post/6844904035619700750)

### JS 原生拖拽节点

* 给需要拖拽的节点绑定`mousedown , mousemove , mouseup` 事件
* `mousedown` 事件触发后，开始拖拽
* `mousemove` 时，需要通过`event.clientX 和 clientY `获取拖拽位置，并实时更新位置
* `mouseup` 时，拖拽结束
* 需要注意浏览器边界值，设置拖拽范围

### 深拷贝、浅拷贝

* 所有的基础数据类型的赋值操作都是深拷贝
* 通常利用上面这点，来对引用数据类型做递归深拷贝
* 浅拷贝：`Object.assign` 或者 扩展运算符
* 深拷贝：`JSON.parse(JSON.stringify(object))` 深层递归
  * 局限性：会忽略 undefined，不能序列化函数，不能解决循环引用的对象

[详细信息更多：https://juejin.cn/post/6906369563793817607**](https://juejin.cn/post/6906369563793817607)

### 节流防抖

* 节流：每隔一段时间执行一次，通常用在高频率触发的地方，降低频率。--如：鼠标滑动 拖拽
* 防抖：一段时间内连续触发，不执行，直到超出限定时间执行最后一次。--如：`input` 模糊搜索

[更多节流、防抖，细节介绍：https://juejin.cn/post/6844903592898330638](https://juejin.cn/post/6844903592898330638)

### 变量提升

> 当执行 `JS` 代码时，会生成执行环境，只要代码不是写在函数中的，就是在全局执行环境中，函数中的代码会产生函数执行环境，只此两种执行环境

```js
b() // call b
console.log(a) // undefined
var a = 'Hello world'
function b() {
 console.log('call b')
}
```

> 变量提升
> 这是因为函数和变量提升的原因。通常提升的解释是说将声明的代码移动到了顶部，这其实没有什么错误，便于大家理解。但是更准确的解释应该是：在生成执行环境时，会有两个阶段。第一个阶段是创建的阶段，`JS `解释器会找出需要提升的变量和函数，并且给他们提前在内存中开辟好空间，函数的话会将整个函数存入内存中，变量只声明并且赋值为 `undefined` ，所以在第二个阶段，也就是代码执行阶段，我们可以直接提前使用

```js copyable
b() // call b second
function b() {
 console.log('call b fist')
}
function b() {
 console.log('call b second')
}
var b = 'Hello world'

复制代码
```

### js单线程

* 单线程 - 只有一个线程，只能做一件事
* 原因 - 避免`DOM` 渲染的冲突
  * 浏览器需要渲染`DOM`
  * `JS` 可以修改`DOM `结构
  * `JS` 执行的时候，浏览器`DOM `渲染会暂停
  * 两段`JS` 也不能同时执行（都修改`DOM` 就冲突了）
  * `webworker` 支持多线程，但是不能访问`DOM`
* 解决方案 - 异步

### 说说event loop

> 首先， `js `是单线程的，主要的任务是处理用户的交互，而用户的交互无非就
> 是响应` DOM` 的增删改，使用事件队列的形式，一次事件循环只处理一个事件
> 响应，使得脚本执行相对连续，所以有了事件队列，用来储存待执行的事件，
> 那么事件队列的事件从哪里被 `push` 进来的呢。那就是另外一个线程叫事件触
> 发线程做的事情了，他的作用主要是在定时触发器线程、异步 `HTTP` 请求线程
> 满足特定条件下的回调函数 `push` 到事件队列中，等待 `js `引擎空闲的时候去
> 执行，当然`js`引擎执行过程中有优先级之分，首先`js`引擎在一次事件循环中，
> 会先执行js线程的主任务，然后会去查找是否有微任务
> `microtask（promise） `，如果有那就优先执行微任务，如果没有，在去查找
> 宏任务` macrotask（setTimeout、setInterval）` 进行执行

[更详细的介绍前往：https://juejin.cn/post/6844903598573240327](https://juejin.cn/post/6844903598573240327)

### 描述下this

> `this `，函数执行的上下文，可以通过 `apply ， call ， bind `改变 `this`
> 的指向。对于匿名函数或者直接调用的函数来说，this指向全局上下文（浏览
> 器为`window，NodeJS为 global `），剩下的函数调用，那就是谁调用它，
> `this `就指向谁。当然还有`es6`的箭头函数，箭头函数的指向取决于该箭头函
> 数声明的位置，在哪里声明， `this `就指向哪里

### ajax、axios、fetch区别

ajax：

* 本身是针对` MVC` 的编程,不符合现在前端`MVVM`的浪潮
* 基于原生的`XHR `开发，`XHR` 本身的架构不清晰，已经有了`fetch `的替代方案
* `JQuery` 整个项目太大，单纯使用`ajax` 却要引入整个`JQuery` 非常的不合理（采取个性化打包的方案又不能享受`CDN`服务）

axios：

* 从浏览器中创建`XMLHttpRequest`
* 从`node.js` 发出`http `请求
* 支持` Promise API`
* 拦截请求和响应
* 转换请求和响应数据
* 取消请求
* 自动转换`JSON`数据
* 客户端支持防止`CSRF/XSRF`

fetch：

* 只对网络请求报错，对 400 ， 500 都当做成功的请求，需要封装去处理
* 默认不会带`cookie` ，需要添加配置项（尴尬）
* 本身无自带`abort `，无法超时控制，可以使用AbortController解决取消请求问题。

[感谢：九旬 同学纠错](https://juejin.cn/user/4037062426631288)

* 没有办法原生监测请求的进度，而`XHR`可以
