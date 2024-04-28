class Player:
    """
    Clase para mantener la información del jugador y su puntaje.
    """
    def __init__(self, player_name_country):
        self.player_name_country = player_name_country
        self.score = 0

    def get_player_info(self):
        if self.name is None:
            return None
        return f"Player: {self.player_name_country}, Score: {self.score}"

    def increase_score(self, difficulty_points):
        self.score += difficulty_points

    def decrease_score(self):
        self.score -= 1
