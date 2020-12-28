"use strict";
(function () {
    var isGood = true;
    var age = 20;
    var name = 'foo';
    var hobbies = ['a', 'b', 'c'];
    var interests = ['q', 'w', 'e'];
    // 元祖 长度和类型都固定的数组
    var point = ['200', 99];
    // 枚举
    var Gender;
    (function (Gender) {
        Gender[Gender["boy"] = 0] = "boy";
        Gender[Gender["girl"] = 1] = "girl";
        Gender[Gender["goy"] = 2] = "goy";
        Gender[Gender["birl"] = 3] = "birl";
    })(Gender || (Gender = {}));
    console.log(Gender.birl + " " + Gender.girl);
    var Week;
    (function (Week) {
        Week[Week["MON"] = 1] = "MON";
        Week[Week["TUE"] = 2] = "TUE";
    })(Week || (Week = {}));
    // 任意类型 any
    try {
        var root = document.getElementById('root');
        root.style.color = 'red'; // 强行断言不能为空
    }
    catch (e) {
        console.log(e);
    }
    // null undefined
    // 空类型 未定义
    var myName = null;
    // void类型
    function say() {
        console.log('hello world');
    }
    say();
    // never
    function createError(msg) {
        console.log('before');
        throw new Error(msg);
        console.log('after');
    }
    //createError('error');
    // 联合类型
    var data;
    data = 1;
    data = true;
    data = 'haha';
    // 推论类型
    var a = 1; // 语法提示是number
    console.log(typeof a); // number
    var b; // 语法提示是any
    console.log(typeof b); // undefined
    b = 1;
    console.log(typeof b); // number
    // 包装对象
    var isOk1 = true;
    var isOk2 = Boolean(1);
    var another1 = 1;
    //let another2:otherType = 2; //语法检测会报错
    // 输出
    var boy = {
        isGood: isGood, age: age, name: name, hobbies: hobbies, interests: interests, point: point
    };
    console.log(boy);
})();
