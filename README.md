
# 基于微软语音服务的语音合成工具

这是一个基于微软 Azure 认知服务的语音合成应用，允许用户输入文本并将其转换为语音，用户可以试听合成的语音并保存为音频文件。

## 功能特点

- 文本到语音的转换
- 试听合成的语音
- 将语音保存为 WAV 文件
- 简单易用的图形用户界面

## 开始使用

### 环境要求

- Python 3.6+
- Windows, macOS 或 Linux

### 安装

1. 克隆或下载此仓库到本地。

2. 安装必要的依赖。

   ```bash
   pip install -r requirements.txt
   ```

3. 创建一个Azure语音服务的订阅，获取你的订阅密钥和服务区域。[Microsoft Azure云计算服务](https://azure.microsoft.com/zh-cn/)

### 配置
你需要在项目根目录下自行创建`config.py` 文件，并设置你的Azure订阅密钥和服务区域。

```python
# config.py
SUBSCRIPTION_KEY = "你的Azure订阅密钥"
SERVICE_REGION = "你的服务区域"
```

### 运行程序

运行主程序：

```bash
python main.py
```

## 使用说明

启动程序后，你会看到一个图形用户界面，其中包括：

- 一个文本框，用于输入你希望转换为语音的文本。
- 一个“试听”按钮，点击后可以听到文本的语音输出。
- 一个“保存音频”按钮，点击后可以将语音输出保存为WAV文件。文件路径位于项目根目录的audio文件夹下。

## 许可证

此项目使用 MIT 许可证。详情请查看 [LICENSE](LICENSE) 文件。

## 贡献

欢迎贡献！如果你有好的建议或改进，请提交 Pull Request 或开 Issue 讨论。

## 联系方式

如果你有任何问题，请联系我们。