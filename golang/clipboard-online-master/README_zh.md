<div align="center">
  <img src="https://raw.githubusercontent.com/YanxinTang/clipboard-online/master/images/clipboard-icon.png" style="display: inline-block; vertical-align: middle;">
  <h1 style="display: inline-block; vertical-align: middle;">clipboard-online</h1>
</div>

![GitHub release (latest by date)](https://img.shields.io/github/v/release/YanxinTang/clipboard-online)

clipboard-online 是一款可以帮你在 💻Windows 和 📱iOS 之间分享剪切板的应用

## 文档

【[English](https://github.com/YanxinTang/clipboard-online/blob/master/README.md)】【[中文](https://github.com/YanxinTang/clipboard-online/blob/master/README_zh.md)】

## 下载

1. 直接下载

    在[这里](https://github.com/YanxinTang/clipboard-online/releases)下载发布的 .exe 文件

2. 源码编译(只在 Windows 下可用，其他平台未知)

    构建之前，请确保你已经安装了 golang. 如果没有，可能你需要[这个](https://golang.org/dl/)

    - `git clone git@github.com:YanxinTang/clipboard-online.git`
    - `cd clipboard-online`
    - `go get github.com/akavel/rsrc`
    - `./build.sh`
    - 你可以在 `release` 目录下找到可执行文件

## 使用

1. 在 Windows 上运行 `clipboard-online`
2. iPhone 或 iPad 上安装快捷指令 （在 safari 中打开链接）
    - 复制: [https://www.icloud.com/shortcuts/242c55e0895e4235875bc71f1f010199](https://www.icloud.com/shortcuts/242c55e0895e4235875bc71f1f010199)
    - 粘贴: [https://www.icloud.com/shortcuts/6a46febf2f0c4ef4b00bbc41f03ccd2f](https://www.icloud.com/shortcuts/6a46febf2f0c4ef4b00bbc41f03ccd2f)
3. 玩的开心...😊

## 配置

`clipboard-online.exe` 将在运行路径下面创建两个文件： `config.json` and `log.txt`

你可以通过修改 `config.json` 来自定义配置

### `config.json`

- `port`
  - 类型: `string`
  - 默认: `"8086"`

- `logLevel`
  - 类型: `string`
  - 默认: `"warning"`
  - 可选: `"panic"`, `"fatal"`, `"error"`, `"warning"`, `"info"`, `"debug"`, `"trace"`

## API

### 1. 获取 Windows 剪切板

> Request

- URL: `/`
- Method: `GET`

> Reponse

- Body: `<clipboard text>`

### 2. 设置 Windows 剪切板

> Request

- URL: `/`
- Method: `POST`
- Body: `text you want to set`

> Reponse

响应的 body 为空。如果剪切板设置成功，状态码将返回 `200`
