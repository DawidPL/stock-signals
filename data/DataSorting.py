from GetStockData import GetStockData, stock1
from typing import Callable


class DataSorting(GetStockData):
    """
    A class to sort the data from file
    """
    def __init__(self, main_dir: str, sub_dir: str,  file_name: str,
                 stock_data_object: Callable = stock1.get_data_from_single_stock_file(),
                 sub_dir_folder: str = '') -> None:

        super().__init__(
            main_dir, sub_dir, sub_dir_folder, file_name,
        )

        self.stock_data_object = stock_data_object

    def stock_data_segregation(self) -> dict:
        """
        Static method to get single columns from stock file

        :return: dict with data from file
        """

        data_list: list[list[str]] = self.stock_data_object
        stock_ticket: str = (data_list[0][0])[:-3]
        date: str = data_list[0][1]
        volume: str = data_list[0][6]
        open, high, low, close = data_list[0][2], data_list[0][3], data_list[0][4], data_list[0][5]
        day, month, year = date[-2:], date[4:6], date[:4]
        data_dict = {'stock_ticket': stock_ticket, 'date': date, 'volume': volume, 'open': open, 'high': high,
                     'low': low, 'close': close, 'formatted_date': day + '.' + month + '.' + year}
        return data_dict

    def calculate_average_volume_from_given_period(self, period: int, start_from_last: bool) -> float:
        """
        Method to calculate average stock volume from given period
        :param period: range in day
        :param start_from_last: start with last day quote or from historical start quote
        :return: int: average volume
        """
        data_list: list[list[str]] = self.stock_data_object
        data_list_len: int = len(data_list) - 1
        vol_sum_from_last: int = 0
        counter: int = 0
        if start_from_last:
            for i in range(data_list_len, data_list_len - period, -1):
                vol_sum_from_last += int(data_list[i][6])
                counter += 1
        else:
            for i in range(0, period):
                vol_sum_from_last += int(data_list[i][6])
                counter += 1
        return vol_sum_from_last / counter


data1 = DataSorting('data/daily/us', 'nasdaq_stocks', 'aaci.us.txt', sub_dir_folder='1')
print(data1.calculate_average_volume_from_given_period(10, True))