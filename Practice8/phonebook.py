from connect import connect
from config import load_config

config = load_config()

def search_pattern(pattern):
    with connect(config) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM get_contacts_by_pattern(%s)", (pattern,))
            return cur.fetchall()

def paginate(limit, offset):
    with connect(config) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
            return cur.fetchall()

def add_or_update(name, phone):
    with connect(config) as conn:
        with conn.cursor() as cur:
            cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
        conn.commit()

def add_many(names, phones):
    with connect(config) as conn:
        with conn.cursor() as cur:
            cur.execute("CALL bulk_upsert_contacts(%s, %s, %s)", (names, phones, None))
        conn.commit()

def delete(name=None, phone=None):
    with connect(config) as conn:
        with conn.cursor() as cur:
            cur.execute("CALL delete_contact(%s, %s)", (name, phone))
        conn.commit()


if __name__ == "__main__":
    print(search_pattern("Ilya"))
    add_or_update("Dana", "87005556677")
    print(paginate(5, 0))
    delete(name="Aigerim")