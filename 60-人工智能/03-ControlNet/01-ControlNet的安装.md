# ControlNet 的安装

## 插件 WebUI extension for ControlNet

https://github.com/Mikubill/sd-webui-controlnet

## 模型

https://openai.wiki/controlnet-install.html

https://huggingface.co/lllyasviel/ControlNet-v1-1/tree/main

---

---

## ControlNet 和 T2I-Adapter 有什么区别？

ControlNet 在论文里提到，Canny Edge Detector 模型的训练用了 300 万张边缘-图像-标注对的语料，A100 80G 的 600 个 GPU 小时。Human Pose （人体姿态骨架）模型用了 8 万张 姿态-图像-标注 对的语料, A100 80G 的 400 个 GPU 时。 T2I-Adapter 的训练是在 4 块 Tesla 32G-V100 上只花了 2 天就完成，包括 3 种 condition，sketch（15 万张图片语料），Semantic segmentation map（16 万张）和 Keypose（15 万张）。 两者的差异：ControlNet 目前提供的预训模型，可用性完成度更高，支持更多种 condition detector （9 大类）。 T2I-Adapter ”在工程上设计和实现得更简洁和灵活，更容易集成和扩展” 此外，T2I-Adapter 支持一种以上的 condition model 引导，比如可以同时使用 sketch 和 segmentation map 作为输入条件，或 在一个蒙版区域 (也就是 inpaint ) 里使用 sketch 引导。

## 参考资料汇总

- ControlNet-G 站主页：https://link.zhihu.com/?target=https%3A//github.com/lllyasviel/ControlNet
- ControlNet-G 站教程: https://link.zhihu.com/?target=https%3A//github.com/Mikubill/sd-webui-controlnet%23examples
- T2I-G 站主页：https://link.zhihu.com/?target=https%3A//github.com/TencentARC/T2I-Adapter
- T2I-G 站介绍：https://link.zhihu.com/?target=https%3A//github.com/TencentARC/T2I-Adapter/blob/main/docs/examples.md
- 中文教程：https://link.zhihu.com/?target=https%3A//openai.wiki/controlnet-guide.html
- 参考文章：https://link.zhihu.com/?target=https%3A//h1cji9hqly.feishu.cn/docx/YioKdqC0oo7XThxvW1ccOmbunEh
- 模型下载（5G 版）https://link.zhihu.com/?target=https%3A//huggingface.co/lllyasviel/ControlNet/tree/main/models
- 模型下载（700m 版）https://link.zhihu.com/?target=https%3A//huggingface.co/webui/ControlNet-modules-safetensors/tree/main

> 注：700m 版为压缩过的 16 位浮点模型（16fp 表示范围更小，但文件更小，内存需求也更小，每个模型仅 700MB）
