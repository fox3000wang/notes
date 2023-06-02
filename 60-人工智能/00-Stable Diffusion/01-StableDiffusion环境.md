# StableDiffusion 环境

## 官网

https://github.com/Stability-AI/stablediffusion

## 依赖

安装操作系统的时候选择自带 Miniconda

然后安装依赖

```sh
git clone https://github.com/Stability-AI/stablediffusion.git
cd stablediffusion

conda install pytorch==1.12.1 torchvision==0.13.1 -c pytorch
pip install transformers==4.19.2 diffusers invisible-watermark
pip install -e .
# Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
# 以“root”用户身份运行pip可能会导致权限中断以及与系统包管理器发生冲突。建议改用虚拟环境：https://pip.pypa.io/warnings/venv
```
