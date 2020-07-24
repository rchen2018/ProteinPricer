import sqlite3
import datetime
from operator import itemgetter


def add_scan(flavor, sale_price, sale_text):
    conn = sqlite3.connect('protein.db')
    c = conn.cursor()

    today = datetime.date.today()
    params = (flavor, sale_price, today, sale_text)

    c.execute("SELECT * FROM scans "
              "WHERE flavor = ? "
              "AND sale_price = ? "
              "AND date = ? "
              "AND sale_text = ?", params)

    if len(c.fetchall()) == 0:
        c.execute("INSERT INTO scans VALUES (?,?,?,?)", params)

    conn.commit()
    conn.close()

    analyze_scan(flavor, sale_price)


def analyze_scan(flavor, sale_price):
    conn = sqlite3.connect('protein.db')
    c = conn.cursor()

    c.execute("SELECT ROWID, flavor, sale_price, date FROM scans "
              "WHERE flavor = ? "
              "AND sale_price <= ?", (flavor, sale_price))

    cheaper_list = c.fetchall()
    if len(cheaper_list) > 0:
        cheapest_price = min(x[2] for x in cheaper_list)
        cheapest = [x for x in cheaper_list if (x[2] == cheapest_price)]
        if sale_price == cheapest_price:
            print('$' + str(sale_price) + ' is tied with the historical cheapest price for an 11lb bag of ' + flavor)
        else:
            print('Now may not be the best time to buy. The historical cheapest price for an 11lb bag of ' + flavor + ' is $' + str(cheapest_price))
    else:
        print('$' + str(sale_price) + ' is the historical cheapest price for an 11lb bag of ' + flavor)

    conn.close()
