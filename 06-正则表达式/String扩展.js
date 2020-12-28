/**
 * 这个小型库用于扩展string上的方法
 * 主要以正则表达式为主
 */

~(function () {
  /**
   * 时间字符串格式化
   * @params
   *  template:[string] 模板规则: {0}->年 {1-5}->月日时分秒。
   */
  function formatTime(template) {
    // 不传模板则用默认
    const DEFAULT_TEMPLATE = `{0}年{1}月{2}日 {3}时{4}分{5}秒`;
    template = !template ? DEFAULT_TEMPLATE : template;

    // 先捕获时间字符串里面的年月日信息
    const timeAry = this.match(/\d+/g);

    const result = template.replace(/\{(\d+)\}/g, (...[, $1]) => {
      let time = timeAry[$1] || '00';
      time.length < 2 ? (time = '0' + time) : null;
      return time;
    });
    return result;
  }

  /**
   * 获取url后面的参数信息, 可能包含hash
   * 以键值的形式返回参数信息
   */
  function queryURLParams() {
    const obj = {};
    this.replace(/([^?=&#]+)=([^?=&#]+)/g, (...[, $1, $2]) => (obj[$1] = $2));
    this.replace(/#([^?=&#]+)/g, (...[, $1]) => (obj['HASH'] = $1));
    return obj;
  }

  /**
   * millimeter: 实现大数字的千分符处理
   */
  function millimeter() {
    return this.replace(/\d{1,3}(?=(\d{3})+$)/g, content => `${content},`);
  }

  /**
   * trim 去掉字符串两端的空格
   */
  function trim() {
    return this.replace(/^\s+|\s+$/g, '');
  }

  /**
   * toCamelCase 字符串转成驼峰 支持 - 和 下滑线分割
   */
  function toCamelCase() {
    //return this.replace(/-(\w)/g, (...[, $1]) => $1.toUpperCase());
    return this.replace(/[-\|_](\w)/g, (...[, $1]) => $1.toUpperCase());
  }

  // 扩展多个方法到内置类上
  ['formatTime', 'millimeter', 'trim', 'toCamelCase', 'queryURLParams'].forEach(
    item => {
      String.prototype[item] = eval(item);
    }
  );
})();

let t = null;

t = 'border-bottom-width_two';
console.log(t.toCamelCase());

t = ' dasd ';
console.log(t.trim());

t = '21231231241312312';
console.log(t.millimeter());

t = 'http://www.zhufengpeixun.cn/?lx=1&from=wx#video';
console.log(t.queryURLParams());

t = '2019-12-16 12:30:01';
console.log(t.formatTime());
