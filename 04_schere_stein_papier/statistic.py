import json
import requests
import configparser

# config-file
config = configparser.ConfigParser()
config.read('data/config.ini')


def get_stats():
    f = open('./data/stats.txt', "r")
    stats = json.loads(f.read())
    f.close()

    return stats


# unused
def increase_stats(stats, *keys):
    for key in keys:
        stats[key[0]][key[1]] += 1

    return stats


def save_stats(stats):
    f = open('./data/stats.txt', 'w')
    f.write(json.dumps(stats))


def save_in_db(stats):
    # get url from config-file
    url = config['client']['url']

    # call flask-service
    res = requests.post(url, json=stats)
    print(res.text)


