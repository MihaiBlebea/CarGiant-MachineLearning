import pandas as pandas
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as numpy


#{'a':[1,3,5,7,4,5,6,4,7,8,9], 'b':[3,5,6,2,4,6,7,8,7,8,9]}

def write_excel(file_name, data):
    data_frame = pandas.DataFrame(data)

    writer = ExcelWriter(file_name + '.xlsx')
    data_frame.to_excel(writer, 'Sheet1', index = False)
    writer.save()

def read_excel(file_name):
    data_frame = pandas.read_excel(file_name + '.xlsx', sheet_name='Sheet1')
    return data_frame.to_dict(orient = 'records')
