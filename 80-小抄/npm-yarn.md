# Yarn 和 Npm 命令行小抄

安装 Yarn

```bash
npm i -g yarn
```

## 常用命令

- `npm install` === `yarn` —— install 安装是默认行为。
- `npm install taco --save` === `yarn add taco` —— taco 包立即被保存到 `package.json` 中。
- `npm uninstall taco --save` === `yarn remove taco
- `npm install taco --save-dev` === `yarn add taco --dev`
- `npm update --save` === `yarn upgrade`

## 已知悉的命令

包和 npm registry 上是一样的。大致而言，Yarn 只是一个新的安装工具，npm 结构和 registry 还是一样的。

- `npm init` === `yarn init`
- `npm link` === `yarn link`
- `npm outdated` === `yarn outdated`
- `npm publish` === `yarn publish`
- `npm run` === `yarn run`
- `npm cache clean` === `yarn cache clean`
- `npm login` === `yarn login` (logout 同理)
- `npm test` === `yarn test`

## Yarn 独有的命令

我跳过了一些提醒我们不要使用的内容，如 [yarn clean](https://yarnpkg.com/en/docs/cli/clean)。

- `yarn licenses ls` —— 允许你检查依赖的许可信息。
- `yarn licenses generate` —— 自动创建依赖免责声明 license。
- `yarn why taco` —— 检查为什么会安装 taco，详细列出依赖它的其他包（鸣谢 [Olivier Combe](https://medium.com/u/5ae4b2205cba)）。
- Emojis
- [速度](https://yarnpkg.com/en/compare)
- 通过 yarn lockfile 自动实现 shrinkwrap 功能
- 以安全为中心的设计

## Npm 独有的命令

- `npm xmas` === **NO EQUIVALENT**
- `npm visnup` === **NO EQUIVALENT**

# npm 命令简写

###### -g

> --global，缩写为-g，表示安装包时，视作全局的包。安装之后的包将位于系统预设的目录之下。

###### -S

> --save，缩写为-S，表示安装的包将写入 package.json 里面的 dependencies。

###### -D

> --save-dev，缩写为-D，表示将安装的包将写入 packege.json 里面的 devDependencies。

###### -O

> --save-optional 缩写为-O，表示将安装的包将写入 packege.json 里面的 optionalDependencies。

###### -E

> --save-exact 缩写为-E，表示安装的包的版本是精确指定的。

###### -B

> --save-bundle 缩写为-B，表示将安装的包将写入 packege.json 里面的 bundleDependencies。
