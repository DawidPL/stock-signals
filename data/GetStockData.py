import os

class GetStockData:
    def __init__(self, main_dir: str, sub_dir: str,  file_name: str, sub_dir_folder: str = ''):
        self.main_dir = main_dir
        self.sub_dir = sub_dir
        self.sub_dir_folder = sub_dir_folder
        self.file_name = file_name

    def get_entry_direction(self) -> str:
        '''
        Return direction with historical stock data

        :param main_dir: main direction
        :param sub_dir: sub directions with single stocks files
        :param sub_dir_folder: optional inner folder for stocks files
        :return: path to stocks files
        '''

        absolute_path = os.path.dirname(__file__)
        relative_path = self.main_dir + '/' + self.sub_dir + '/' + self.sub_dir_folder
        full_path = os.path.join(absolute_path, relative_path)
        return full_path

    def get_single_stock_file(self) -> str:
        '''

        :param file_name: file name with stock historical data
        :param entry_dir: main direction with single stock files data
        :return: single stock file
        '''

        single_stock_dir: str = self.get_entry_direction() + '/' + self.file_name
        return single_stock_dir

    def get_data_from_single_stock_file(self) -> list[list[str]]:
        '''
        Retrieve data from single stock file
        :param file_dir: file directory
        :return: list with stock data
        '''

        file_dir = self.get_single_stock_file()
        lines: list[list[str]] = []
        with open(file_dir) as f:
            for line in f:
                row = line.split(',')
                lines.append(row[0:1] + row[2:3] + row[4:9])
        return lines

stock1 = GetStockData('data/daily/us', 'nasdaq_stocks', 'aaci.us.txt', '1')

print(stock1.get_entry_direction())
print(stock1.get_data_from_single_stock_file())