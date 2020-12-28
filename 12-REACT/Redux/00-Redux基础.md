# Redux 基础

https://fe.rualc.com/note/redux.html#redux-jian-jie

## 简介

什么是 Redux
Redux 一种用于 JS 应用的状态管理工具。可以直接使用，也可以借助响应式编程的范式，搭配视图层（比如 React）或其他逻辑。

Redux 的诞生：redux == reducer 方法 + flux 架构

所以它的核心理念是：纯函数 + 单向数据流

#### 为什么要用 Redux

使用数据驱动的编程模型
当你要做一个大型应用，想要拆分数据逻辑和视图层的代码
（并且你用的是 React）
这时候你可以使用 Redux 集中管理应用的数据

## 学习 Redux

- 耗时：
  - 从入门到熟悉 Redux 模式，15~40 小时
  - 简单了解 Redux 衍生生态需要，2~5 小时
  - 练习 Redux + React，2~5 小时
- 难点：
  - 理解 FP 和 Redux 理念
  - 设计出合理的数据结构和数据流
  - 探索不同业务下的设计，全局状态和局部状态如何管理和划分
- 工具：
  - redux
  - react-redux
  - redux-react-hook
  - webpack/parcel/cli

## Redux 知识体系

### Redux 的三个原则

- 整个 App 只有一个 Store（便于维护和实施）
- State （本身）是只读的
- 变更只通过 Dispatch(Action) 替换旧的 State 完成
  Reducer 是纯函数
