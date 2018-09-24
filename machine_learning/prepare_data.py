from machine_learning.price_model import encode_row


# Encode string data to integers
def encode_columns(data):
    encoded_datas = []
    result = []
    columns = data[0].keys()
    for column in columns:

        foo = [car[column] for car in data]
        if check_integer(foo[0]) == True:
            new_columns = transform_list_integer(foo)
        elif check_float(foo[0]) == True:
            new_columns = transform_list_float(foo)
        else:
            new_columns = encode_row(foo)

        encoded_datas.append(list(new_columns))

    for index in range(0, len(data)):
        car = [features[index] for features in encoded_datas]
        result.append(car)

    return result


def remove_incomplete(data, columns):
    result = []
    columns.append('Price')

    for car in data:
        new_car = {}
        should_include = True
        for column in columns:
            if column in car:
                if car[column] != '' and car[column] != 'N/A':
                    new_car[column] = car[column]
            else:
                should_include = False

        if should_include == True:
            result.append(new_car)

    return result


def pick_columns(data, columns):
    result = []
    for car in data:
        del car['Price']
        new_car = {}
        for column in columns:
            if column in car:
                new_car[column] = car[column]

        result.append(new_car)

    return result


# Pluck features as price from the data scraped
def pick_price(data):
    result = []
    for car in data:
        result.append(int(car['Price']))

    return result


def transform_list_integer(data):
    new_data = []
    for item in data:
        new_data.append(int(item))
    return new_data


def transform_list_float(data):
    new_data = []
    for item in data:
        new_data.append(float(item))
    return new_data


def check_integer(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def check_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def split_data(data):
    training_data = []
    testing_data = []
    train_length = int(len(data) * 3 / 4)
    for index, car in enumerate(data):
        if index < train_length:
            training_data.append(car)
        else:
            testing_data.append(car)
    return {
        'train': training_data,
        'test': testing_data
    }
