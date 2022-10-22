# Selenium

[官网](https://www.selenium.dev/)

Selenium 有 3 个子项目，我们主要用到 [WebDriver](https://www.selenium.dev/documentation/webdriver/)

[Selenium Grid](https://www.selenium.dev/documentation/grid/) 用于分布式，以后应该可以考虑用到

## Getting started 入门

### Install a Selenium library 安装语言依赖库

```bash
pip install selenium
```

```bash
npm install selenium-webdriver
```

### Install browser drivers 安装驱动

下载地址:
[官方驱动页面](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/)

bash zsh 把 chromedriver 放到环境变量里

```bash
echo 'export PATH=$PATH:/path/to/driver' >> ~/.zshenv
```
