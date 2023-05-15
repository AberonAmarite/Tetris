import sqlite3
from datetime import datetime


class GameDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('src/scores.db')
        self.c = self.conn.cursor()

        # Create a table for scores if it doesn't exist
        self.c.execute('''CREATE TABLE IF NOT EXISTS scores
                     (username TEXT, score INTEGER, timestamp TEXT)''')

    def insert_score(self, username, score):
        timestamp = str(datetime.now())
        self.c.execute("INSERT INTO scores VALUES (?, ?, ?)", (username, score, timestamp))
        self.conn.commit()

    # Get the top 3 scores
    def get_top_scores(self):
        self.c.execute("SELECT username, score FROM scores ORDER BY score DESC LIMIT 10")
        top_scores = self.c.fetchall()
        scores_list = []
        for i, score in enumerate(top_scores):
            scores_list.append(f"{i + 1}. {score[0]}: {score[1]}")
        return scores_list

    # Get the highest score for a specific user
    def get_highest_score(self, username):
        if username:
            self.c.execute("SELECT MAX(score) FROM scores WHERE username=?", (username,))
            highest_score = self.c.fetchone()[0]
            if highest_score is not None:
                return f"{username}'s highest score: {highest_score}"
            else:
                return f"{username} doesn't have any scores yet"

    # Get the most recent score for a specific user
    def get_most_recent_score(self, username):
        if username:
            self.c.execute("SELECT score, timestamp FROM scores WHERE username=? ORDER BY timestamp DESC LIMIT 1",
                           (username,))
            recent_score = self.c.fetchone()
            if recent_score is not None:
                time = datetime.strptime(recent_score[1], '%Y-%m-%d %H:%M:%S.%f')
                formatted_score = time.strftime('%d.%m.%Y %H:%M:%S')
                return f"{username}'s most recent score: {recent_score[0]} at {formatted_score}"
            else:
                return f"{username} doesn't have any scores yet"
