///////////////////////////////////////////////////////////////////////////////
// 将左侧序列看成一个有序序列，每次将一个数字插入该有序序列。
// 插入时，从有序序列最右侧开始比较，若比较的数较大，后移一位。
// 复杂度
//   时间复杂度：`O(n2)`
//   空间复杂度:`O(1)`
// 稳定性
//   稳定
///////////////////////////////////////////////////////////////////////////////

Array.prototype.insert = function insert() {
  // 先取出一张牌放到手里
  let _this = this;
  let hanlde = [];
  hanlde.push(_this[0]);

  // 开始抓牌
  for (let i = 1; i < _this.length; i++) {
    // A每一次新抓的牌
    let A = _this[i];
    // 和手里的牌进行比较（倒着比较）
    for (let j = hanlde.length - 1; j >= 0; j--) {
      // 要比较的手里这张牌
      let B = hanlde[j];
      // 新抓的牌A比B要大，则放在B的后面
      if (A > B) {
        hanlde.splice(j + 1, 0, A);
        break; //=>没必要和手里的牌继续比较了
      }
      // 都比到最开始，A都没有比任何的牌大，则A是最小的，插入到开始
      if (j === 0) {
        hanlde.unshift(A);
      }
    }
  }
  return hanlde;
};

console.log([12, 8, 24, 16, 1].insert());

// 传参方式
function insertSort(array) {
  for (let i = 1; i < array.length; i++) {
    let target = i;
    for (let j = i - 1; j >= 0; j--) {
      if (array[target] < array[j]) {
        [array[target], array[j]] = [array[j], array[target]];
        target = j;
      } else {
        break;
      }
    }
  }
  return array;
}

console.log(insertSort([12, 8, 24, 16, 1]));

// TODO: 自己练习
