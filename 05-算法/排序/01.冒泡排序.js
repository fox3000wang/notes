///////////////////////////////////////////////////////////////////////////////
// 循环数组，比较当前元素和下一个元素，如果当前元素比下一个元素大，向上冒泡。
// 这样一次循环之后最后一个数就是本数组最大的数。
// 下一次循环继续上面的操作，不循环已经排序好的数。
// 优化：当一次循环没有发生冒泡，说明已经排序完成，停止循环。
// 复杂度
//   时间复杂度：`O(n2)`
//   空间复杂度:`O(1)`
// 稳定性
//   稳定
///////////////////////////////////////////////////////////////////////////////

Array.prototype.bubble = function bubble() {
  function swap(arr, i, j) {
    let temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
    return arr;
  }

  const _this = this;
  const flag = false;

  // 控制循环多少轮
  for (let i = 0; i < _this.length - 1; i++) {
    // 控制每一轮循环多少次
    for (let j = 0; j < _this.length - 1 - i; j++) {
      // 交换位置
      if (_this[j] > _this[j + 1]) {
        swap(_this, j, j + 1);
        flag = true;
      }
    }
    if (!flag) break;
    flag = false;
  }
  return _this;
};

console.log([12, 8, 24, 16, 1].bubble());

// 传参方式
function bubbleSort(array) {
  for (let j = 0; j < array.length; j++) {
    let complete = true;
    for (let i = 0; i < array.length - 1 - j; i++) {
      // 比较相邻数
      if (array[i] > array[i + 1]) {
        [array[i], array[i + 1]] = [array[i + 1], array[i]];
        complete = false;
      }
    }
    // 如果冒泡一轮都没有需要交换的, 说明排序结束
    if (complete) break;
  }
  return array;
}
console.log(bubbleSort([12, 8, 24, 16, 1]));

// TODO: 自己练习
