"use strict";
// 函数表达式
var getUserName = function (firstName, lastName) {
};
// 可选参数
function print(name, age, isMeil) {
    // 只能传0个或者3个
}
function print(name, age, isMeil) {
    // 只能传0个到3个
}
// 剩余参数
function sum() {
    var number = [];
    for (var _i = 0; _i < arguments.length; _i++) {
        number[_i] = arguments[_i];
    }
    return number.reduce(function (t, i) { return t + i; }, 0);
}
function attr(val) {
    console.log(typeof val == 'number' ? 'number' : 'string');
}
function absum(a, b) {
    return eval(a + "+" + b);
}
console.log(absum(1, 2));
console.log(absum('1', '2'));
