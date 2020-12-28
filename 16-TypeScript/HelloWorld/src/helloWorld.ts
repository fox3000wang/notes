
(() => {
    
  let isGood:boolean = true;
  let age:number = 20;
  let name :string = 'foo';
  let hobbies: string[] = ['a','b','c'];
  let interests: Array<string> = ['q','w','e'];
  
  // 元祖 长度和类型都固定的数组
  let point:[string,number] = ['200',99];

  // 枚举
  enum Gender {
    boy,girl,goy,birl
  }
  console.log(`${Gender.birl} ${Gender.girl}`);
  enum Week {
    MON = 1,
    TUE = 2
  }

  // 任意类型 any
  try{
    let root: HTMLElement | null = document.getElementById('root');
    root!.style.color = 'red'; // 强行断言不能为空
  }catch(e){
    console.log(e);
  }
  
  // null undefined
  // 空类型 未定义
  let myName = null;

  // void类型
  function say():void{
    console.log('hello world');
  }
  say();

  // never
  function createError(msg:string):never{
    console.log('before');
    throw new Error(msg);
    console.log('after');
  }
  //createError('error');

  // 联合类型
  let data: boolean | number | string;
  data = 1;
  data = true;
  data = 'haha';

  // 推论类型
  let a = 1; // 语法提示是number
  console.log(typeof a); // number

  let b; // 语法提示是any
  console.log(typeof b); // undefined
  b = 1;
  console.log(typeof b); // number

  // 包装对象
  let isOk1:boolean = true;
  let isOk2:boolean = Boolean(1);
  //let isOk3:boolean = new Boolean(1); //语法会报错

  // 字面量类型
  type otherType = 1 | 'other' | false;
  let another1:otherType = 1;
  //let another2:otherType = 2; //语法检测会报错
  

  // 输出
  const boy:object = {
    isGood,age,name,hobbies,interests,point
  }
  
  console.log(boy);

})();