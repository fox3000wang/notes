/*
 * JS高阶编程技巧「本质：基于“闭包”的机制完成的」
 *   闭包的特点：
 *     + 保护
 *     + 保存
 *     + 弊端:占用内存，消耗浏览器的性能（闭包可以用，但是不能滥用）
 *
 * 应用6：jQuery（JQ）中关于闭包的使用
 */

// 利用JS的暂时性死区:基于typeof检测一个未被声明的变量,不会报错,结果是undefined
//   + 浏览器环境下 & APP的webview环境下：默认就有window -> GO
//   + Node环境下：没有window，this->global || 当前模块
let params1 = typeof window !== 'undefined' ? window : this;
let params2 = function (window, noGlobal) {
  // 浏览器环境下:window->window noGlobal->undefined
  // Node环境下:window->this noGlobal->true

  var jQuery = function (selector, context) {
    // ...
  };

  // 暴露到全局的，不宜过多
  // 浏览器环境下，基于window.xxx=xxx的方式，把jQuery暴露到全局
  //   jQuery() 或者 $() -> 都是把内部私有的jQuery执行
  if (typeof noGlobal === 'undefined') {
    window.jQuery = window.$ = jQuery;
  }

  return jQuery;
};

(function (window, noGlobal) {
  // 浏览器环境下:
  'use strict';
  if (typeof module === 'object' && typeof module.exports === 'object') {
    // 支持
  } else {
  }
})(params1, params2);
