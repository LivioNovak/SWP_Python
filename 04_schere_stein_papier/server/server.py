import sqlite3
import configparser
from flask import Flask, request, json

# flask
app = Flask(__name__)

# get config-file
config = configparser.ConfigParser()
config.read('../data/config.ini')


# ====================
# == Sqlite methods ==
# ====================

def db_connect():
    # get db-name from config
    db = config['server']['database']

    # create connection to sqlite3 database
    connection = sqlite3.connect(db)
    cursor = connection.cursor()  # create cursor to interact with db

    return connection, cursor


def init_table(t_name, cols):
    # cols: matrix for every column with every 1st entry being the name, 2nd the type of the column
    connection, cursor = db_connect()

    # create query-string
    query = f'CREATE TABLE IF NOT EXISTS {t_name}(' \
            f'id INTEGER PRIMARY KEY,'

    for c in cols:
        query += f'{c[0]} {c[1]},'
    query = query[:-1] + ');'  # close brackets (without the last ',')

    # try executing query, print message
    try:
        print(f'execute SQL statement:\n{query}')
        cursor.execute(query)
        print(f'success\n')
    except:
        print('ERROR! Could not execute SQL statement!\n')

    connection.close()


def insert_into(t_name, data):
    # data: dictionary for every entry; key = the column-name
    connection, cursor = db_connect()

    # create query-string
    query = f'INSERT INTO {t_name} ('

    for key in data:
        query += f'{key},'
    query = query[:-1] + ') VALUES ('

    for key in data:
        query += f'{data[key]},'
    query = query[:-1] + ');'

    # try executing query, print message
    try:
        print(f'execute SQL statement:\n{query}')
        cursor.execute(query)
        connection.commit()
        print(f'success\n')
    except:
        print('ERROR! Could not execute SQL statement!\n')

    connection.close()

'''
def select_last(t_name):
    connection, cursor = db_connect()

    # create query-string
    query = f'SELECT * FROM {t_name};'

    # try executing query, print message
    try:
        print(f'execute SQL statement:\n{query}')
        return cursor.execute(query)
        print(f'success\n')
    except:
        print('ERROR! Could not execute SQL statement!\n')
        return

    connection.close()
'''


# =====================
# == Flask services: ==
# =====================

@app.route('/save_stats', methods=['POST'])
def save_stats():
    data = None

    # get data from json
    if request.is_json:
        data = request.json
    else:
        # data could still be stored as json
        try:
            data = json.loads(request.data)
        except:
            return 'Content type is not supported'

    # save statistics
    insert_into('results', data['results'])
    insert_into('signs', data['signs'])

    # return data
    return ''   # return nothing


# ==================
# == other & main ==
# ==================

def init_db():
    # create result table
    cols = [['win', 'INTEGER'], ['draw', 'INTEGER'], ['lose', 'INTEGER']]
    init_table('results', cols)

    # create sign table
    cols = [['sc', 'INTEGER'], ['p', 'INTEGER'], ['r', 'INTEGER'], ['l', 'INTEGER'], ['sp', 'INTEGER']]
    init_table('signs', cols)


if __name__ == '__main__':
    init_db()  # create tables of db
    app.run(debug=True)  # start flask-server
