# -*- coding: utf-8 -*-

# 将AI_Mircowave_Oven解压到D盘根目录下

from image_predict import item_cls
from audio_predict import sound_cls
from Connect_To_SQLlite import heating_mode
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import shutil
from Get_Picture_And_Audio_Path import get_file_name
from Get_Temperature import get_temperatures
import time
from Take_A_Picture import take_a_picture
from Record_An_Audio import record_an_audio
from record_audio import recording_audio

app = Flask(__name__)

temperature_sensor1_bool = True
temperature_sensor2_bool = True
real_time_temperature1 = 0
real_time_temperature2 = 0

start_time = 0
start_time_bool = True
heating_time = 0

rest_time = 0
start_counting_down_time = 0
start_counting_down = True
heating_control = "no_reaching_specified_temperature"

file_dir = '/home/bill/Documents/AI_Microwave_Oven/Test'
shutil.rmtree(file_dir)
os.mkdir(file_dir)

picture_taking_bool = input("你想要拍摄实时图片吗？（y/n）? :")
if picture_taking_bool == 'y':
    camera = input("笔记本自带摄像头输入0，外接摄像头输入1 ：")
    print("查看任务栏最小化拍照界面，鼠标点击拍照窗口任意位置，敲击键盘s键，图片保存到了Test文件夹，请后续上传")
    take_a_picture(int(camera))
else:
    print("可自行准备图片或音频上传，项目提供Test_Set文件夹，可利用文件夹中图片上传")

audio_recording_bool = input("你想要录制实时音频吗？（y/n）? :")
if audio_recording_bool == 'y':
    print("音频保存到了Test文件夹，请后续上传")
    recording_audio()
else:
    print("可自行准备图片或音频上传，项目提供Test_Set文件夹，可利用文件夹中音频上传")

print("程序已启动在：http://127.0.0.1:5000/ 端口,点击跳转")


@app.route('/')
@app.route('/upload')
def upload_file():
    file_dir = '/home/bill/Documents/AI_Microwave_Oven/app/static/images'
    shutil.rmtree(file_dir)
    os.mkdir(file_dir)

    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        f = request.files['file']

        os.chdir("/home/bill/Documents/AI_Microwave_Oven/app/static/images")

        f.save(secure_filename("test" + str(hash(f)) + f.filename[-4:]))

        if f.filename.endswith('wav'):
            return 'sound uploaded successfully'
        elif f.filename.endswith('WAV'):
            return 'sound uploaded successfully'
        elif f.filename.endswith('jpg'):
            return 'picture uploaded successfully'
        elif f.filename.endswith('JPG'):
            return 'picture uploaded successfully'
        else:
            return 'upload failed'


@app.route('/show')
def show_informations():
    hash_path = "/home/bill/Documents/AI_Microwave_Oven/app/static/images"
    suffix = '.jpg'
    picture_name = get_file_name(hash_path, suffix)

    item_cls()

    f = open("/home/bill/Documents/AI_Microwave_Oven/result.txt")
    line = f.readline()

    # if not isinstance(item, str):
    #     item = str(item)

    item = line.strip()

    global temperature_sensor1_bool
    global temperature_sensor2_bool
    global real_time_temperature1
    global real_time_temperature2

    global start_time
    global start_time_bool
    global heating_time

    global rest_time
    global start_counting_down_time
    global start_counting_down
    global heating_control

    voice_order_index = sound_cls()
    if voice_order_index == 0:
        voice_order = "start"
    elif voice_order_index == 1:
        voice_order = "end"
    elif voice_order_index == 2:
        voice_order = "pause"

    if start_time_bool:
        start_time = time.time()
        start_time_bool = False

    if heating_mode(item)[1] == "no_heating":
        heating_time = "0"
    else:
        if (voice_order == "start"):
            heating_time = str(int(time.time() - start_time))
        else:
            heating_time = "heating_not_started"

    # real_time_temperature2 = get_temperatures()["temperature1"]
    # real_time_temperature1 = get_temperatures()["temperature2"]
    real_time_temperature2 = 20
    real_time_temperature1 = 18


    if real_time_temperature1 == -1:
        real_time_temperature1 = "temperature sensor1 not connected"
        temperature_sensor1_bool = False
    if real_time_temperature2 == -1:
        real_time_temperature2 = "temperature sensor2 not connected"
        temperature_sensor2_bool = False

    additional_heating_time = int(heating_mode(item)[4])

    if (temperature_sensor1_bool and temperature_sensor2_bool and int(real_time_temperature1) >= int(
            heating_mode(item)[2]) and int(real_time_temperature2) >= int(
        heating_mode(item)[
            3]) and start_counting_down):
        start_counting_down_time = time.time()
        start_counting_down = False

    if start_counting_down_time != 0:
        rest_time = additional_heating_time - (start_counting_down_time - time.time())
        if rest_time < 0:
            heating_control = "heating_completed"
        else:
            heating_control = str(int(rest_time))

    return render_template('show.html',
                           picture=picture_name,
                           picture_kind=item,
                           order=voice_order,
                           heating_mode=heating_mode(item)[1],
                           setting_temperature1=heating_mode(item)[2],
                           setting_temperature2=heating_mode(item)[3],
                           additional_heating_time=
                           heating_mode(item)[4],
                           current_time_temperature1=real_time_temperature1,
                           current_time_temperature2=real_time_temperature2,
                           heating_time=heating_time,
                           count_down_time=heating_control)


# app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=False)
