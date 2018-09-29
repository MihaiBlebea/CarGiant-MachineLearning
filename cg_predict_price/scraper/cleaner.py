
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
