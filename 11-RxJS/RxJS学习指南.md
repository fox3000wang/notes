# RxJS 学习指南

https://fe.rualc.com/note/rxjs.html#rxjs-jian-jie

什么是 ReactiveX
ReactiveX 是一套采用响应式流的异步编程模式，
具体实现包括 RxJS、RxJava、RxSwift 等，
虽然这些实现的语言不同，但是核心思想和 API 都是相同的。
这个相同的部分就称之为 ReactiveX。

它能将离散的多个事件视为一个流来操控，

将事件/数据作为流传播，
流可以（通过操作符）进行各种变换（映射、采样、合并等）

# 什么是 RxJS

ReactiveX 的 JS 具体实现

它相当于事件版的 Lodash

# 为什么要用 RxJS

能用更少和清晰的代码完成异步业务

## 学习 RxJS #概览

- 耗时：从入门到熟悉需要大约 15~30 小时（个人估计）
- 难点：
  - 理解 Stream 范式
  - 熟悉 API 全貌并综合运用
- 工具：
  - rxjs@6+
  - webpack/parcel/cli

## RxJS 知识体系

- [Ob 相关]
  - Observable: 可被观测的/数据流序列（很多创建方式，如 timer、fromEvent 等）
  - operator: 操作符（对事件流进行形变，比如 map、merge 等）
- [Sub 相关]
  - subscribe: 订阅方法（Observable 提供的）
    - Observer: 观察者/消费者方法集合（业务方法，传给 subscribe() 的）
  - Subscription: 订阅关系（subscribe 返回的）
    - unsubscribe: 结束订阅方法（Subscription 提供的）
- Subject: 多播的 Observable（可以作为 Observable 和 Subscription 的中间层）
- Scheduler：调度器

- Cold VS Hot Observable
  - Cold：多次订阅产生多个独立的事件流（用途例如：interval）
  - Hot：多次订阅共享同一个事件流（用途例如：fromEvent、Subject）
