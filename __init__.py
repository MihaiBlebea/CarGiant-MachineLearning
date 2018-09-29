from app import CGData, CGPredict
from encoder import CGEncode

cg_encode = CGEncode('data/encode_dict.json')


cg_data = CGData('https://www.cargiant.co.uk/search', ['Body Type', 'Engine size', 'Fuel', '0 to 62 mph (secs)', 'Car'], 'Price', cg_encode)
cg_data.load_or_scrape_data('data/car_data.xlsx')
df_features = cg_data.get_features()
df_labels = cg_data.get_labels()

print(df_features)

cg_predict = CGPredict(df_features, df_labels)
cg_predict.train_or_load('data/car_price.model')
prediction = cg_predict.predict()
score = cg_predict.get_score()
print(prediction)

print(score)
