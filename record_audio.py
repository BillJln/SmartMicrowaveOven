import pyaudio
import wave
import uuid
from tqdm import tqdm
import os

def recording_audio():

    path = '/home/bill/Documents/AI_Microwave_Oven/Test'
    files_name = os.listdir(path)
    for file in files_name:
        os.remove(path + '/' +file)

    s = input('请输入你计划录音多少秒：')

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    RECORD_SECONDS = int(s)
    WAVE_OUTPUT_FILENAME = "/home/bill/Documents/AI_Microwave_Oven/Test/%s.wav" % str(uuid.uuid1()).replace('-', '')

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("开始录音, 请说话......")

    frames = []

    for i in tqdm(range(0, int(RATE / CHUNK * RECORD_SECONDS))):
        data = stream.read(CHUNK)
        frames.append(data)

    print("录音已结束!")

    stream.stop_stream()
    stream.close()
    p.terminate()

    if not os.path.exists('/home/bill/Documents/AI_Microwave_Oven/Test'):
        os.makedirs('/home/bill/Documents/AI_Microwave_Oven/Test')

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    return WAVE_OUTPUT_FILENAME

# print('文件保存在：%s' % recording_audio())
#os.system('pause')
