from scraper.scraper import next_url, scrape_url
from scraper.cleaner import remove_money_sign, remove_asterix, remove_comma


def process_url(initial_url):
    data = []
    for i in range(1, 10):
        print('Started scraping page nr: ' + str(i))
        url = next_url(initial_url, i)
        data = data + parse_url(url)

    for car in data:
        car = remove_money_sign(car)
        car = remove_asterix(car)
        car = remove_comma(car)

    return data
