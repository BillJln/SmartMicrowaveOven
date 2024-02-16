import base64
import json
import pprint
import requests

from Get_Picture_And_Audio_Path import get_file_name


# def get_token():
#     client_id = 'Zie7k517LyMkf8IsIKe0arhM'
#     client_secret = 'Zie7k517LyMkf8IsIKe0arhM'
#     host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials'
#     host += "&client_id=%s&client_secret=%s" % (client_id, client_secret)
#     session = requests.Session()
#     response = session.get(host)
#     access_token = response.json().get("access_token")
#     # print(access_token)
#     return access_token


def sound_cls():
    # access_token获取方法请详见API使用说明，请注意access_token有效期为30天,这里仅为了简化编码每一次请求都去获取access_token
    # access_token = get_token()
    # 请将API地址替换为EasyDL所提供的API地址

    hash_path = "D:/AI_Microwave_Oven/app/static/images"
    suffix = '.MP3'
    file_name = get_file_name(hash_path, suffix)

    audio_name = hash_path + '/' + file_name
    request_url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/sound_cls/MircowaveOvenOrder1"
    with open(audio_name, 'rb') as f:
        sound = base64.b64encode(f.read()).decode('UTF8')
    headers = {
        'Content-Type': 'application/json'
    }
    params = {
        "sound": sound,
        "top_num": 1
    }
    access_token = '24.bedd991980778af0ebaf67edd4fb3d3d.2592000.1628747172.282335-24111424'
    request_url = request_url + "?access_token=" + access_token
    # start = time.time()
    response = requests.post(request_url, headers=headers, json=params)
    content = response.content.decode('UTF-8')
    result = json.loads(content)
    # end = time.time()
    # print('耗时时长: %1.2f s' % (end - start))
    result = pprint.pformat(result)

    # return result

    # print(result)
    begin = result.index('name')
    end = result.index('score')
    # print(result[begin + 8:end - 4])
    return result[begin + 8:end - 4]

# 输出结果
# if __name__ == '__main__':
#     print(sound_cls())
