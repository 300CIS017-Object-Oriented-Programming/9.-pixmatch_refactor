class Player:
    def __init__(self):
        self.__name = None
        self.__country = None
        self.__score = 0

    def get_player_info(self):
        if self.name is None:
            return None
        return f"Player: {self.__name}, Country: {self.__country}, Score: {self.__score}"

    def increase_score(self, difficulty):
        self.__score += difficulty.points_by_difficulty

    def decrease_score(self):
        self.__score -= 1

    def get_score(self):
        return self.__score

    def get_current_score(self):
        return self.__score

    def get_country(self):
        return self.__country

    def get_name(self):
        return self.__name
