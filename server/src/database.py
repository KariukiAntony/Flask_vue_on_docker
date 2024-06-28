from flask import g, current_app
import sqlite3
import psycopg2
from termcolor import colored

""" CONSTANTS """
TABLE = "book"
FILENAME = "books.sql"


def get_db_connection():
    DATABASE_URL = current_app.config.get("DATABASE_URL")
    db = getattr(g, "_database", None)
    if db is None:
        try:
            if DATABASE_URL.startswith("sqlite"):
                db = g._database = sqlite3.connect("books.sqlite")

            elif DATABASE_URL.startswith("postgresql"):
                db = g._database = psycopg2.connect(DATABASE_URL)
            else:
                pass

        except Exception as e:
            print(colored(f"[-] error connecting to db: {e}", "red"))

    return db


def close_conn():
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


class Database(object):
    def __init__(self) -> None:
        self.conn = None
        self.cursor = None
        self.table = TABLE
        self.filename = FILENAME
        try:
            self.conn = get_db_connection()
            self.cursor = self.conn.cursor()
            self.create_tables()

        except Exception as error:
            print(colored(f"[-] An error occured: {error}", "red"))

    def create_tables(self):
        try:
            with current_app.open_resource(self.filename, mode="r") as file:
                self.cursor.execute(file.read())
                print(colored("[+] tables created successfully..", "green"))
            self.conn.commit()
        except Exception as error:
            print(colored(f"[-] Error while creating table: {error}", "red"))

    def get_all_books(self) -> list:
        sql = """ SELECT * FROM {} ORDER BY id DESC;""".format(self.table)
        self.cursor.execute(sql)
        raw_data = self.cursor.fetchall()
        return [self.to_json(book) for book in raw_data]

    def get_a_book(self, id):
        sql = """SELECT * FROM {} WHERE id={};""".format(self.table, id)
        self.cursor.execute(sql)
        data = self.cursor.fetchone()
        return self.to_json(data)

    def add_new_book(self, data: dict) -> None:
        sql = (
            """ INSERT INTO {} (title, author, read)VALUES('{}', '{}', '{}');""".format(
                self.table, data.get("title"), data.get("author"), data.get("read")
            )
        )
        self.cursor.execute(sql)
        self.conn.commit()

    def update_book(self, data: dict) -> None:
        sql = (
            """UPDATE {} SET title='{}', author='{}', read='{}' WHERE id={};""".format(
                self.table,
                data.get("title"),
                data.get("author"),
                data.get("read"),
                data.get("id"),
            )
        )
        self.cursor.execute(sql)
        self.conn.commit()

    def delete_book(self, id: int) -> None:
        sql = """DELETE FROM {} WHERE id={};""".format(self.table, id)
        self.cursor.execute(sql)
        self.conn.commit()

    def to_json(self, data: dict) -> dict:
        return {"id": data[0], "title": data[1], "author": data[2], "read": data[3]}
