import sqlite3


connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER
)
''')
# cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')
# for i in range(1, 11):
#     cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)',
#                 (f'User{i}', f'example{i}@gmail.com', f'{i * 10}', '1000'))

# cursor.execute('UPDATE Users SET balance = ? WHERE username = ?',
#                (500, 'User2'))
# cursor.execute('UPDATE Users SET balance = ? WHERE username = ?',
#                (500, 'User4'))
# cursor.execute('UPDATE Users SET balance = ? WHERE username = ?',
#                (500, 'User6'))
# cursor.execute('UPDATE Users SET balance = ? WHERE username = ?',
#                (500, 'User8'))
# cursor.execute('UPDATE Users SET balance = ? WHERE username = ?',
#                (500, 'User10'))
# cursor.execute('DELETE FROM Users WHERE username = ?', ('User1',))
# cursor.execute('DELETE FROM Users WHERE username = ?', ('User4',))
# cursor.execute('DELETE FROM Users WHERE username = ?', ('User7',))
# cursor.execute('DELETE FROM Users WHERE username = ?', ('User10',))
cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60,))
users = cursor.fetchall()
for user in users:
    print(user)



connection.commit()
connection.close()