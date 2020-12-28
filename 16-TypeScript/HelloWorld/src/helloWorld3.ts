
namespace a {
  class Person {
    name: string = 'fox';
    age: number = 39;
    constructor() {
      // todo srh
    }
  }
}


// 存取器
namespace b {
  class Person {
    _name: string = 'fox';
    get name(){
      return this._name
    }
    set name(v:string){
      this._name = v;
    }
  }
}

// 参数属性
namespace c {
  class Person {
    public name: string = 'foo';
    // get name(){
    //   return this.myName
    // }
    // set name(v:string){
    //   this.myName = v;
    // }
    readonly gender:string = 'man';
  }

  let p = new Person();
  p.name = 'bar';
  //p.gender = 'woman'; // error TS2540: Cannot assign to 'gender' because it is a read-only property.


}

// 继承
namespace d {
  class Person {
    name:string;
    age:number;

    static readonly type_boy: number = 0;
    static readonly type_girl: number = 1;

    constructor(name:string,age:number){
      this.name = name;
      this.age = age;
    }
  }
  class Student extends Person {
    id:number;
    constructor(name:string,age:number,id:number){
      super(name,age);
      this.id = id;
    }
  }
  let p = new Person('foo', 1);
  let s = new Student('bar', 1, 111);

  console.log(Person.type_boy);
}

// 装饰器

namespace e {

  interface Person{
    xx:string;
    yy:string
  }

  function enhancer(target:any){
    target.prototype.xx = 'xx';
    target.prototype.yy = 'yy';
  }

  @enhancer
  class Person{
    constructor(){}
  }
  let p = new Person();
  // 在不改动Person的前提下，为Person加两个属性
  console.log(p.xx);
  console.log(p.yy);

}

let aa:number = 1, bb:number = 2, cc:number = 3;
[aa,bb,cc]=[bb,cc,aa];
console.log(`${aa} ${bb} ${cc}`);