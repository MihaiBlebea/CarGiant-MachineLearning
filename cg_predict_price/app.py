from cg_predict_price.scraper import scrape_url
from cg_predict_price.writer import write_excel, read_excel
from cg_predict_price.serializer import save_obj, load_obj

from sklearn import linear_model
from sklearn.model_selection import train_test_split

from pandas import Series, DataFrame
import numpy as np
from pathlib import Path


class CGData:

    def __init__(self, url, feature_columns, label_column, encoder, max_pages = 2):
        self.feature_columns = feature_columns
        self.label_column = label_column
        self.url = url
        self.max_pages = max_pages
        self.encoder = encoder

        self.columns = self.feature_columns + [ self.label_column ]
        self.df = None


    def load_data(self, file_path):
        excel_file = Path(file_path)
        return read_excel(file_path)


    def load_or_scrape_data(self, file_path):

        excel_file = Path(file_path)

        if excel_file.exists():
            df = self.load_data(file_path)
        else:
            df = DataFrame( scrape_url(self.url, self.max_pages) )
            write_excel(file_path, df)

        df_selected = df[self.columns]
        self.df = df_selected.dropna()


    def get_features(self):
        if self.df is None:
            pass
        else:
            df_features = self.df[self.feature_columns]
            return self.encoder.encode_to_integer(df_features, self.feature_columns)


    def get_labels(self):
        if self.df is None:
            pass
        else:
            return self.df[self.label_column]


class CGPredict:

    def __init__(self, df_features, df_labels):
        self.df_features_train, self.df_features_test, self.df_labels_train, self.df_labels_test = train_test_split(df_features, df_labels, test_size=0.2, shuffle=True)
        self.model = None


    def train(self):
        cls = linear_model.LinearRegression()
        model = cls.fit(self.df_features_train, self.df_labels_train)
        return model


    def train_or_load(self, file_path):
        model_file = Path(file_path)

        if model_file.exists():
            model = load_obj(file_path)
        else:
            model = self.train()
            save_obj(model, file_path)

        self.model = model


    def predict(self, df_features = None):
        if df_features == None:
            df_features = self.df_features_test

        if self.model is None:
            pass
        else:
            prediction = self.model.predict(df_features)
            return Series(np.array(prediction).astype(int))


    def get_score(self):
        if self.model is None:
            pass
        else:
            return self.model.score(self.df_features_test, self.df_labels_test)
