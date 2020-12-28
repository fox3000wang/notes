// 几种方式重写new

function Dog(name) {
  this.name = name;
}
Dog.prototype.bark = function () {
  console.log('wangwang');
};
Dog.prototype.sayName = function () {
  console.log('my name is ' + this.name);
};
//
let sanmao = new Dog('三毛');
sanmao.sayName();
sanmao.bark();

// 普通方式重写new ==================================================================

function _new(Ctor, ...params) {
  // Ctor->Dog params->['三毛']
  // 1.创建一个实例对象  实例对象.__proto__===所属类.prototype
  let obj = {};
  obj.__proto__ = Ctor.prototype;

  // 2.会把构造函数当做普通函数执行「私有上下文、作用域链、初始THIS、形参赋值...」
  // this->指向创建的实例对象  基于call方法改变即可
  let result = Ctor.call(obj, ...params);

  // 3.观察函数执行的返回值，如果没有返回值或者返回的是基本数据类型值，
  //   默认返回的都是实例对象，否则以自己返回的值为主
  if (/^(object|function)$/.test(typeof result)) return result;
  return obj;
}

// 基于Object.create方式实现 ========================================================

function _new(Ctor, ...params) {
  let obj = Object.create(Ctor.prototype);
  let result = Ctor.call(obj, ...params);
  if (/^(object|function)$/.test(typeof result)) return result;
  return obj;
}

// 兼容性最好的方式实现 =================================================================

// 重写的方法只考虑pro传递的是一个对象
Object.create = function (pro) {
  function Proxy() {}
  Proxy.prototype = pro;
  return new Proxy();
};

function _new(Ctor) {
  // 获取除第一个实参以外，剩余传递的参数信息，以数组的形式保存到params中
  var params = [].slice.call(arguments, 1);
  // Object.create兼容IE低版本浏览器，需要改写
  var obj = Object.create(Ctor.prototype);
  // 基于apply既可以改变this，也可以把数组中的每一项传递给函数
  var result = Ctor.apply(obj, params);
  if (/^(object|function)$/.test(typeof result)) return result;
  return obj;
}
