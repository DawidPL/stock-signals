import os
from icecream import ic
from typing import Callable, Any


def get_entry_direction(main_dir: str, sub_dir: str, sub_dir_folder: str = '') -> str:
    ''' Return direction with historical stock data

    :param main_dir: main direction
    :param sub_dir: sub directions with single stocks files
    :param sub_dir_folder: optional inner folder for stocks files
    :return: path to stocks files
    '''

    absolute_path = os.path.dirname(__file__)
    relative_path = main_dir + '/' + sub_dir + '/' + sub_dir_folder
    full_path = os.path.join(absolute_path, relative_path)

    return full_path


def get_single_stock_files(file_name: str, entry_dir: Callable) -> str:
    '''

    :param file_name: file name with stock historical data
    :param entry_dir: main direction with single stock files data
    :return: single stock file
    '''

    single_stock_dir: str = entry_dir + '/' + file_name
    return single_stock_dir


def get_data_from_single_stock_file(file_dir: str) -> list[list[str]]:
    '''
    Retrieve data from single stock file
    :param file_dir: file directory
    :return: list with stock data
    '''

    lines: list[list[str]] = []
    with open(file_dir) as f:
        for line in f:
            row = line.split(',')
            lines.append(row[0:1] + row[2:3] + row[4:9])
    return lines



#ic(get_entry_direction('data/daily/us', 'nasdaq_stocks', '1'))
#ic(get_single_stock_files('aaciu.us.txt', get_entry_direction('data/daily/us', 'nasdaq_stocks', '1')))
ic(get_data_from_single_stock_file(get_single_stock_files('aaci.us.txt', get_entry_direction('data/daily/us', 'nasdaq_stocks', '1'))))
