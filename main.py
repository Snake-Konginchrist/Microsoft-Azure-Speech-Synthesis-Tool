import os
import tkinter as tk
from tkinter import simpledialog, messagebox
from azure.cognitiveservices.speech import SpeechConfig, SpeechSynthesizer, AudioConfig
from config import SUBSCRIPTION_KEY, SERVICE_REGION  # 导入配置

# 初始化 Azure 语音服务配置
speech_config = SpeechConfig(subscription=SUBSCRIPTION_KEY, region=SERVICE_REGION)

# 创建 GUI 根窗口
root = tk.Tk()
root.title("基于微软语音服务的语音合成工具")


# 合成语音并试听
def synthesize_speech():
    text = text_entry.get("1.0", tk.END).strip()
    if not text:
        messagebox.showinfo("提示", "请输入文本")
        return

    synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=None)
    result = synthesizer.speak_text_async(text).get()
    if result.reason != result.Reason.SynthesizingAudioCompleted:
        messagebox.showerror("错误", "语音合成失败")


# 保存合成的语音到文件
def save_speech():
    text = text_entry.get("1.0", tk.END).strip()
    if not text:
        messagebox.showinfo("提示", "请输入文本")
        return

    file_name = simpledialog.askstring("保存音频", "输入文件名:", parent=root)
    if file_name:
        file_path = os.path.join("data", f"{file_name}.wav")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        audio_config = AudioConfig(filename=file_path)
        synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
        result = synthesizer.speak_text_async(text).get()
        if result.reason == result.Reason.SynthesizingAudioCompleted:
            messagebox.showinfo("保存成功", f"音频已保存到: {file_path}")
        else:
            messagebox.showerror("错误", "保存音频失败")


# 创建 GUI 组件
text_entry = tk.Text(root, height=10, width=50)
text_entry.pack(pady=20)

synthesize_button = tk.Button(root, text="试听", command=synthesize_speech)
synthesize_button.pack()

save_button = tk.Button(root, text="保存音频", command=save_speech)
save_button.pack(pady=10)

root.mainloop()
