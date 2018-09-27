import pickle

def save_model(model):
    pickle.dump(model, open('data/car_price.model', 'wb'))

def load_model():
    return pickle.load(open('data/car_price.model', 'rb'))
