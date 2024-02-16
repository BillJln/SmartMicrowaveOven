import torch
import numpy as np
import librosa
import os
from record_audio import recording_audio

# 加载模型
model_path = '/home/bill/Documents/AI_Microwave_Oven/AudioClassification-Pytorch-master/models/resnet34.pth'
device = torch.device("cuda")
model = torch.jit.load(model_path)
model.to(device)
model.eval()

def load_data(data_path, spec_len=128):
    # 读取音频
    wav, sr = librosa.load(data_path, sr=16000)
    spec_mag = librosa.feature.melspectrogram(y=wav, sr=sr, hop_length=256).astype(np.float32)
    mean = np.mean(spec_mag, 0, keepdims=True)
    std = np.std(spec_mag, 0, keepdims=True)
    spec_mag = (spec_mag - mean) / (std + 1e-5)
    spec_mag = spec_mag[np.newaxis, np.newaxis, :]
    return spec_mag


def infer(audio_path):
    data = load_data(audio_path)
    data = torch.tensor(data, dtype=torch.float32, device=device)
    # 执行预测
    output = model(data)
    result = torch.nn.functional.softmax(output)
    result = result.data.cpu().numpy()
    print(result)
    # 显示图片并输出结果最大的label
    lab = np.argsort(result)[0][-1]
    return lab


# if __name__ == '__main__':
def sound_cls():
    # recording_audio()
    # 要预测的音频文件
    path = '/home/bill/Documents/AI_Microwave_Oven/Test'
    file_name = os.listdir(path)
    file = path + '/' + file_name[0]
    if file_name[0].split('.')[1] == "wav":
        label = infer(file)
        print('音频：%s 的预测结果标签为：%d' % (file, label))
    return label