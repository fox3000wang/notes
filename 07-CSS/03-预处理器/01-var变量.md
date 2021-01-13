# 变量

### 定义

--变量名称（自定义）
参数 - 2 个参数，第 2 个备用参数
参数 - 缺省性（属性名 和 属性值 不匹配） 第 2 个失效 走的其实是元素天生默认自带样式

属性名不能用变量，变量末尾尾部是有空格的

```css
/* 全局变量  */
:root {
  --bg: red;
}

/* 局部变量 */
p {
  --bg: green;
}
```

### 调用

var(--名称)

```css
div {
  blackground: var(--bg);
}
```

#### 带单位的情况

```css
span {
  --txt: 20;
  width: calc(var(--txt) * 1px);
}
```

### 变量符号:

原生 css 变量: --
less 变量 @
sass 变量 $

# 响应式匹配方案

```html
<div class="wrap">
  <div class="item"></div>
  <div class="item"></div>
  <div class="item"></div>
  <div class="item"></div>
</div>
```

- pc 4 个模块
- pad 2 个模块
- 手机 1 个模块

### 通用方案

```css
* {
  margin: 0;
  padding: 0;
}

.wrap {
  overflow: hidden;
}
.item {
  /* 100 / 列数  width:100% / column  */
  float: left;
  width: 25%;
  height: 300px;
  margin-bottom: 20px;
}
.item:nth-of-type(2n + 1) {
  background-color: rebeccapurple;
}
.item:nth-of-type(2n) {
  background-color: red;
}
/* <= 1080 适配pad端 */
@media screen and (max-width: 1080px) {
  .item {
    width: 50%;
  }
}
/* <= 640 适配手机端 */
@media screen and (max-width: 640px) {
  .item {
    width: 100%;
  }
}
```

### 变量方案

```css
* {
  margin: 0;
  padding: 0;
}

:root {
  --column: 4;
}

.wrap {
  overflow: hidden;
}

.item {
  /* calc(100%/4)  calc(% - px)*/
  float: left;
  width: calc(100% / var(--column));
  height: 300px;
  margin-bottom: 20px;
}

.item:nth-of-type(2n + 1) {
  background-color: rebeccapurple;
}

.item:nth-of-type(2n) {
  background-color: red;
}

/* <= 1080 适配pad端 */
@media screen and (max-width: 1080px) {
  :root {
    --column: 2;
  }
}

/* <= 640 适配手机端 */
@media screen and (max-width: 640px) {
  :root {
    --column: 1;
  }
}
```
