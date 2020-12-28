# Math

## 常用方法

- Math.PI / Math['PI'] ：获取圆周率
- Math.abs([N])：获取数字 N 的绝对值（绝对值都是正数）
- Math.ceil([N]) / Math.floor([N])：把数字 N 向上或者向下取整
- Math.round([N])：把数字 N 四舍五入（结果是整数）
- Math.max(N1,N2,...) / Math.min(N1,N2,...)：获取一堆数值中的最大值和最小值
- Math.pow([N],[m])：获取数字 N 的 m 次幂（多少次方）
- Matn.sqrt([N])：给数字 N 开平方
- Math.random()：获取 0~1 之间的随机小数（每一次获取的结果是不一样的）
- 获取[N,M]之间的随机整数（包含 N 和 M）：Math.round(Math.random()\*(m-n)+n)

```js
// 圆周率
console.log(Math.PI); // 3.141592653589793

// 绝对值
console.log(Math.abs(-1)); // 1

// 向上取整 ceiling是天花板
console.log(Math.ceil(1.1)); // 2

// 向下取整 floor是地板
console.log(Math.ceil(1.9)); // 1

// 四舍五入
console.log(Math.round(1.4)); // 1
console.log(Math.round(1.5)); // 2

// 取最大值
console.log(Math.max(1, 3, 9, 2, 5)); // 9

// 取最小值
console.log(Math.min(1, 3, 9, 2, 5)); // 1

// 获取数字N的m次幂
console.log(Math.pow(2, 10)); // 1024

// N开平方, 并不是开N的m次方
console.log(Math.sqrt(1024, 2)); // 32
console.log(Math.sqrt(1024, 10)); // 32

// 取0-1之间的随机数
console.log(Math.random());
console.log(Math.random());

// 取n-m之间的一个随机整数
const result = [];
for (let i = 0; i < 100; i++) {
  result.push(Math.round(Math.random() * 4 + (8 - 4)));
}
console.log(result);
// [
//   5, 6, 6, 7, 5, 7, 6, 5, 7, 4, 6, 6,
//   6, 5, 4, 6, 5, 8, 8, 5, 7, 5, 6, 5,
//   5, 8, 5, 4, 5, 6, 8, 8, 7, 7, 5, 8,
//   7, 6, 6, 8, 7, 5, 5, 4, 6, 5, 5, 5,
//   5, 7, 5, 7, 8, 8, 6, 7, 8, 5, 6, 8,
//   5, 4, 5, 5, 4, 6, 8, 8, 7, 7, 5, 5,
//   5, 4, 6, 6, 4, 8, 5, 5, 5, 5, 7, 4,
//   5, 8, 5, 6, 5, 4, 7, 6, 7, 5, 7, 6,
//   4, 5, 6, 7
// ]
```
