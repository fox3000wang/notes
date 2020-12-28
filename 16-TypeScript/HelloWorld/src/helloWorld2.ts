


// type 定义一个类型或者类型的别名
type GetNameType = (firstName:string, lastName:string) => void

// 函数表达式
let getUserName : GetNameType = function(firstName:string, lastName:string): void{

}

// 可选参数
function print(name:string, age:number, isMeil:boolean):void{
  // 只能传0个或者3个
}

function print(name:string, age?:number, isMeil?:boolean):void{
  // 只能传0个到3个
}

// 剩余参数
function sum(...number:Array<number>){
  return number.reduce((t,i) => t + i, 0);
}

// 函数重载
function attr(val:number):void;
function attr(val:string):void;
function attr(val:any):void{
  console.log(typeof val == 'number' ? 'number' : 'string');
} 

function absum(a:number, b:number):number;
function absum(a:string, b:string):number;
function absum(a:any, b:any):number{
  return eval(`${a}+${b}`);
}
console.log(absum(1,2));
console.log(absum('1','2'));