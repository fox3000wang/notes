# Redux DevTools 扩展的使用说明

> 原文：[github.com/zalmoxisus/…](https://github.com/zalmoxisus/redux-devtools-extension#usage)

## 安装

---

### 1. Chrome、Firefox

- 可以在浏览器网上商店中下载安装该扩展

### 2. 其它浏览器和非浏览器环境

- 使用[remote-redux-devtools](https://github.com/zalmoxisus/remote-redux-devtools)

## 用法

---

> 注意，从 2.7 开始，`window.devToolsExtension`重命名为`window.__REDUX_DEVTOOLS_EXTENSION__`/ `window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__`.

### 使用 Redux

1. store 普通用法 对于基础的 redux store 只加添加：

   ```
    const store = createStore(
      reducer, /* preloadedState, */
   +  window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
    );
   复制代码
   ```

   注：`preloadedState`在`createStore`中是可选的

   > 对于通用（“同构”）应用程序，请在其前面加上`typeof window !== 'undefined' &&`。

   出现 ESLint 报错时，可以如下配置：

   ```
   + /* eslint-disable no-underscore-dangle */
     const store = createStore(
      reducer, /* preloadedState, */
      window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
     );
   + /* eslint-enable */
   复制代码
   ```

   > 支持 redux>=3.1.0 版本

2. store 高级用法 如果 store 使用了中间件`middleware`和增强器`enhaners`，代码要修改下：

   ```
   import { createStore, applyMiddleware, compose } from 'redux';

   const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

   const store = createStore(
       reducer, /* preloadedState, */
       composeEnhancers(
           applyMiddleware(...middleware)
     ));
   复制代码
   ```

   当有特殊扩展选项时，用这么使用：

   ```
   const composeEnhancers = typeof window === 'object' && window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ ?
   window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__({
     // 有指定扩展选项，像name, actionsBlacklist, actionsCreators, serialize...
   }) : compose;

   const enhancer = composeEnhancers(
       applyMiddleware(...middleware),
       // 其他store增强器（如果有的话）
   );

   const store = createStore(reducer, enhancer);
   复制代码
   ```

3. 使用`redux-devtools-extension`包 为了简化操作需要安装个 npm 包 `npm install --save-dev redux-devtools-extension` 使用

   ```
   import { createStore, applyMiddleware } from 'redux';
   import { composeWithDevTools } from 'redux-devtools-extension';

   const store = createStore(reducer,
       composeWithDevTools(
           applyMiddleware(...middleware),
           // 其他store增强器（如果有的话）
   ));
   复制代码
   ```

   指定扩展名选项：

   ```
   import { createStore, applyMiddleware } from 'redux';
   import { composeWithDevTools } from 'redux-devtools-extension';

   const composeEnhancers = composeWithDevTools({
     // 如果需要，在这里指定名称，actionsBlacklist，actionsCreators和其他选项
   });
   const store = createStore(reducer, /* preloadedState, */ composeEnhancers(
     applyMiddleware(...middleware),
     // 其他store增强器（如果有的话）
   ));
   复制代码
   ```

   如果你没有包含其它增强器和中间件的话，只需要使用 devToolsEnhancer

   ```
   import { createStore } from 'redux';
   import { devToolsEnhancer } from 'redux-devtools-extension';

   const store = createStore(reducer, /* preloadedState, */ devToolsEnhancer(
     // 需要的话，在这里指定名称，actionsBlacklist，actionsCreators和其他选项
   ));
   复制代码
   ```

4. 在生产环境中使用 这个扩展在生产环境也是有用的，但一般都是在开发环境中使用它。 如果你想限制它的使用，可以用`redux-devtools-extension/logOnlyInProduction`：

   ```
   import { createStore } from 'redux';
   import { devToolsEnhancer } from 'redux-devtools-extension/logOnlyInProduction';

   const store = createStore(reducer, /* preloadedState, */         devToolsEnhancer(
       // actionSanitizer, stateSanitizer等选项
   ));
   复制代码
   ```

   使用中间件和增强器时：

   ```
   import { createStore, applyMiddleware } from 'redux';
   import { composeWithDevTools } from 'redux-devtools-extension/logOnlyInProduction';

   const composeEnhancers = composeWithDevTools({
     // actionSanitizer, stateSanitizer选项
   });
   const store = createStore(reducer, /* preloadedState, */ composeEnhancers(
     applyMiddleware(...middleware),
     // 其它增强器
   ));
   复制代码
   ```

   > 你将不得不在 webpack 的生产环境打包配置中加上`process.env.NODE_ENV': JSON.stringify('production')`。如果你用的是`create-react-app`，那么它已经帮你配置好了

   如果你在创建 store 时检查过`process.env.NODE_ENV`，那么也包括了生产环境的`redux-devtools-extension/logOnly` 如果不想在生产环境使用扩展，那就只开启`redux-devtools-extension/developmentOnly`就好

   > 点击[文章](https://medium.com/@zalmoxis/using-redux-devtools-in-production-4c5b56c5600f)查看更多细节

5. 对于`react-native`, `hybrid`, `desktop` 和 服务端的 redux 应用程序

   - `react-native` 可以用和 redux DevTools Extension 一样 api 的 react-native-debugger 工具。
   - 大多数平台，包括`remote redux devtool's` 的 store 增强器，可以通过扩展上下文的菜单中选择`'open remote devtools'` 来远程监控。
