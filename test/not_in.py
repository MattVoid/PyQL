from PyQL import PyQL

# connect to database
sql = PyQL("./database.db")

#  create table
sql.create_table(
    "try",
    exist=True,
    id = {
        "INTEGER": True,
        "PRIMARY KEY": True
    },
    nome = {
        "VARCHAR": 255,
        "NOT NULL": True,
    },
    surname = {
        "VARCHAR": 255,
        "NOT NULL": True
    },
    bin = {
        "BINARY": 8000,
        "NOT NULL": True
    }
)

# insert new values
sql.insert(
    "try",
    ("nome", "surname", "bin"),
    ("name1", "surname1", b"binary1"),
    ("name2", "surname2", b"binary2"),
    ("name3", "surname3", b"binary3"),
    ("name4", "surname4", b"binary4"),
    ("name5", "surname5", b"binary5"),
)

search = sql.select(
    "try",
    ("id"),
    id = ["<", 3]
)

sql.update(
    "try",
    ("nome", "surname", "bin"),
    ("name_changed", "surname_changed", b"binary_change"),
    id = ["NOT IN", search]
)

search = sql.select(
    "try"
)

for i in search:
    print(i)
