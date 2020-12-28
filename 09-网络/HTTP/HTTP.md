# HTTP

## 简介

超文本传输协议
HyperText Transfer Protocol

底层是 TCP/IP 协议

其他几种**传输协议**

- HTTP
- HTTPS
- FTP
- UDP

## 报文

- HTTP 报文：所有客户端和服务器端传输的信息统称为**报文**
  - 请求：客户端传递给服务器
    - 起始行：请求起始行、响应起始行
    - 首部(头)：通用头、请求头、响应头、自定义头信息
  - 响应：服务器返回给客户端信息
  - 主体：请求主体、响应主体

## 头 Headers

- 起始行

  - GET / HTTP1.1
  - 描述报文, 请求方式和协议版本

- 通用头 General

```
Request URL: https://www.bilibili.com/
Request Method: GET
Status Code: 200
Remote Address: 119.3.65.116:443
Referrer Policy: strict-origin-when-cross-origin
```

- 相应头 response heads
  - date 服务器的时间,不是接收到报文的时间
  - content-encoding 压缩方式

```
cache-control: max-age=30
content-encoding: gzip
content-type: text/html; charset=utf-8
date: Fri, 11 Dec 2020 01:18:42 GMT
expires: Fri, 11 Dec 2020 01:19:12 GMT
gear: 1
idc: shjd
support: nantianmen
vary: Origin,Accept-Encoding
x-cache-webcdn: MISS from hw-sh3-webcdn-07
```

- 请求头 request heads

```
:authority: www.bilibili.com
:method: GET
:path: /
:scheme: https
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: zh,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7
cookie: LIVE_BUVID=AUTO9215660213378336; stardustvideo=1; rpdid=|(u~||k~uJl|0J'ulY~l|JJYY;
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: none
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
```

## 主体

服务器

- 服务器返回的信息，主要都是放在相应主体里。
- 只有少部分信息存在头里
- 头部先返回，间隔一段时间，主体才返回

客户端请求

- 一部分是基于请求头传递的
- 还有一部分是基于请求主体(例如:POST 请求方式下的 AJAX/FETCH)，
- 还有一部分也可以直接拼接到 URL 的末尾，基于**问号参数**传递(例如:GET 请求方式下的 AJAX/FETCH)；

## 请求方法

GET(HEAD)

PUT

POST

DELETE

### 不常用

TRACE

OPTIONS

CONNECT

PATCH

## url 编码和解码

```js
console.log(encodeURIComponent('齐天大圣')); // %E9%BD%90%E5%A4%A9%E5%A4%A7%E5%9C%A3

console.log(encodeURI('齐天大圣')); // %E9%BD%90%E5%A4%A9%E5%A4%A7%E5%9C%A3

console.log(decodeURI('%E9%BD%90%E5%A4%A9%E5%A4%A7%E5%9C%A3')); // 齐天大圣
```

## HTTP 事务

每完成一次请求+响应，算一次完整的 HTTP 事务

## 状态码

- 1xx 消息——请求已被服务器接收，继续处理
- 2xx 成功——请求已成功被服务器接收、理解、并接受
- 3xx 重定向——需要后续操作才能完成这一请求
- 4xx 请求错误——请求含有词法错误或者无法被执行
- 5xx 服务器错误——服务器在处理某个正确请求时发生错误

## http 的几个版本

#### HTTP1.0 和 HTTP1.1 的一些区别

**缓存处理** HTTP1.0 中主要使用 Last-Modified，Expires 来做为缓存判断的标准，HTTP1.1 则引入了更多的缓存控制策略：ETag，Cache-Control…

**带宽优化及网络连接的使用** HTTP1.1 支持断点续传，即返回码是 206（Partial Content）

**错误通知的管理** 在 HTTP1.1 中新增了 24 个错误状态响应码，如 409（Conflict）表示请求的资源与资源的当前状态发生冲突；410（Gone）表示服务器上的某个资源被永久性的删除…

**Host 头处理** 在 HTTP1.0 中认为每台服务器都绑定一个唯一的 IP 地址，因此，请求消息中的 URL 并没有传递主机名（hostname）。但随着虚拟主机技术的发展，在一台物理服务器上可以存在多个虚拟主机（Multi-homed Web Servers），并且它们共享一个 IP 地址。HTTP1.1 的请求消息和响应消息都应支持 Host 头域，且请求消息中如果没有 Host 头域会报告一个错误（400 Bad Request）

**长连接** HTTP1.1 中默认开启 Connection： keep-alive，一定程度上弥补了 HTTP1.0 每次请求都要创建连接的缺点

#### HTTP2.0 和 HTTP1.X 相比的新特性

**新的二进制格式(Binary Format)** HTTP1.x 的解析是基于文本，基于文本协议的格式解析存在天然缺陷，文本的表现形式有多样性，要做到健壮性考虑的场景必然很多，二进制则不同，只认 0 和 1 的组合，基于这种考虑 HTTP2.0 的协议解析决定采用二进制格式，实现方便且健壮

**header 压缩** HTTP1.x 的 header 带有大量信息，而且每次都要重复发送，HTTP2.0 使用 encoder 来减少需要传输的 header 大小，通讯双方各自 cache 一份 header fields 表，既避免了重复 header 的传输，又减小了需要传输的大小

**服务端推送(server push)** 例如我的网页有一个 sytle.css 的请求，在客户端收到 sytle.css 数据的同时，服务端会将 sytle.js 的文件推送给客户端，当客户端再次尝试获取 sytle.js 时就可以直接从缓存中获取到，不用再发请求了

```
// 通过在应用生、成 HTTP 响应头信息中设置 Link 命令
Link: </styles.css>; rel=preload; as=style, </example.png>; rel=preload; as=image
```

**多路复用(MultiPlexing)**

- HTTP/1.0 每次请求响应，建立一个 TCP 连接，用完关闭
- HTTP/1.1 「长连接」 若干个请求排队串行化单线程处理，后面的请求等待前面请求的返回才能获得执行机会，一旦有某请求超时等，后续请求只能被阻塞，毫无办法，也就是人们常说的线头阻塞；
- HTTP/2.0 「多路复用」多个请求可同时在一个连接上并行执行，某个请求任务耗时严重，不会影响到其它连接的正常执行；
