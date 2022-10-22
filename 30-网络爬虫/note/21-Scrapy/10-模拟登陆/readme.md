# 模拟登陆

## 登陆的实质

就是拿用户名和密码，放在 form 里面，用 http 的 post 请求，返回的 cookie

## 识别验证码

### OCR 识别

```
sudo apt-get install tesseract-ocr

pip install pillow
pip install pytesseract

```

### 网络平台识别

略 需要花钱

### 人工识别

略

## Cookie 登录

### 获取浏览器 Cookie

```
pip install browsercookie
```
