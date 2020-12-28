# DOM 操作

## DOM 简介

document object model 文档对象模型

提供一系列的属性和方法，让我们能操作页面中的 DOM 元素->简单理解为操作页面中的 HTML 标签

## 获取 DOM 元素

基于元素的 ID 获取到这个元素（一个元素对象)

```js
document.getElementById([ID]);
```

根据元素的 NAME 属性值，在整个文档中获取一组元素集合

```js
document.getElementsByName([NAME])：
```

根据标签名获取到页面中（指定容器中）所有的元素标签集合 （一组元素集合)

```js
document.getElementsByTagName([标签名]);
```

在指定上下文中，基于样式类名获取对应的元素集合
不兼容 IE6~8 低版本浏览器

```js
[context].getElementsByClassName([样式类名]);
```

获取页面中的 BODY 元素
获取整个 HEAD 元素对象

```js
document.body;
document.head;
```

不兼容 IE6~8 低版本浏览器，可以根据选择器（类似于 CSS 选择器）快速获取元素和元素集合的办法：

```js
[context].querySelector([SELECTOR]) 获取一个元素对象
[context].querySelectorAll([SELECTOR]) 获取一组元素集合
```

在不考虑兼容的情况下，这两个方法就足以获取我们需要的元素对象和元素集合了

## 获取 DOM 节点的属性和方法

我们认为在页面中所有呈现的内容，都是 DOM 文档中的一个节点（node），例如：元素标签是元素节点、注释的内容是注释节点、文本内容是文本节点、document 是文档节点

## DOM 元素中的增加/删除/修改

- document.createElement([标签名])：动态创建一个 DOM 元素
- [CONTAINER].appendChild([元素])：把元素动态插入到指定容器的末尾
- [CONTAINER].insertBefore([新元素],[原始页面中的元素])：把新创建的元素放置到指定容器原始页面元素的前面 [原始页面中的元素]肯定在[CONTAINER]容器中
- [CONTAINER].removeChild([元素])：在指定容器中移除元素
- document.createTextNode()：创建一个文本节点

## 4.修改 DOM 元素的样式

- 元素.style.xxx ：修改（获取）当前元素的行内样式
  - 操作的都是行内样式，哪怕把样式写在样式表中，只要没有写在行内上，也获取不到
- 元素.className：操作的是当前元素的样式类，基于样式类的管理给予其不同的样式

## 5.给 DOM 元素设置内容

- innerHTML / innerText：给非表单元素设置或者操作其内容
- value：操作表单元素的内容
