const jquery = require('./jquery');

function factory(window, noGlobal) {
  // window->window  noGlobal->undefined
  var arr = [];
  var slice = arr.slice; //Array.prototype.slice

  var version = '3.5.1',
    jQuery = function (selector, context) {
      return new jQuery.fn.init(selector, context);
    };
  jQuery.fn = jQuery.prototype = {
    constructor: jQuery,
    // 把JQ对象转换为原生对象
    get: function (num) {
      if (num == null) {
        // num=null/undefined
        return slice.call(this);
      }
      return num < 0 ? this[num + this.length] : this[num];
    },
    // 基于索引 最后返回的依然是实例对象
    eq: function (i) {
      var len = this.length,
        j = +i + (i < 0 ? len : 0);
      // this[j] 原生的，包在数组中
      return this.pushStack(j >= 0 && j < len ? [this[j]] : []);
    },
    pushStack: function (elems) {
      // this.constructor->jQuery  jQuery()空JQ实例
      // JQ对象:{0:xxx,length:1}
      var ret = jQuery.merge(this.constructor(), elems);
      ret.prevObject = this;
      return ret;
    },
    each: function (callback) {
      // $(...).each(callback)
      // this:JQ实例(类数组JQ对象)
      return jQuery.each(this, callback);
    },
  };

  jQuery.each = function each(obj, callback) {
    var length,
      i = 0;
    // isArrayLike:检测是否为数组或者类数组
    if (isArrayLike(obj)) {
      length = obj.length;
      for (; i < length; i++) {
        //每一轮循环都去执行回调函数
        //   + 传递实参：索引/当前项
        //   + 改变THIS：当前项
        //   + 接收返回值：如果回调函数返回false，则结束循环
        var result = callback.call(obj[i], i, obj[i]);
        if (result === false) {
          break;
        }
      }
    } else {
      // 对象
      /* for (i in obj) {
                // for in遍历的问题：
                //    + 1.遍历到原型上自己扩展的公共的属性
                //    + 2.顺序 
                //    + 3.无法找到symbol的属性
                if (callback.call(obj[i], i, obj[i]) === false) {
                    break;
                }
            } */
      var keys = Object.getOwnPropertyNames(obj).concat(
        Object.getOwnPropertySymbols(obj)
      );
      for (; i < keys.length; i++) {
        var key = keys[i];
        if (callback.call(obj[key], key, obj[key]) === false) {
          break;
        }
      }
    }
    return obj;
  };

  var rootjQuery = jQuery(document);
  var rquickExpr = /^(?:\s*(<[\w\W]+>)[^>]*|#([\w-]+))$/;
  var init = (jQuery.fn.init = function (selector, context, root) {
    var match, elem;
    // HANDLE: $(""), $(null), $(undefined), $(false)
    // 返回结果是一个JQ实例「空的实例对象」
    if (!selector) {
      return this;
    }
    // $('.xxx') => root=$(document)
    root = root || rootjQuery;
    // 选择器是一个字符串？
    if (typeof selector === 'string') {
      if (
        selector[0] === '<' &&
        selector[selector.length - 1] === '>' &&
        selector.length >= 3
      ) {
        match = [null, selector, null];
      } else {
        match = rquickExpr.exec(selector);
      }

      // Match html or make sure no context is specified for #id
      if (match && (match[1] || !context)) {
        // HANDLE: $(html) -> $(array)
        if (match[1]) {
          context = context instanceof jQuery ? context[0] : context;

          // Option to run scripts is true for back-compat
          // Intentionally let the error be thrown if parseHTML is not present
          jQuery.merge(
            this,
            jQuery.parseHTML(
              match[1],
              context && context.nodeType
                ? context.ownerDocument || context
                : document,
              true
            )
          );

          // HANDLE: $(html, props)
          if (rsingleTag.test(match[1]) && jQuery.isPlainObject(context)) {
            for (match in context) {
              // Properties of context are called as methods if possible
              if (isFunction(this[match])) {
                this[match](context[match]);
                // ...and otherwise set as attributes
              } else {
                this.attr(match, context[match]);
              }
            }
          }
          return this;
        } else {
          elem = document.getElementById(match[2]);

          if (elem) {
            // Inject the element directly into the jQuery object
            this[0] = elem;
            this.length = 1;
          }
          return this;
        }

        // HANDLE: $(expr, $(...))
      } else if (!context || context.jquery) {
        return (context || root).find(selector);

        // HANDLE: $(expr, context)
        // (which is just equivalent to: $(context).find(expr)
      } else {
        return this.constructor(context).find(selector);
      }

      // HANDLE: $(DOMElement)
    } else if (selector.nodeType) {
      // 选择器是一个节点「DOM元素节点/文本节点... JS获取的」
      this[0] = selector;
      this.length = 1;
      return this;
    } else if (isFunction(selector)) {
      // 选择器是一个函数  $(document).ready(函数) 「监听DOMContentLoaded事件：等到DOM结构加载完成，执行对应的方法」
      return root.ready !== undefined ? root.ready(selector) : selector(jQuery);
    }
    return jQuery.makeArray(selector, this);
  });
  init.prototype = jQuery.fn;

  // 浏览器环境下运行，条件成立的
  if (typeof noGlobal === 'undefined') {
    window.jQuery = window.$ = jQuery;
  }
}
factory(window);

//===========
// $() -> 就是把jQuery方法执行的「普通函数」 “JQ选择器”
// =>最后获取的结果是jQuery类的实例对象“JQ对象”
//    $('.box')
//    $('.box',conatiner)
/* $('.box')
jQuery('.box')
$.ajax({}); */
//...

//=> $(document).ready(函数)
/* $(function () {
    // 等待页面中的DOM结构渲染完，去执行回调函数
    // ...
}); */

// 基于JS方法获取的是原生DOM对象：可以调用内置的JS方法
// 基于$()获取的JQ对象，只能调JQ原型上的方法
// ===默认两种对象之间所用的方法不能混着调，想调用只能先相互转换
// 原生->JQ   $(原生对象)   {0:xxx,length:1...}  「类数组集合」
// JQ->原生   $xxx[索引] / $xxx.get(索引)
