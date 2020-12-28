///////////////////////////////////////////////////////////////////////////////
// 快速排序：
//   通过一趟排序将要排序的数据分割成独立的两部分
//   其中一部分的所有数据比另一部分的所有数据要小
//   再按这种方法对这两部分数据分别进行快速排序
//   整个排序过程可以递归进行，使整个数据变成有序序列
// 实现步骤：
//   选择一个基准元素`target`（一般选择第一个数）
//   将比`target`小的元素移动到数组左边，比`target`大的元素移动到数组右边
//   分别对`target`左侧和右侧的元素进行快速排序
// 复杂度
//   时间复杂度：平均`O(nlogn)`，最坏`O(n2)`，实际上大多数情况下小于`O(nlogn)`
//   空间复杂度:`O(logn)`（递归调用消耗）
// 稳定性
//   不稳定
///////////////////////////////////////////////////////////////////////////////

Array.prototype.quick = function quick() {
  let _this = this;

  // 如果处理的数组只有一项或者空的，则无需处理了
  if (_this.length <= 1) {
    return _this;
  }

  // 获取中间项，并且把中间项在数组中删除
  let middleIndex = Math.floor(_this.length / 2),
    middleValue = _this.splice(middleIndex, 1)[0];

  let arrLeft = [];
  let arrRight = [];
  for (let i = 0; i < _this.length; i++) {
    let item = _this[i];
    item < middleValue ? arrLeft.push(item) : arrRight.push(item);
  }

  return quick.call(arrLeft).concat(middleValue, quick.call(arrRight));
};

console.log([12, 34, 22, 54, 1].quick());

function quickSort(array) {
  if (array.length < 2) {
    return array;
  }
  const target = array[0];
  const left = [];
  const right = [];
  for (let i = 1; i < array.length; i++) {
    if (array[i] < target) {
      left.push(array[i]);
    } else {
      right.push(array[i]);
    }
  }
  return quickSort(left).concat([target], quickSort(right));
}

// 不需要额外存储空间，写法思路稍复杂（有能力推荐这种写法）
function quickSort(array, start, end) {
  if (end - start < 1) {
    return;
  }
  const target = array[start];
  let l = start;
  let r = end;
  while (l < r) {
    while (l < r && array[r] >= target) {
      r--;
    }
    array[l] = array[r];
    while (l < r && array[l] < target) {
      l++;
    }
    array[r] = array[l];
  }
  array[l] = target;
  quickSort(array, start, l - 1);
  quickSort(array, l + 1, end);
  return array;
}
