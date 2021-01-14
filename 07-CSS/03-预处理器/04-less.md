# less

官网：http://lesscss.org/

https://less.bootcss.com/

### 编译

#### webpack 中

loader

#### node

watcher-less

#### 浏览器中

```js
<link rel="stylesheet/less" type="text/css" href="styles.less" />
<script src="//cdnjs.cloudflare.com/ajax/libs/less.js/3.11.1/less.min.js" ></script>
```

#### 考拉

http://koala-app.com/index-zh.html

#### vscode

插件：easy less

### 语法

#### variables 变量

```less
// 选择器调用
@my-selector: banner;
.@{my-selector} {
  margin: 0 auto;
}

// 路径调用
@images: '../img';
body {
  background: url('@{images}/five.jpg');
}

// 属性调用
@property: color;
.widget {
  background-@{property}: #999;
}

// 变量调用变量
@primary: green;
@secondary: blue;
.section {
  @color: primary;
  .element {
    color: @@color;
  }
}
// css
.section .element {
  color: #008000;
}

// 属性名做变量调用
.block {
  color: red;
  .inner {
    background-color: $color;
  }
  color: blue;
}
```

#### mixin 混合

```less
// !important
.foo (@bg: #f5f5f5, @color: #900) {
  background: @bg;
  color: @color;
}

.unimportant {
  .foo();
}

.important {
  .foo() !important;
}

// css
.unimportant {
  background: #f5f5f5;
  color: #990000;
}
.important {
  background: #f5f5f5 !important;
  color: #990000 !important;
}
```

```less
// 带参数的Mixins
.border-radius(@radius) {
  -webkit-border-radius: @radius;
  -moz-border-radius: @radius;
  border-radius: @radius;
}

#header {
  .border-radius(4px);
}

.button {
  .border-radius(6px);
}

// Using Mixins as Functions
.average(@x, @y) {
  @result: ((@x + @y) / 2);
}

div {
  padding: .average(16px, 50px) [ @result];
}
```

#### extend 扩展/继承

```less
@w: 200px;
@h: 200px;

.block {
  width: @w;
  height: @h;
  border: 10px solid #ccc;
}
.box1 {
  &:extend(.block);
  background: red;
}

.box2:extend(.block) {
  background: green;
}
```

#### nesting 嵌套

```less
// @规则嵌套和冒泡
.component {
  width: 300px;

  @media (min-width: 768px) {
    width: 600px;

    @media (min-resolution: 192dpi) {
      background-image: url(/img/retina2x.png);
    }
  }

  @media (min-width: 1280px) {
    width: 800px;
  }
}

// css
.component {
  width: 300px;
}
@media (min-width: 768px) {
  .component {
    width: 600px;
  }
}
@media (min-width: 768px) and (min-resolution: 192dpi) {
  .component {
    background-image: url(/img/retina2x.png);
  }
}
@media (min-width: 1280px) {
  .component {
    width: 800px;
  }
}
```

#### Scope 作用域

#### loop 循环

#### import 导入
