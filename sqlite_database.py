from flask import Flask, sqlite3

conn = sqlite3.connect('games.db')

c = conn.cursor()

c.execute("""CREATE TABLE games (
			id int,
			game_title text
			)""")
			
conn.commit()

conn.close()
