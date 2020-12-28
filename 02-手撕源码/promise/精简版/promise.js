// https://mp.weixin.qq.com/s?__biz=MzI1NTcxOTQ1Nw==&mid=2247490351&idx=1&sn=9cb2d450c954281f33953d7661ecb798&chksm=ea30fa61dd477377925810c3c60f7b9b763537d8a4107ab97eadf00192be82fd19c9a1d0daa8&scene=27

/**
 * 在面试的时候，经常会有面试官让你实现一个 Promise，
 * 如果参照 A+规范来实现的话，可能面到天黑都结束不了。
 * 说到 Promise，我们首先想到的最核心的功能就是异步链式调用，
 * 本篇文章就带你用 20 行代码实现一个可以异步链式调用的 Promise。
 * 这个 Promise 的实现不考虑任何异常情况，只考虑代码最简短，
 * 从而便于读者理解核心的异步链式调用原理。
 */

function Promise(fn) {
  this.cbs = [];

  const resolve = value => {
    setTimeout(() => {
      this.data = value;
      this.cbs.forEach(cb => cb(value));
    });
  };

  fn(resolve.bind(this));
}

Promise.prototype.then = function (onResolved) {
  return new Promise(resolve => {
    this.cbs.push(() => {
      const res = onResolved(this.data);
      if (res instanceof Promise) {
        res.then(resolve);
      } else {
        resolve(res);
      }
    });
  });
};
