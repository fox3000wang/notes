# chrome 插件基础模版 v3

## 简介

- 小 DEMO 功能
- 点击 icon
- 弹出 popup 窗口
- 点击按钮 1
- 自动弹出百度页面
- 2 秒后自动关闭

## 文件介绍

### 主文件 manifest.json

- manifest_version // manifest 版本，这里默认是 3
- icons // 图标，最好是 PNG，支持 BMP, GIF, ICO, and JPEG. 支持四种大小像素 16*16，32*32，48*48，128*128
- action // 工具栏按钮，mv2 里面写法：browser_action、page_action
- externally_connectable //清单属性声明哪些扩展程序、应用程序和网页可以通过 runtime.connect 和 runtime.sendMessage 连接到您的扩展程序
- permissions // 扩展需要的权限
- host_permissions // 页面权限

### js 文件

- background 核心调试文件
- background.js 注入业务文件
- popup.js 控制弹出框

#### 依赖

- superagent.js 无头浏览器库
- polyfill.min.js 上面文件的依赖

## 其他参考

https://juejin.cn/post/7021072232461893639#heading-12

## 官方文档

https://developer.chrome.com/docs/extensions/

## 关于升级到 Manifest V3

https://developer.chrome.com/docs/extensions/mv3/mv3-migration/
