///////////////////////////////////////////////////////////////////////////////
// 思路 ：
//     1. 利用set的唯一的特性
//     2. 利用{}的key的唯一性,其实和楼上差不多,还比楼上麻烦
//     3. 正则
//     4. 人工方式: 制成null然后再去掉啊，双for循环 主要用splice，还要避免数组塌陷的坑
///////////////////////////////////////////////////////////////////////////////

let ary = [12, 21, 12, 21, 3, 5, 7, 100, 100, 100];

// 用...展开
let arr = [...new Set(ary)];
console.log(arr);

// 利用 Array.from
let arr2 = Array.from(new Set(ary));
console.log(arr2);

// 双for循环 主要用splice
function remove1(arg) {
  let arr = JSON.parse(JSON.stringify(arg));
  for (let i = 0; i < arr.length; i++) {
    let item = arr[i];
    for (let j = i + 1; j < arr.length; j++) {
      if (item === arr[j]) {
        arr.splice(j, 1);
        j--;
      }
    }
  }
  return arr;
}
console.log(remove1(arr));

// 1次遍历 主要用index splice
function remove2(arg) {
  let arr = JSON.parse(JSON.stringify(arg));
  for (let i = 0; i < arr.length; i++) {
    let item = arr[i];
    let args = arr.splice(i + 1);
    if (args.indexOf(item) > -1) {
      arr.splice(i, 1);
      i--;
    }
  }
  return arr;
}
console.log(remove1(arr));

/* 不删除，而是设置成null 最后清理*/

/* 不删除，把最后一项填到当前位置 */

/* 对象键值对 */

// 正则
ary.sort((a, b) => a - b);
ary = ary.join('@') + '@';
const reg = /(\d+@)\1*/g;
const result = [];
ary.replace(reg, (val, $1) => {
  result.push(parseFloat($1));
});
console.log(result);
