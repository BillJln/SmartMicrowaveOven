# encoding:utf-8
import base64
import json
import requests

from Get_Picture_And_Audio_Path import get_file_name


def item_cls():
    hash_path = "D:/AI_Microwave_Oven/app/static/images"
    suffix = '.jpg'
    file_name = get_file_name(hash_path, suffix)
    picture_name = hash_path + '/' + file_name

    path = picture_name
    # path = "D:/AI_Microwave_Oven/Test_Set/Picture/dish1.jpg"

    with open(path, 'rb') as f:
        base64_data = base64.b64encode(f.read())

    request_url = "	https://aip.baidubce.com/rpc/2.0/ai_custom/v1/classification/AI_Microwave_Oven_3"

    params = {
        "image": str(base64_data, encoding="utf-8"),
        "top_num": "1",
    }
    data = json.dumps(params)
    access_token = '24.33250def7bb4e665aa7bc312d4c97f20.2592000.1628747274.282335-24111192'
    request_url = request_url + "?access_token=" + access_token
    headers = {"'Content-Type'": 'application/json'}
    response = requests.post(url=request_url, headers=headers, data=data)
    content = response.text
    if content:
        # print(content)

        begin = content.index('name')
        end = content.index('score')
        # print(content[begin + 7:end - 3])

        return content[begin + 7:end - 3]
        # return content

# 输出结果
# if __name__ == '__main__':
#     print(item_cls())
