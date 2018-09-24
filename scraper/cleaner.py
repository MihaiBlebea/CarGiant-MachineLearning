
def remove_money_sign(car):
    for column in car:
        if '£' in car[column]:
            car[column] = car[column].replace('£', '')
    return car


def remove_asterix(car):
    for column in car:
        if '*' in car[column]:
            car[column] = car[column].replace('*', '').strip()
    return car


def remove_comma(car):
    for column in car:
        if ',' in car[column]:
            car[column] = car[column].replace(',', '')
    return car


def remove_key(data, key):
    r = dict(data)
    del r[key]
    return r


# Remove cars that contain incomplete column data or 'N/A'
def remove_incomplete_data(data, columns):
    complete_data = []
    for car in data:
        for column in columns:
            if column in car and car[column] != 'N/A':
                complete_data.append(car)

    return complete_data
