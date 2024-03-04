import json


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
