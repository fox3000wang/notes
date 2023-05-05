# stable-diffusion-webui

## 整合包

https://www.codewithgpu.com/i/AUTOMATIC1111/stable-diffusion-webui/NovelAI-Consolidation-Package-3.1

## 文生图

### 采样方法 sampler

一般默认用 Euler a

### 采样迭代步数 steps

默认 20, 一般 30

### 面部修复

对二次元效果反而不好
一般三次元开

### 可平铺

生成花纹，一般新手不用

### 高清修复

一般画全身图，脸部会崩
开了以后脸会正常一些

面部修复和高清修复不要同时开

### 宽度 和 高度

默认: 512 x 512

SD1.5 的版本不要超过 1024
至少有一个参数是 512 或者 768

### 提示词相关性(CFG Scale)

123 的时候画面会比较暗，4 以后画面效果会比较好，
9 以后对比度会变重，色彩会非常鲜艳。

### 随机种子(seed)

### 脚本

#### X/Y/Z 图表

#### 提示词矩阵

### clip 跳过层

一般来说，是个玄学 一般情况下 2-4 都可以

## 图生图

- VAE
