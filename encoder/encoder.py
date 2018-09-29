import numpy as np
from pandas import DataFrame, Series
from pathlib import Path
import json


class CGEncode:

    def __init__(self, file_path):
        self.file_path = file_path
        self.encode_dict = None


    # Create the dict for encoding the items in the DataFrame
    def create_encode_dict(self, df, columns):
        encode_dict = {}
        for column in columns:
            df_no_dupli = df.drop_duplicates(column)
            df_no_dupli_indexed = df_no_dupli.assign(encode_values_int = Series( np.arange( 1, len(df_no_dupli.index) + 1 )).values )
            df_two_columns = df_no_dupli_indexed[[column, 'encode_values_int']]

            d = {}
            for index, row in df_two_columns.iterrows():
                d[row[column]] = row['encode_values_int']

            encode_dict[column] = d
        return encode_dict


    # Encode the items in the Data Frame using the dict
    def encode_to_integer(self, df, columns):

        string_columns = self.check_columns(df, columns)

        dict_file = Path(self.file_path)

        if dict_file.exists():
            with open(self.file_path, 'r') as read_file:
                encode_dict = json.load(read_file)
        else:
            encode_dict = self.create_encode_dict(df, columns)
            with open(self.file_path, 'w') as outfile:
                json.dump(encode_dict, outfile)

        for column in string_columns:
            for index, row in df.iterrows():
                df.loc[index, column] = encode_dict[column][row[column]]

        return df


    def check_columns(self, df, columns):
        string_columns = []
        for column in columns:
            if self.check_integer(df[column][0]) is False and self.check_float(df[column][0]) is False:
                string_columns.append(column)
        return string_columns


    def check_integer(self, value):
        try:
            int(value)
            return True
        except ValueError:
            return False


    def check_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False
