import sqlite3
from datetime import datetime
from pprint import pprint

con = sqlite3.connect('db.db')
cur = con.cursor()

ADMINS = [7137240331]

API_TOKEN = '7290212966:AAEzBfv3S-dJFUT3Tw22yd-6f1_n58H2tFg'


def get_date():
    date = str(datetime.now()).split()[0].split('-')
    date = f'{date[2]}/{date[1]}/{date[0]}'
    return date


cur.execute("""CREATE TABLE IF NOT EXISTS Users(
   user_id INTEGER,
   user_name TEXT,
   buy BOOL,
   date DATE,
   bought INTEGER,
   balance INTEGER,
   admin BOOL,
   ban BOOL,
   sent INTEGER);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS Subs(
   user_id INTEGER,
   days INTEGER,
   tariff TEXT,
   date DATE);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS Tariffs(
   name TEXT,
   days TEXT,
   description TEXT,
   price TEXT,
   work BOOL);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS Tariffs_links(
   name TEXT,
   id INTEGER);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS Admins(
   user_id INTEGER,
   date DATE,
   payments BOOL,
   feedback BOOL,
   add_admins BOOL);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS Payment_methods(
   name TEXT,
   currencies TEXT,
   commission FLOAT,
   number TEXT,
   crypto BOOL,
   work BOOL);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS Settings(
   buy BOOL,
   buy_all BOOL,
   phrase_tariff TEXT,
   helper TEXT,
   min_deposit INTEGER);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS Purchase(
   user_id INTEGER,
   date DATE,
   photo TEXT,
   tariff TEXT,
   payment_method TEXT,
   price TEXT,
   number INTEGER,
   accept BOOL,
   sent BOOL,
   admin BOOL);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS Last_check (last DATE);""")

cur.execute("""CREATE TABLE IF NOT EXISTS Not_send(
   user_id INTEGER,
   date DATE,
   photo TEXT,
   tariff TEXT,
   payment_method TEXT,
   price TEXT,
   number INTEGER,
   accept BOOL,
   sent BOOL,
   admin BOOL);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS Promo(
   name TEXT,
   skidka INTEGER);
""")

cur.execute("""CREATE TABLE IF NOT EXISTS Media(
   user_id INTEGER,
   media TEXT,
   caption TEXT,
   type TEXT,
   sent INTEGER,
   number INTEGER);
""")

con.commit()
