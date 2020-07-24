import sqlite3
import datetime


def add_scan(flavor, sale_price, sale_text):
    conn = sqlite3.connect('protein.db')
    c = conn.cursor()

    today = datetime.date.today()
    params = (flavor, sale_price, today, sale_text)

    c.execute("SELECT * FROM scans WHERE flavor = ? AND sale_price = ? AND date = ? AND sale_text = ?", params)

    if len(c.fetchall()) == 0:
        c.execute("INSERT INTO scans VALUES (?,?,?,?)", params)

    conn.commit()
    conn.close()
    