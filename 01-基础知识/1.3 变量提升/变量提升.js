foo(); // 1
var foo;

function foo() {
  console.log(1);
}

foo = function () {
  console.log(2);
};
foo(); // 2

///////////////////////

// 楼上的代码相当于这样
function foo() {
  console.log(1);
}

foo(); // 1
foo = function () {
  console.log(2);
};

///////////////////////

foo(); // 3
function foo() {
  console.log(1);
}

var foo = function () {
  console.log(2);
};

function foo() {
  console.log(3);
}
foo(); // 2
