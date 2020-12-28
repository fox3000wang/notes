// es6快速优雅的创建数组
const arr = [...Array(1000).keys()];

// 数据量大以后,需要开辟和释放大量内存性能最差
(() => {
  function sum(arr) {
    let len = arr.length;
    if (len === 0) {
      return 0;
    } else if (len === 1) {
      return arr[0];
    } else {
      return arr[0] + sum(arr.slice(1));
    }
  }
  console.time(`t`);
  sum(arr);
  console.timeEnd(`t`);
})();

(() => {
  function sum(arr) {
    let s = 0;
    for (let i = arr.length - 1; i >= 0; i--) {
      s += arr[i];
    }
    return s;
  }
  console.time(`t`);
  sum(arr);
  console.timeEnd(`t`);
})();

// 性能最好
(() => {
  function sum(arr) {
    return arr.reduce(function (prev, curr, idx, arr) {
      return prev + curr;
    });
  }
  console.time(`t`);
  sum(arr);
  console.timeEnd(`t`);
})();

(() => {
  function sum(arr) {
    var s = 0;
    arr.forEach(function (val, idx, arr) {
      s += val;
    }, 0);

    return s;
  }
  console.time(`t`);
  sum(arr);
  console.timeEnd(`t`);
})();

// 代码量最少,最优雅
(() => {
  function sum(arr) {
    return eval(arr.join('+'));
  }
  console.time(`t`);
  sum(arr);
  console.timeEnd(`t`);
})();
