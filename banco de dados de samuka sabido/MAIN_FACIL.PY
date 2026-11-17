import sqlite3

banco = sqlite3.connect("primeiro_banco.db")

cursor = banco.cursor()

#cursor.execute("CREATE TABLE aluno(Nome text, idade integer, email text)")

#cursor.execute("INSERT INTO aluno VALUES('Tirulipa', 20, 'xerozinho@gmail.com')")

#banco.commit()

#cursor.execute("SELECT * FROM aluno")
# print(cursor.fetchall())

# cursor.execute("DELETE FROM aluno WHERE idade = 20")

# banco.commit()

    #  cursor.execute("SELECT * FROM aluno")
    #  print(cursor.fetchall())

    #  cursor.execute("DELETE")