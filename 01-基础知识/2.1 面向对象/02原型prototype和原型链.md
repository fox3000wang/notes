# 原型和原型链

- 每一个类（函数）都具备 prototype，并且属性值是一个对象
- 对象上天生具备一个属性：constructor，指向类本身
- 每一个对象（普通对象、prototype、实例、函数等）都具备：\_\_proto\_\_，属性值是当前实例所属类的原型

## 原型 prototype

- 原型模式解决了成员共享的问题

## 原型链

## 原型重定向

1.内置类的原型是无法重定向的

2.在大量向原型上扩充方法的时候，重定向的操作一方面可以简化代码的编写。一方面也可以把所有扩充的公共属性和方法统一管理起来

- 弊端：重定向原型后，之前原型对象上存在的公共的属性和方法也都没有了（包含 constructor）
- 如果之前原型上没有手动扩充任何属性方法，则重定向的原型对象手动设置一个 constructor 即可
- 如果之前原型上还存在其他的属性方法，则在重定向之前最好做“新老”原型对象的合并处理

```js
function Fn() {
  this.x = 100;
  this.y = 200;
}
// Fn.prototype = {
//     constructor: Fn,
//     ...
// };
Fn.prototype.write = function () {};
Fn.prototype.read = function () {};
Fn.prototype = Object.assign(Fn.prototype, {
  say() {},
  eat() {},
  song() {},
  jump() {},
});
let f1 = new Fn();
console.log(f1);
```
