#!/usr/bin/python
import pandas as pd
import sqlalchemy
import sqlalchemy_utils

DB_USER = "root"
DB_PASSWORD = "my-secret-pw"
DB_HOST = "127.0.0.1"
DB_PORT = 3306
DB_BASE = "test"

CSV_FILE = "1.csv"

data = pd.read_csv(CSV_FILE, sep="\t", on_bad_lines="skip")

engine = sqlalchemy.create_engine(f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_BASE}")

if not sqlalchemy_utils.database_exists(engine.url):
    sqlalchemy_utils.create_database(engine.url)

data.to_sql("tuturu", engine, if_exists="replace")
