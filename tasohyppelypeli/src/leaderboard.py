from database.database import Database

class LeaderBoard():

    def __init__(self):
        self.database = Database()
        self.head_1 = "PLAYER"
        self.head_2 = "SCORE"
        self.column_font = "arial"
        self.column_font_size = 16
        self.header_font = "arial black"
        self.header_font_size = 20

    def get_leaderboard(self):
        leaders = self.database.get_top_10()
        return leaders

    def add_score(self):
        "INSERT into leaderboard (player, score, time) VALUES ('Nicolas', 345, current_timestamp);"
    
    def get_font_styles(self):
        return [self.column_font, self.column_font_size, self.header_font, self.header_font_size]
    
    def get_headers(self):
        return [self.head_1, self.head_2]
