import os
from icecream import ic


def get_entry_direction(main_dir: str, sub_dir: str, sub_dir_folder: str = '') -> list[str]:
    ''' Return direction with historical stock data

    :param main_dir: main direction
    :param sub_dir: sub directions with single stocks files
    :param sub_dir_folder: optional folder for stocks files
    :return: list with single stocks files data
    '''

    main_entry = os.listdir(main_dir + '/' + sub_dir + '/' + sub_dir_folder)
    return main_entry


#ic(get_entry_direction('data/daily/us', 'nasdaq_stocks', '1'))

