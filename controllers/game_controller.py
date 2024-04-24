class GameController:
    def __init__(self):
        self.selected_difficulty = None
        self.current_player = None
        self.emojis_bank = []
        self.target_emoji = None
        self.game_status = None
        self.board = None

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
