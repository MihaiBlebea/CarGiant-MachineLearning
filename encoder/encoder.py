import numpy as np
from pandas import DataFrame, Series

# Create the dict for encoding the items in the DataFrame
def create_encode_dict(df, columns):
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
def encode_to_integer(df, columns):
    encode_dict = create_encode_dict(df, columns)
    for column in columns:
        for index, row in df.iterrows():
            df.loc[index, column] = encode_dict[column][row[column]]

    return df
