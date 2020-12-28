(() => {
  // 简单粗暴的写法
  Function.prototype.call = function call(context, ...params) {
    context.xxx = this;
    let result = context.xxx(...params);
    delete context.xxx;
    return result;
  };
})();

(() => {
  /*
   * 优化1：临时给context设置的属性不能和原始对象中的属性冲突
   * 优化2：参数的处理} context
   */
  Function.prototype.call = function call(context, ...params) {
    // 优化2.1 context不传递或者传递null，最后要改的this都会是window
    context === null ? (context = window) : null;

    // 优化2.2 必须要保证context都是引用数据类型的值。因为基本属性类型值没有办法设置属性。
    !/^(object|function)$/.test(typeof context)
      ? (context = Object(context))
      : null;

    // 优化1， 因为 Symbol('KEY') !== Symbol('KEY')
    const key = Symbol('KEY');

    // this->fn 当前要执行的函数, context->obj 需要改变的this
    context[key] = this;

    // params->[10,20] 需要给函数传递的实参信息
    const result = context[key](...params);

    // 用完后删除临时增加的属性，不改变原始的数据结构
    delete context[key];
    return result;
  };

  let obj = {
    name: 'call',
    age: 11,
    [Symbol('KEY')]: '哈哈',
  };

  function fn(x, y) {
    console.log(this);
    return x + y;
  }
  let result = fn.call(100, 10, 20);
  console.log(result);
})();

// ============================================================================s

(() => {
  // 原理：闭包 “柯理化”
  Function.prototype.bind = function bind(context, ...params) {
    // this->fn 最后要执行的函数
    // context->obj 最后要改变的this
    // params->[10,20] 最后要传递的参数
    let that = this;
    return function proxy(...args) {
      return that.call(context, ...params, ...args);
    };
  };

  let obj = {
    name: '吃喝玩乐',
    age: 11,
  };

  function fn(x, y, ev) {
    console.log(this, ev, x + y);
  }

  document.body.onclick = fn.bind(obj, 10, 20);
  // 不用bind的时候用以下办法
  // document.body.onclick = function proxy(ev) {
  //     fn.call(obj, 10, 20, ev);
  // };
})();
