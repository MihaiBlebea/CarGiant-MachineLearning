import pickle


def save_obj(obj, file_path):
    pickle.dump(obj, open(file_path, 'wb'))

def load_obj(file_path):
    return pickle.load(open(file_path, 'rb'))
