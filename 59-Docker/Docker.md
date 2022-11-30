# Docker

## 简介

Docker 是一个开放源代码的开放平台软件，用于开发应用、交付应用、运行应用。Docker 允许用户将基础设施中的应用单独分割出来，形成更小的颗粒，从而提高交付软件的速度。 Docker 容器与虚拟机类似，但二者在原理上不同。容器是将操作系统层虚拟化，虚拟机则是虚拟化硬件，因此容器更具有便携性、高效地利用服务器。

## 应用

暂略

## 搭建私服

暂略

## 打包 node 项目

### 1.创建打包 Dockerfile

```Dockerfile
# node version
FROM node:12

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
RUN npm install

# If you are building your code for production
# RUN npm ci --only=production
RUN npm run build

# Bundle app source
COPY . .

EXPOSE 9999
CMD [ "node", "dist/main" ]
```

### 2.创建.dockerignore

```.dockerignore
node_modules
npm-debug.log
script
```

### 3.运行打包脚本

```shell
docker build . -t gigi-server

docker images

REPOSITORY                 TAG       IMAGE ID       CREATED          SIZE
gigi-server                latest    e0447f86ae8a   13 minutes ago   1.2GB
```

### 4.测试运行

```docker-compose.yml
version: '3.0'
services:
  server:
    image: gigi-server
    ports:
      - 9999:9999
    restart: always
```

```shell
docker-compose up
```

###

参考： https://nodejs.org/zh-cn/docs/guides/nodejs-docker-webapp/
官方文档： https://docs.docker.com/engine/reference/builder/

## 最佳实践

https://docs.docker.com/develop/dev-best-practices/
