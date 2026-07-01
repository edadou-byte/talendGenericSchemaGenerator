from processors.csv_processor import get_columns_types
from processors.csv_processor import open_csv_file
from processors.generic_schema_generator import create_xml_rows

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cols = open_csv_file("C:\\Users\\edadou.ext\\PycharmProjects\\talendGenericSchemaGenerator\\tests\\test.csv")
    print(get_columns_types(cols))
    rows = create_xml_rows(get_columns_types(cols))

    for row in rows:
        print(row.write_xml())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
