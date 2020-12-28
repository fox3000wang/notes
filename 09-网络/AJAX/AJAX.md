# AJAX

## 简介

async javascript and xml 异步的 JS 和 XML

[MDN 文档](https://developer.mozilla.org/zh-CN/docs/Web/Guide/AJAX)

ajax 的核心是 XMLHttpRequest（XHR）

## 基本用法

```js
xhr.open('GET', 'http://127.0.0.1:8888/user/login');
```

监听请求的状态和阶段，获取到服务器返回的信息

- readystate:AJAX 请求状态
  - 0:UNSENT 最开始
  - 1:OPENED 已经执行 open 方法了
  - 2:HEADERS_RECEIVED 服务器已经返回了响应头信息
  - 3:LOADING 响应主体信息正在处理和返回
  - 4:DONE 响应主体信息已经获取，此时证明 AJAX 请求结束了
- 服务器返回的 HTTP 状态码
  - 200:OK 成功
  - ...

## AJAX 和 axios 的区别

axios 是通过 Promise 实现对 ajax 技术的一种封装
