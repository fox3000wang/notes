# ControlNet 的使用

https://openai.wiki/controlnet-guide.html

## 预处理器与对应模型清单

| 预处理器名称  | 对应 ControlNet 模型 | 对应腾讯 t2i 模型                      | 功能描述                                     |
| ------------- | -------------------- | -------------------------------------- | -------------------------------------------- |
| canny         | control_canny        | t2iadapter_canny                       | 边缘检测，适合原画设计师                     |
| depth         | control_depth        | t2iadapter_depth                       | MiDaS 深度检测                               |
| depth_leres   | control_depth        | t2iadapter_depth                       | LeReS 深度检测                               |
| hed           | control_hed          | 无                                     | 边缘检测但保留更多细节，适合重新着色和风格化 |
| mlsd          | control_mlsd         | 无                                     | 线段识别，识别人物功能极差，适合建筑设计师   |
| normal_map    | control_normal       | 无                                     | 根据图片生成法线贴图，适合 CG 或游戏美术师   |
| openpose      | control_openpose     | t2iadapter_openpose t2iadapter_keypose | 提取人物骨骼姿势                             |
| openpose_hand | control_openpose     | t2iadapter_openpose t2iadapter_keypose | 提取人物+手部骨骼姿势                        |
| scribble      | control_scribble     | t2iadapter_sketch                      | 应用自画的黑白稿                             |
| fake_scribble | control_scribble     | t2iadapter_sketch                      | 涂鸦风格提取（很强大的模型）                 |
| segmentation  | control_seg          | t2iadapter_seg                         | 应用语义分割                                 |
| binary        | control_scribble     | t2iadapter_sketch                      | 提取黑白稿                                   |
| clip_vision   | 无                   | t2iadapter_style                       | 风格转移                                     |
| color         | 无                   | t2iadapter_color                       | 色彩分布                                     |

---

## 模型功能分类

| 功能描述         | 对应 ControlNet 模型 | 备注       |
| ---------------- | -------------------- | ---------- |
| 边缘检测 人物    | canny,hed,softedge   | 适合人物   |
| 边缘检测 建筑    | mlsd                 | 适合建筑   |
| 生成法线贴图     | normal               | 3D         |
| 提取人物骨骼姿势 | openpose             | 需插件配合 |
| 深度检测         | depth                |            |
| 生成黑白稿       | scribble             | 艺术涂鸦   |
| 手绘涂鸦         | fake_scribble        | 涂鸦(很强) |
| 高清重绘         | tile                 |            |
| 线稿上色         | lineart              | 偏写实     |
| 线稿上色         | anime lineart        | 偏动漫     |
| 图生图           | ip2p                 |            |
| 重绘             | inpaint              |            |
