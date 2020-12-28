# 输入 URL 到显示页面，中间经历了什么？

## 第一步 域名解析

```
https://user:psss@www.jd.com:80/index.html?ll=1&xx=2#video
```

## 第二步 缓存检查

查找 disk cache 中是否有匹配，如有则使用，如没有则发送网络请求

## 第三步：DNS 解析

递归查询 / 迭代查询

## 第四步：TCP 三次握手

核心思想：既要保证数据可靠传输，又要提高传输的效率！

## 第五步：数据传输

## 第六步：TCP 四次挥手

```
Connection:keep-alive
```

## 第七步：页面渲染
