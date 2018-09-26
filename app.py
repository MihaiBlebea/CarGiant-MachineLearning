from scraper import scrape_url
from writer import write_excel, read_excel
from encoder import encode_to_integer
from model import save_model, load_model

from sklearn import tree, linear_model
from sklearn.model_selection import train_test_split

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
model_file = Path('data/model')


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

# Select the columns plus 'Price' from DataFrame
df_selected = df[columns + ['Price']]

# Take out the incomplete rows from the DataFrame
df_not_null = df_selected.dropna()

# Select columns from the complete DataFrame
df_features = df_not_null[columns]

# Encode labels from string to integer
df_features = encode_to_integer(df_features, ['Body Type', 'Fuel', 'Car'])
# print(df_features)

#Select the 'Price' column from the complete DataFrame
df_labels = df_not_null['Price']

# Split data in train and test
df_features_train, df_features_test, df_labels_train, df_labels_test = train_test_split(df_features, df_labels, test_size=0.2, shuffle=True)

# Train model with training features and training labels
cls = linear_model.LinearRegression()
# cls = tree.DecisionTreeClassifier()
model = cls.fit(df_features_train, df_labels_train)

# Check if the model is saved to disk or not
if model_file.exists():
    # Load model from disk file
    loaded_model = load_model()
else:
    # Save the trained model to disk
    save_model(model)

# Give the model some prediction data labels from testing data
prediction = cls.predict(df_features_test)

# Print result and compare testing data with predition
print(Series(prediction))
print(df_labels_test)

print('Score is ', cls.score(df_features_test, df_labels_test))
print('Saved model ', loaded_model.score(df_features_test, df_labels_test))
