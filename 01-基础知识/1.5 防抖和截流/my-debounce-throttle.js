/*
 * 函数的防抖（debounce）和节流（throttle）
 *   在“高频”触发的场景下，需要进行防抖和节流
 *     + 狂点一个按钮
 *     + 页面滚动
 *     + 输入模糊匹配
 *     + ...
 *   我们自己设定，多长的时间内，触发两次及以上就算“高频”：封装方法的时候需要指定这个频率（可以设置默认值）
 *  「防抖」在某一次高频触发下，我们只识别一次（可以控制开始触发，还是最后一次触发）；详细：假设我们规定500MS触发多次算是高频，只要我们检测到是高频触发了，则在本次频繁操作下（哪怕你操作了10min）也是只触发一次...
 *  「节流」在某一次高频触发下，我们不是只识别一次，按照我们设定的间隔时间（自己规定的频率），没到达这个频率都会触发一次；详细：假设我们规定频率是500MS，我们操作了10min，触发的次数=(10*60*1000)/500
 */

// function debounce(func, wait = 500, immediate = false) {  // bad
function debounce(func, wait, immediate) {
  // 多个参数及传递默认的处理
  if (typeof func !== 'function') {
    throw new TypeError('func must be an function!');
  }
  if (typeof wait === 'undefined') {
    wait = 500;
  }
  if (typeof wait === 'boolean') {
    immediate = wait;
    wait = 500;
  }
  if (typeof immediate !== 'boolean') {
    immediate = false;
  }
  console.log(
    `[debounce] func = ${func} wait = ${wait} immediate = ${immediate}`
  );

  // 设定定时器返回值标识
  let timer = null;
  return function proxy(...params) {
    console.log(`[proxy] ${params}`);
    let self = this;
    let now = immediate && !timer;

    clearTimeout(timer); // 每次进到函数都把计数器清零，直到手抖结束
    timer = setTimeout(function () {
      timer = null;
      !immediate ? func.call(self, ...params) : null;
    }, wait);

    // 第一次触发就立即执行
    now ? func.call(self, ...params) : null;
  };
}

function throttle(func, wait) {
  if (typeof func !== 'function') {
    throw new TypeError('func must be an function!');
  }
  if (typeof wait === 'undefined') {
    wait = 500;
  }

  let timer = null;
  let previous = 0; //记录上一次操作的时间
  console.log(`[throttle] func = ${func} wait = ${wait}`);

  return function proxy(...params) {
    const self = this;
    const now = new Date(); //当前这次触发操作的时间
    const remaining = wait - (now - previous);

    if (remaining <= 0) {
      // 两次间隔时间超过wait了，直接执行即可
      clearTimeout(timer);
      timer = null;
      previous = now;
      func.call(self, ...params);
    } else if (!timer) {
      // 两次触发的间隔时间没有超过wait，则设置定时器，让其等待remaining这么久之后执行一次「前提：没有设置过定时器」
      timer = setTimeout(function () {
        clearTimeout(timer);
        timer = null;
        previous = new Date();
        func.call(self, ...params);
      }, remaining);
    }
  };
}
