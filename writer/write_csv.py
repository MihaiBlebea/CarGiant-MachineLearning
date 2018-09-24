import csv


def write_csv(file_name, data):
    with open(file_name + '.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')

        writer.writerow(data[0].keys())
        for car in data:
            writer.writerow(car.values())


def read_csv(file_name):
    with open(file_name + '.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        headers = next(reader, None)
        print(len(headers))
        result = []

        for index, value in enumerate(reader, start=0):
            if index != 0:
                row = {}

                for key, header in enumerate(headers):
                    row[header] = value[key]

                result.append(row)

        return result
