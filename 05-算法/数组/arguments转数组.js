// arguments toArray 我要打十个专题

// 方案0 土法 遍历大法
function toArray() {
  let arg = [];
  for (let i = 0; i < arguments.length; i++) {
    arg.push(arguments[i]);
  }
  return arg;
}

// 方案1 利用数组特性
function toArray() {
  return [...arguments];
}

// 方案2 利用数组特性 和1是差不多的
function toArray() {
  return Array.from(arguments);
}

// 方案3 利用迭代器
function toArray() {
  const arg = [];
  const iterator = arguments[Symbol.iterator]();
  while (arguments.length > arg.length) {
    arg.push(iterator.next().value);
  }
  return arg;
}

// 方案4 利用Array的slice, Array.prototype.slice.call()能把类数组对象转化成数组
function toArray() {
  return Array.prototype.slice.call(arguments);
}

// 方案5 直接展开, 不用arguments
function toArray(...arg) {
  return arg;
}

// 方案6 arguments stringify以后, 正则匹配去掉一些, 然后再JSON.parse回来
//  '{"0":"A","1":10,"2":20,"3":30}' => '["A",10,20,30]' => Array
function toArray() {
  return JSON.parse(
    `[${JSON.stringify(arguments).replace(/("\d+":)|{|}/g, '')}]`
  );
}

// 方案7 arguments stringify以后, 用正则匹配到需要的值, 然后一个一个push到数组返回
// 缺点就是塞回去的时候,字符和数字需要稍微处理一下
function toArray() {
  const ary = [];
  let argStr = JSON.stringify(arguments);
  argStr.replace(/:("?\w+"?)(,|})/g, (e, $1) => {
    ary.push(/\d+/.test($1) ? parseFloat($1) : $1.replace(/"/g, ''));
  });
  return ary;
}

// 方案8 stringify以后, 用正则, 把这条string改写成 可以执行的js语句, 然后利用eval执行返回
// '{"0":"A","1":10,"2":20,"3":30}' => ary[0]="A";ary[1]=10;ary[2]=20;ary[3]=30 => eval()
function toArray() {
  const ary = [];
  let argStr = JSON.stringify(arguments)
    .replace(/{|}/g, '')
    .replace(/,/g, ';')
    .replace(/:/g, '=')
    .replace(/"(\d+)"=/g, (...[, $1]) => `ary[${$1}]=`);
  eval(argStr);
  return ary;
}
console.log(toArray('A', 10, 20, 30)); //=>['A',10,20,30]

// 方案9 最佳的方案,在你心中
