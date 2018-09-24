from scraper import process_url
from writer import write_excel, write_txt, read_excel, write_csv, read_csv
from machine_learning import train_predict, pick_columns, encode_columns, pick_price, split_data, remove_incomplete
import pandas as pd
import random


initial_url = 'https://www.cargiant.co.uk/search'

columns = [
    'Body Type',
    'Engine size',
    'Fuel',
    'CO',
    'Car'
]

user_car = {
    'Body Type': 'SUV',
    'Engine size': '2.4',
    'Fuel': 'Petrol',
    'CO': '0.133',
    'Car': 'Renault Scenic XMod'
}


# Process the car giant data and scrape the site
data = process_url(initial_url)
random.shuffle(data)
write_excel('data', data)

data = remove_incomplete(data, columns)
labels = pick_price(data)
data = pick_columns(data, columns)
features = encode_columns(data)

# write_excel('features', features)
# write_excel('labels', labels)

# Split data into training and testing data
features = split_data(features)
labels = split_data(labels)

prediction = train_predict(pd.DataFrame(features['train']), labels['train'], features['test'])

print(list(prediction))
print(labels['test'])
