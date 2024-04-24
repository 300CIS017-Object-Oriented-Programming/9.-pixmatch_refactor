from models.player import Player


class GameController:
    def __init__(self):
        self.selected_difficulty = None
        self.current_player = None
        self.emojis_bank = []
        self.target_emoji = None
        self.game_status = None
        self.board = None

    def define_player(self, player_name_country):
        self.current_player = Player(player_name_country) # Define la info del jugador que interactua con el juego

    def pick_emoji_bank(self, difficulty):
        pass

    def find_target_emoji(self, current_img, selected_difficulty, img_bank):
        pass

    def reset_board(self):
        pass

    def verify_game_status(self):
        pass

    def play(self, cell_idx):
        pass
