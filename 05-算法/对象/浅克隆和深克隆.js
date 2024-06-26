var class2type = {};
var hasOwn = class2type.hasOwnProperty;
var fnToString = hasOwn.toString;
[
  'Boolean',
  'Number',
  'String',
  'Symbol',
  'Function',
  'Array',
  'Date',
  'RegExp',
  'Object',
  'Error',
].forEach(function (name) {
  class2type['[object ' + name + ']'] = name.toLowerCase();
});

//console.log(class2type);

function toType(obj) {
  return null === obj
    ? `${obj}`
    : typeof obj === 'object' || typeof obj === 'function'
    ? class2type[toString.call(obj)] || 'object'
    : typeof obj;
}

function shallowClone(obj) {
  // 处理其它类型的值克隆
  let type = toType(obj);
  if (/^(number|string|boolean|null|undefiend|symbol|bigint)$/.test(type))
    return obj;
  if (/^function$/.test(type)) {
    // 返回一个不同的函数，但是最后执行的效果和原始函数一致
    return function proxy() {
      return obj();
    };
  }
  if (/^(regexp|date)$/.test(type)) return new obj.constructor(obj);
  if (/^error$/.test(type)) return new obj.constructor(obj.message);

  // 只处理数组(最后返回的是数组)和对象(普通对象/类数组对象等->最后返回的都是普通对象)
  let keys = getOwnPropertys(obj),
    clone = {};
  Array.isArray(obj) ? (clone = []) : null;
  keys.forEach(key => {
    clone[key] = obj[key];
  });
  return clone;
}

// 深克隆
function deepClone(obj, cache = new Set()) {
  // 只有数组和对象我们再处理深克隆，其余的情况直接按照浅克隆处理即可
  let type = toType(obj);
  if (!/^(array|object)$/.test(type)) return shallowClone(obj);

  // 避免自己套用自己导致的无限递归
  if (cache.has(obj)) return shallowClone(obj);
  cache.add(obj);

  let keys = getOwnPropertys(obj),
    clone = {};
  type === 'array' ? (clone = []) : null;
  keys.forEach(key => {
    clone[key] = deepClone(obj[key], cache);
  });
  return clone;
}
