import psycopg2

connection = psycopg2.connect('dbname=example user=postgres password=postgres')

cursor = connection.cursor()

# cursor.execute(
#     '''
#     CREATE TABLE table2 (
#     id INTEGER PRIMARY KEY,
#     completed BOOLEAN NOT NULL DEFAULT False
#     );
#     '''
# )

# cursor.execute('INSERT INTO table2 (id, completed) VALUES (1, true);')

# cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (2, False))

cursor.execute('INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);',
               {
                   'id': 3,
                   'completed': True
               })

connection.commit()

connection.close()
cursor.close()
