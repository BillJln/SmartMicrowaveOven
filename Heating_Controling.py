import time
from Connect_To_SQLlite import heating_mode
from Object_Recognition_api import item_cls
from Voice_Recognition_api import sound_cls


# heating_modes = {
# 'barbecue': ['high_temperature_heating', 95, 95, 30], 'dish': ['high_temperature_heating', 95, 95, 30],
# 'rice': ['high_temperature_heating', 90, 90, 20],
# 'boil': ['medium_and_high_temperature_heating', 95, 95, 20],
# 'steam': ['medium_and_high_temperature_heating', 95, 95, 20],
# 'stew': ['medium_and_high_temperature_heating', 95, 95, 30],
# 'fry': ['medium_temperature_heating', 90, 90, 50],
# 'drink': ['medium_temperature_heating', 60, 60, 10],
# 'sterilization': ['low_temperature_heating', 95, 95, 60],
# 'chilling_food': ['thawing_heating', 95, 95, 240],
# }


def heating_control(heating_item):
    heating_method = heating_mode(heating_item)[0][1]
    additional_heating_time = heating_mode(heating_item)[0][4]

    if (heating_method == 'no_heating'):
        # print("{0} cannot be heated!".format(heating_item))
        return ("{0} cannot be heated!".format(heating_item))
    else:
        if (judge_the_temperature(heating_item)):
            # print(heating_item + " has been heated for {0} seconds, heating completed!".format(additional_heating_time))
            return (heating_item + " has been heated for {0} seconds, heating completed!".format(
                additional_heating_time))
        else:
            # print(heating_item + " , heating failed")
            return (heating_item + " has been heated for {0} seconds, heating completed!".format(
                additional_heating_time))


def judge_the_temperature(heating_item):
    duration = 0
    real_time_temperature1 = 100
    real_time_temperature2 = 100

    Order = sound_cls()
    heating_information = heating_mode(heating_item)

    if (Order == 'start'):
        # start heating
        # heating to the suitalbe temperature
        if (real_time_temperature1 >= heating_information[0][2] and real_time_temperature2 >=
                heating_information[0][3]):
            start = time.time()
            while (duration <= heating_information[0][4]):
                duration = time.time() - start
            return True

    return False


heating_item = item_cls()

# print(heating_control(heating_item))
