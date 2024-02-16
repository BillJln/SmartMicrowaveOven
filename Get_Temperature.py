import ctypes
import time


def get_temperatures():
    dll = ctypes.windll.LoadLibrary("D:/AI_Microwave_Oven/Temperature.dll")

    temperatures = {}

    for num in range(0, 100):
        ti1 = dll.GetTemp1()
        # print("温度1:")
        # print(ti1 / 10)
        temperatures["temperature1"] = ti1 / 10

        ti2 = dll.GetTemp2()
        # print("温度2：")
        # print(ti2 / 10)
        temperatures["temperature2"] = ti2 / 10

        # hi = dll.GetHumidity1()
        # print("湿度:")
        # print(hi / 10)

        if ti1 / 10 == 3276.7:
            temperatures["temperature1"] = -1

        if ti2 / 10 == 3276.7:
            temperatures["temperature2"] = -1

        return (temperatures)

        # time.sleep(1)

# if __name__ == '__main__':
#     sleep_second = 3
#     while True:
#         time.sleep(sleep_second)
#         print(get_temperatures())
