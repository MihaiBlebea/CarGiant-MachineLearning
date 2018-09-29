import pandas as pd
from pandas import ExcelWriter


def write_excel(file_name, data):
    data_frame = pd.DataFrame(data)

    writer = ExcelWriter(file_name)
    data_frame.to_excel(writer, 'Sheet1', index = False)
    writer.save()

def read_excel(file_name):
    return pd.read_excel(file_name, sheet_name='Sheet1')
