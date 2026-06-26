from processors.csv_processor import get_columns_types
from processors.csv_processor import open_csv_file

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cols = open_csv_file("C:\\Users\\edadou.ext\\PycharmProjects\\talendGenericSchemaGenerator\\tests\\test.csv")
    get_columns_types(cols)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
