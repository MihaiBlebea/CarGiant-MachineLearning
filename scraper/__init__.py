from scraper.scraper import next_url, scrape
from scraper.cleaner import remove_money_sign, remove_asterix, remove_comma


def scrape_url(initial_url):
    data = []
    for i in range(1, 2):
        print('Started scraping page nr: ' + str(i))
        url = next_url(initial_url, i)
        data = data + scrape(url)

    for car in data:
        car = remove_money_sign(car)
        car = remove_asterix(car)
        car = remove_comma(car)

    return data
