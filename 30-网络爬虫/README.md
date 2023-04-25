# spider-man 网络爬虫学习项目

## 爬虫分类

- 通用爬虫

  - 获取重要信息，抓取一个页面

- 聚焦爬虫

  - 建立在通用爬虫的基础上，抓取页面中特定局部内容

- 增量式爬虫

  - 检测数据更新情况，只抓取新增的数据

## 爬虫的矛与盾

### 反爬机制

### 反反爬虫技术

## robots.txt 协议

君子协议 明确规定哪些网站可以被爬取，哪些不可以。

https://www.taobao.com/robots.txt

---

# 技能栈

## 初阶技能

### 获取数据

- 请求库

  - [ ] urillib
  - [ ] request
  - [ ] selenium
  - [ ] aiohttp

- 抓包工具

  - [ ] chrome
  - [ ] Fidder
  - [ ] Appium

### 解析数据

- [ ] css
- [ ] pyquery
- [ ] beautifulsoup
- [ ] xpath
- [ ] re

### 数据存储

- 小规模

  - [x] txt
  - [x] json
  - [x] csv

- 大规模

  - [ ] mysql
  - [ ] mongodb
  - [ ] redis

## 中阶技能 爬虫框架

- [ ] Scrapy(重点)
- [ ] Appium
- [ ] Nutch
- [ ] Pyspider

其他配套附属技能

- [ ] django

## 高阶技能

- [ ] 反爬
- [ ] 对应措施
- [ ] 分布式爬虫系统
- [ ] 工程逆向
- [ ] 人工智能训练

---

### 验证码识别

通过“超级鹰” https://www.chaojiying.com/

### 滑动验证码

- [ ] 1. 学习 Python 基础。Python 是爬虫领域最重要的语言,所以要熟练掌握 Python 语法、数据结构等基础知识。
- [ ] 2. 学习网页抓取原理。要理解 HTTP 协议、HTML 语言的原理,掌握解析 HTML 的基本方法。推荐学习 BeautifulSoup 和 lxml 两个库。
- [ ] 3. 学习反爬机制和对应方法。要了解网站为什么要采用反爬措施,以及如何绕过常见的反爬机制,比如 IP 限制、User-Agent 检测等。
- [ ] 4. 学习 Scrapy 框架。Scrapy 是 Python 的一个重量级爬虫框架,使用 Scrapy 可以快速开发强大的爬虫。
- [ ] 5. 学习代理和 IP 池的使用。代理可以隐藏真实 IP,绕过某些简单的反爬机制。IP 池可以提供大量 IP 用于爬取。
- [ ] 6. 了解爬虫部署方法。包括 Scrapyd 部署 Scrapy 项目,Docker 部署,AWS、阿里云等云服务部署等。
- [ ] 7. 其他高级技术学习。比如 Scrapy Middlewares、动态网页爬取、JS 渲染等各种高级技术的原理和应用。
- [ ] 8. 项目实战。通过一些实际项目,熟练运用所学知识进行爬虫开发,实现网站数据抓取。
