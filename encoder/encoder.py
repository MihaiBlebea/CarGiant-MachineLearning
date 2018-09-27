import numpy as np
from pandas import DataFrame, Series


# Separate the function that creates the dict from the main encode function


def encode_to_integer(df, columns):
    for column in columns:
        df_no_dupli = df.drop_duplicates(column)
        df_no_dupli_indexed = df_no_dupli.assign(encode_values_int = Series( np.arange( 1, len(df_no_dupli.index) + 1 )).values )
        df_two_columns = df_no_dupli_indexed[[column, 'encode_values_int']]

        d = {}
        for index, row in df_two_columns.iterrows():
            d[row[column]] = row['encode_values_int']

        for index, row in df.iterrows():
            df.loc[index, column] = d[row[column]]

    return df
