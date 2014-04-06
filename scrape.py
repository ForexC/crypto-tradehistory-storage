from Cryptsy import Api
import sqlite3

def create_database(exchange, marketcode):
    if exchange == 'cryptsy':
        exchange_api = Api('YOURKEY', 'YOURSECRETKEY')
        db_name = 'db/cryptsy_' + marketcode + '.db'

        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS market_history
             (tradeid real, datetime text, tradeprice real, initiate_ordertype text, total real, quantity real)''')

        conn.commit()
        conn.close()


def scrape_market(exchange, marketid, marketcode):
    create_database(exchange, marketcode)

    if exchange == 'cryptsy':
        exchange_api = Api('YOURKEY', 'YOURSECRETKEY')
        db_name = 'db/cryptsy_' + marketcode + '.db'

        conn = sqlite3.connect(db_name)
        c = conn.cursor()

        data = exchange_api.market_trades(marketid)
        for d in data['return']:

             c.execute("SELECT tradeid FROM market_history WHERE tradeid = ?", (d['tradeid'],))
             data=c.fetchall()
             if len(data)==0:
                 c.execute("INSERT INTO market_history (tradeid, datetime, tradeprice, initiate_ordertype, total, quantity) values (?, ?, ?, ?, ?, ?)",
                             (d['tradeid'], d['datetime'], d['tradeprice'], d['initiate_ordertype'], d['total'], d['quantity']))

        conn.commit()
        conn.close()


def scrape_all(exchange):
    if exchange == 'cryptsy':
        exchange_api = Api('YOURKEY', 'YOURSECRETKEY')
        data = exchange_api.market_data(v2=True)

        for label in data['return']['markets']:
            marketid = data['return']['markets'][label]['marketid']
            marketcode = data['return']['markets'][label]['primarycode'] + data['return']['markets'][label]['secondarycode']
            marketcode = marketcode.lower()
            scrape_market('cryptsy', marketid, marketcode)
