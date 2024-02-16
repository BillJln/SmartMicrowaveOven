from sqlite3 import *


def heating_mode(heating_item):
    # connect to database
    connection = connect('/home/bill/Documents/AI_Microwave_Oven/item_heating.db')
    item_heating_db = connection.cursor()

    # select
    item_heating_db.execute(
        "SELECT item,heating_mode, temperature1, temperature2, additional_heating_time FROM item_heating WHERE item = (?) ",
        (heating_item,))

    # return values
    values = item_heating_db.fetchall()
    return values[0]

    item_heating_db.close()
    connection.close()



# print(heating_mode('dish'))
