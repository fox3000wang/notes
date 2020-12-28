"use strict";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var _a;
var a;
(function (a) {
    var Person = /** @class */ (function () {
        function Person() {
            this.name = 'fox';
            this.age = 39;
            // todo srh
        }
        return Person;
    }());
})(a || (a = {}));
// 存取器
var b;
(function (b) {
    var Person = /** @class */ (function () {
        function Person() {
            this._name = 'fox';
        }
        Object.defineProperty(Person.prototype, "name", {
            get: function () {
                return this._name;
            },
            set: function (v) {
                this._name = v;
            },
            enumerable: false,
            configurable: true
        });
        return Person;
    }());
})(b || (b = {}));
// 参数属性
var c;
(function (c) {
    var Person = /** @class */ (function () {
        function Person() {
            this.name = 'foo';
            // get name(){
            //   return this.myName
            // }
            // set name(v:string){
            //   this.myName = v;
            // }
            this.gender = 'man';
        }
        return Person;
    }());
    var p = new Person();
    p.name = 'bar';
    //p.gender = 'woman'; // error TS2540: Cannot assign to 'gender' because it is a read-only property.
})(c || (c = {}));
// 继承
var d;
(function (d) {
    var Person = /** @class */ (function () {
        function Person(name, age) {
            this.name = name;
            this.age = age;
        }
        Person.type_boy = 0;
        Person.type_girl = 1;
        return Person;
    }());
    var Student = /** @class */ (function (_super) {
        __extends(Student, _super);
        function Student(name, age, id) {
            var _this = _super.call(this, name, age) || this;
            _this.id = id;
            return _this;
        }
        return Student;
    }(Person));
    var p = new Person('foo', 1);
    var s = new Student('bar', 1, 111);
    console.log(Person.type_boy);
})(d || (d = {}));
// 装饰器
var e;
(function (e) {
    function enhancer(target) {
        target.prototype.xx = 'xx';
        target.prototype.yy = 'yy';
    }
    var Person = /** @class */ (function () {
        function Person() {
        }
        Person = __decorate([
            enhancer
        ], Person);
        return Person;
    }());
    var p = new Person();
    // 在不改动Person的前提下，为Person加两个属性
    console.log(p.xx);
    console.log(p.yy);
})(e || (e = {}));
var aa = 1, bb = 2, cc = 3;
_a = [bb, cc, aa], aa = _a[0], bb = _a[1], cc = _a[2];
console.log(aa + " " + bb + " " + cc);
