from GetStockData import GetStockData, stock1
from typing import Callable


class DataSorting(GetStockData):
    """
    A class to sort the data from file
    """
    def __init__(self, main_dir: str, sub_dir: str,  file_name: str, sub_dir_folder: str = ''):
        self.main_dir = main_dir
        self.sub_dir = sub_dir
        self.sub_dir_folder = sub_dir_folder
        self.file_name = file_name
        super().__init__(
            main_dir, sub_dir, sub_dir_folder, file_name
        )

    @staticmethod
    def single_stock_data_segregation(stock_data: Callable) -> None:
        """
        Static method to get single columns from stock file

        :param stock_data: Object which finds wanted file
        :return: None
        """

        data_list: Callable = stock_data
        del data_list[0]
        stock_ticket: str = (data_list[0][0])[:-3]
        date: str = data_list[0][1]
        volume: int = data_list[0][6]
        open, high, low, close = data_list[0][2], data_list[0][3], data_list[0][4], data_list[0][5]
        day, month, year = date[-2:], date[5:7], date[:4]

        print(stock_ticket, volume)


data1 = DataSorting('data/daily/us', 'nasdaq_stocks', 'cdzi.us.txt', '1')
print(data1.single_stock_data_segregation(stock1.get_data_from_single_stock_file()))