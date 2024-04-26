import os
import tkinter as tk
from tkinter import simpledialog, messagebox
from azure.cognitiveservices.speech import SpeechConfig, SpeechSynthesizer, ResultReason, AudioConfig
from config import SUBSCRIPTION_KEY, SERVICE_REGION  # 导入配置

# 初始化 Azure 语音服务配置
speech_config = SpeechConfig(subscription=SUBSCRIPTION_KEY, region=SERVICE_REGION)

# 创建 GUI 根窗口
root = tk.Tk()
root.title("基于微软语音服务的语音合成工具")

# 假设的音色列表
voices = [
    "zh-CN-XiaoxiaoNeural",  # 中文女声
    "zh-CN-YunyangNeural",  # 中文男声
    "zh-CN-YunjianNeural",
    "zh-CN-XiaoyiNeural",
    "zh-CN-YunyangNeural",
    "zh-CN-XiaochenNeural",
    "zh-CN-XiaohanNeural",
    "zh-CN-XiaomengNeural",
    "zh-CN-XiaomoNeural",
    "zh-CN-XiaoqiuNeural",
    "zh-CN-XiaoruiNeural",
    "zh-CN-XiaoshuangNeural",
    "zh-CN-XiaoyanNeural",
    "zh-CN-XiaoyouNeural",
    "zh-CN-XiaozhenNeural",
    "zh-CN-YunfengNeural",
    "zh-CN-YunhaoNeural",
    "zh-CN-YunxiaNeural",
    "zh-CN-YunyeNeural",
    "zh-CN-YunzeNeural",
    "zh-CN-XiaochenMultilingualNeural",
    "zh-CN-XiaorouNeural",
    "zh-CN-XiaoxiaoDialectsNeural",
    "zh-CN-XiaoxiaoMultilingualNeural",
    "zh-CN-XiaoyuMultilingualNeural",
    "zh-CN-YunjieNeural1",
    "zh-CN-YunyiMultilingualNeural",
    "en-US-AriaNeural",  # 英文女声
    "en-US-GuyNeural"  # 英文男声
]


# 试听
def preview_speech():
    text = text_entry.get("1.0", tk.END).strip()
    voice = voice_var.get()  # 获取选择的音色
    if not text:
        messagebox.showinfo("提示", "请输入文本")
        return

    speech_config.speech_synthesis_voice_name = voice  # 设置音色
    synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=None)  # 使用默认音频输出
    result = synthesizer.speak_text_async(text).get()
    print("试听结果：", result.reason)  # 打印试听的结果
    if result.reason != ResultReason.SynthesizingAudioCompleted:
        messagebox.showerror("错误", "语音试听失败")
    else:
        print("试听成功")  # 可以选择性添加一些反馈信息


# 保存合成的语音到文件
def save_speech():
    text = text_entry.get("1.0", tk.END).strip()
    voice = voice_var.get()  # 获取选择的音色
    speech_config.speech_synthesis_voice_name = voice  # 设置音色
    if not text:
        messagebox.showinfo("提示", "请输入文本")
        return

    file_name = simpledialog.askstring("保存音频", "输入文件名:", parent=root)
    if file_name:
        file_path = os.path.join("audio", f"{file_name}.wav")
        # 显式检查文件夹是否存在
        if not os.path.exists(os.path.dirname(file_path)):
            os.makedirs(os.path.dirname(file_path))  # 如果不存在就创建文件夹
        audio_config = AudioConfig(filename=file_path)
        synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
        result = synthesizer.speak_text_async(text).get()
        if result.reason == ResultReason.SynthesizingAudioCompleted:
            messagebox.showinfo("保存成功", f"音频已保存到: {file_path}")
        else:
            messagebox.showerror("错误", "保存音频失败")


# 创建 GUI 组件
text_entry = tk.Text(root, height=10, width=50)
text_entry.pack(pady=20)

voice_var = tk.StringVar(root)  # 创建一个Tkinter字符串变量
voice_var.set(voices[1])  # 默认设置为第一个音色

voice_menu = tk.OptionMenu(root, voice_var, *voices)  # 创建下拉菜单
voice_menu.pack(pady=10)

preview_button = tk.Button(root, text="试听", command=preview_speech)
preview_button.pack(pady=10)

save_button = tk.Button(root, text="保存音频", command=save_speech)
save_button.pack(pady=10)

root.mainloop()
