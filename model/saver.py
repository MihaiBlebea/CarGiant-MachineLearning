import pickle

def save_model(model):
    pickle.dump(model, open('data/model', 'wb'))

def load_model():
    return pickle.load(open('data/model', 'rb'))
