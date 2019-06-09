# PQL

This pregetto makes the management of the sql language more "python"

* ### CREATE TABLE
	The function ```create_table``` is like "CREATE TABLE" in sql
	and is structured like this:
	```
	create_table(table, exist=False,  **kwargs)
	```
	```table```: table name<br>
	```exist```: adds the "IF NOT EXISTS" control if param is ```True```<br>
	```**kargs```: columns of table, the key of param is the name of table
	and the value (```dict```) is the data type, in the dict key is the name of data type
	and the value dict is the value of data type, if value is ```True``` data type has no value

	#### PQL ####

	```
	>>> from PQL import PQL
	>>> sql = PYQL.("./database.db")
	>>> sql.create_table(
    ...     "prova",
    ...     exist=True,
    ...     id = {
    ...         "INTEGER": True,
    ...         "PRIMARY KEY": True
    ...     },
    ...     name = {
    ...         "VARCHAR": 255,
    ...         "NOT NULL": True,
    ...     },
    ...     bin = {
    ...         "BINARY": 8000,
    ...         "NOT NULL": True
    ...     }
    ... )
	```

	#### SQL ####

	```
	CREATE TABLE IF NOT EXISTS prova(
	    id INTEGER PRIMARY KEY,
	    name VARCHAR(255) NOT NULL,
	    bin BINARY(8000) NOT NULL
	);
	```
* ### INSERT INTO
	The function ```insert``` is like "INSERT INTO" in sql
	and is structured like this:
	```
	insert(table, columns, *values)
	```
	```table```: table name<br>
	```columns```: columns to insert<br>
	```*values```: columns value to insert

	#### PQL ####

	```
	>>> sql.insert(
    ...     "prova",
    ...     ("name", "bin"),
    ...     ("Matteo", b"binary"),
    ...     ("James", b"binary")
    ... )
	```

	#### SQL ####

	```
	INSERT INTO prova
	(nome, bin)
	VALUES
	('Matteo', b'binary'),
	('James', b'binary')
	```

* ### SELECT
	The function ```select``` is like "SELECT" in sql
	and is structured like this:
	```
	select(self, table, select="*", distinct=False, **conditions)
	```
	```table```: table name<br>
	```select```: columns to get<br>
	```distinct```: adds the "DISTINCT" control if param is ```True```<br>
	```**conditions```: conditions of query

	#### PQL ####

	```
	>>> sql.select(
    ...     "prova",
    ...     ("name", "bin"),
    ...     name = "James"
    ... )
	```

	#### SQL ####

	```
	SELECT name, bin
	FROM prova
	WHERE name = 'James'

	```
* ### UPDATE
	The function ```update``` is like "UPDATE" in sql
	and is structured like this:
	```
	update(table, columns, set, **conditions)
	```
	```table```: table name<br>
	```columns```: columns to update<br>
	```set```: new value for columns<br>
	```**conditions```: conditions of query

	#### PQL ####

	```
	>>> sql.update(
    ...     "prova",
    ...     ("name", "bin"),
    ...     ("Mike", b"binary2"),
    ...     name = "James"
    ... )
	```

	#### SQL ####

	```
	UPDATE prova
	SET nome = 'Mike', bin  b'binary2'
	WHERE name = 'James'

	```

* ### DELETE
	The function ```delete``` is like "DELETE" in sql
	and is structured like this:
	```
	delete(table, **conditions)
	```
	```table```: table name<br>
	```**conditions```: conditions of query

	#### SQL ####

	```
	>>> sql.delete(
    ...     "prova",
    ...     name = "James"
    ... )
	```

	#### SQL ####

	```
	DELETE FROM prova
	WHERE name = 'James'
	```

# Conditions

Conditions are managed like:
keys of *\*kargs are the elements to compare with the value of the **kwargs,
default operator is ```equal```
and default logic operator is ```AND```

#### SQL ####

```
>>> sql.select(
...     "prova",
...     ("name"),
...     id = 1,
...     bin = b'binary'
... )
```

#### SQL ####

```
SELECT name
FROM prova
WHERE id = '1'
AND bin = b'binary'
```

To change the operator the value is a list [operatior, value]

#### SQL ####

```
>>> sql.select(
...     "prova",
...     ("id"),
...     id = ["<>", 7]
... )
```

#### SQL ####

```
SELECT id
FROM prova
WHERE id <> '7'
```

To change the logic operator the value is a list [value, logic operator] or [operator, value, logic operator]

#### SQL ####

```
>>> sql.select(
...     "prova",
...     ("id"),
...     id = ["<>", 7, "OR"],
...     name = [
...         ["Mike", "OR"],
...         "James"
...     ]
... )
```

#### SQL ####

```
SELECT id
FROM prova
WHERE id <> '7'
OR name = 'Mike'
OR name = 'James'
```
