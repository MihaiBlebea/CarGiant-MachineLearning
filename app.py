from scraper import scrape_url
from writer import write_excel, read_excel, write_txt, write_csv, read_csv
from encoder import encode_to_integer

from sklearn import tree
from sklearn.utils import shuffle

from pandas import Series, DataFrame
from pathlib import Path


initial_url = 'https://www.cargiant.co.uk/search'

columns = [
    'Body Type',
    'Engine size',
    'Fuel',
    '0 to 62 mph (secs)',
    'Car'
]

excel_file = Path('data/car_data.xlsx')

# If excel file exists then take data from excel,
# If not, then scrape the site
if excel_file.exists():
    df = read_excel('data/car_data.xlsx')
else:
    # Scrape site
    data = scrape_url(initial_url)

    # Transform data to DataFrame
    df = DataFrame(data)

    # Save data to excel
    write_excel('data/car_data.xlsx', df)

# Shuffle the DataFrame before predicting the price
df = shuffle(df)
df = df.reset_index(drop=True)

# Select the columns plus 'Price' from DataFrame
df_selected = df[columns + ['Price']]

# Take out the incomplete rows from the DataFrame
df_not_null = df_selected.dropna()

# Select columns from the complete DataFrame
df_features = df_not_null[columns]

# Encode labels from string to integer
df_features = encode_to_integer(df_features, ['Body Type', 'Fuel', 'Car'])
print(df_features)

# Select the 'Price' column from the complete DataFrame
df_labels = df_not_null['Price']

# Figure out how many rows are for training and how many are for testing
count_rows = len(df_features.index)
train_length = int(count_rows * 70/100)
test_length = count_rows - train_length

# Get the DataFrame for training
df_features_training = df_features[ 0:train_length ]
df_labels_training = df_labels[ 0:train_length ]

# Get the DataFrame for testing
df_features_testing = df_features[ train_length:count_rows ]
df_labels_testing = df_labels[ train_length:count_rows ]


# Train model with training features and training labels
cls = tree.DecisionTreeClassifier()
cls.fit(df_features_training, df_labels_training)

# Give the model some prediction data labels from testing data
prediction = cls.predict(df_features_testing)

# Print result and compare testing data with predition
print(Series(prediction))
print(df_labels_testing.reindex())
