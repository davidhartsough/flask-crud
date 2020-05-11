from db import get_db


def get_all_things():
    db = get_db()
    things = db.execute(
        "SELECT t.id, title, created, stuff, num"
        " FROM thing t"
        " ORDER BY created DESC"
    ).fetchall()
    return things


def get_thing(id):
    db = get_db()
    thing = db.execute(
        "SELECT t.id, title, created, stuff, num"
        " FROM thing t"
        " WHERE t.id = ?",
        (id,),
    ).fetchone()
    return thing


def create_thing(title, stuff, num):
    db = get_db()
    db.execute(
        "INSERT INTO thing (title, stuff, num) VALUES (?, ?, ?)",
        (title, stuff, num),
    )
    db.commit()


def update_thing(id, title, stuff, num):
    db = get_db()
    db.execute(
        "UPDATE thing SET title = ?, stuff = ?, num = ? WHERE id = ?",
        (title, stuff, num, id),
    )
    db.commit()


def delete_thing(id):
    db = get_db()
    db.execute("DELETE FROM thing WHERE id = ?", (id,))
    db.commit()
