import os


class GetStockData:
    """
    A class to get data from single stock files. This files contains historical data.

    """

    def __init__(self, main_dir: str, sub_dir: str,  file_name: str, sub_dir_folder: str = ''):
        """
        :param main_dir: main direction
        :param sub_dir: sub directions with single stocks files
        :param file_name: file name with stock historical data
        :param sub_dir_folder: optional inner folder for stocks files
        """

        self.main_dir = main_dir
        self.sub_dir = sub_dir
        self.sub_dir_folder = sub_dir_folder
        self.file_name = file_name

    def get_entry_direction(self) -> str:
        """ Function to get main path with all stock data folders

        :return: str: relative path to folders
        """

        absolute_path = os.path.dirname(__file__)
        relative_path = self.main_dir + '/' + self.sub_dir + '/' + self.sub_dir_folder
        full_path = os.path.join(absolute_path, relative_path)
        return full_path

    def get_single_stock_file(self) -> str:
        """ Function to get single file with stock data

        :return: str:  path to wanted single .txt file
        """

        single_stock_dir: str = self.get_entry_direction() + '/' + self.file_name
        return single_stock_dir

    def get_data_from_single_stock_file(self) -> list[list[str]]:
        """ Function to open file and get the data

        :return: list[list[str]]: list with all data from file
        """

        file_dir = self.get_single_stock_file()
        lines: list[list[str]] = []
        with open(file_dir) as f:
            for line in f:
                row = line.split(',')
                lines.append(row[0:1] + row[2:3] + row[4:9])
        return lines


stock1 = GetStockData('data/daily/us', 'nasdaq_stocks', 'cdzi.us.txt', '1')

print(stock1.get_entry_direction())
print(stock1.get_data_from_single_stock_file())