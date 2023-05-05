# LoRA 模型训练

## 一、准备好训练的素材，最好是 20 张图片

## 二、使用批量裁剪工具

https://www.birme.net/

裁剪的最好是 512x512, 或者是 64 的倍数

## 三、图像预处理

- 在 webui 训练标签页里，选择图像预处理
- 钩上"使用 deepbooru 生成说明文字(tags)"
- 源文件夹和目标文件夹不能是同一个

## 四、使用工具 BooruDatasetTagManager 调整

https://github.com/starik222/BooruDatasetTagManager

在这里编辑，和调整标签，删除掉一些不好的

## 五、

## 六、脚本方式训练

<!--
https://github.com/Akegarasu/lora-scripts

```sh
cd /root/autodl-tmp/
git clone --recurse-submodules https://github.com/Akegarasu/lora-scripts
```

脚本下载完毕以后运行

```sh
Installing torch & xformers...
Which version of torch do you want to install?
(1) torch 2.0.0+cu118 with xformers 0.0.17 (suggested)
(2) torch 1.12.1+cu116, with xformers 0bad001ddd56c080524d37c84ff58d9cd030ebfd
Choose: 2
```

大概要安装 5-10 分钟

运行这个脚本需要依赖 python3.10.8

```sh
conda update --force conda
conda install python=3.10.8

conda install -c conda-forge accelerate
conda install toml diffusers transformers albumentations

# https://pytorch.org/get-started/previous-versions/
# CUDA 11.6
conda install pytorch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 pytorch-cuda=11.6 -c pytorch -c nvidia
# CUDA 11.7
conda install pytorch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 pytorch-cuda=11.7 -c pytorch -c nvidia
```

```sh
source venv/bin/activate
``` -->
