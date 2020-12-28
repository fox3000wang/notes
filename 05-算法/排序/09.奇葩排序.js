// 睡眠排序
[4, 2, 7, 5, 6, 0, 8].forEach(val => {
  setTimeout(() => {
    console.log(val);
  }, val);
});

// 猴子排序
function bogoSort(arr) {
  var n = 0,
    ordered = false;

  function shuffle(array) {
    for (var i = 0, length = arr.length; i < length; i++) {
      var j = Math.floor(Math.random() * length);
      [arr[i], arr[j]] = [arr[j], arr[i]];
      n++;
    }
  }

  function isOrdered(array) {
    for (var i = 1, length = arr.length; i < length; i++) {
      if (arr[i] < arr[i - 1]) {
        return false;
      }
    }
    return true;
  }

  while (ordered == false) {
    // 效率低下的位置
    v = shuffle(arr);
    ordered = isOrdered(arr);
  }
  console.log('计算了' + n + '次');
  return arr;
}
