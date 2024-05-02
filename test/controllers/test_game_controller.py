import unittest
from controllers.game_controller import GameController

class TestGameController(unittest.TestCase):

    def setUp(self):
        self.game_controller = GameController()

    def test_initialization(self):
        self.assertIsNone(self.game_controller.selected_difficulty)
        self.assertIsNone(self.game_controller.current_player)
        self.assertEqual(self.game_controller.emoji_bank, [])
        self.assertIsNone(self.game_controller.target_emoji)
        self.assertIsNone(self.game_controller.game_status)
        self.assertIsNone(self.game_controller.board)
        self.assertEqual(self.game_controller.leaderboard_ranking, {})

    def test_pick_emoji_bank(self):
        self.game_controller.selected_difficulty = {'name': 'Easy'}
        self.game_controller.pick_emoji_bank()
        self.assertIsNotNone(self.game_controller.emoji_bank)

    def test_choose_sidebar_emoji(self):
        self.game_controller.emoji_bank = ['😀', '😃', '😄', '😁', '😆']
        self.game_controller.choose_sidebar_emoji()
        self.assertIsNotNone(self.game_controller.target_emoji)

    def test_pre_new_game(self):
        self.game_controller.pre_new_game('Easy', 'John Doe, USA')
        self.assertIsNotNone(self.game_controller.selected_difficulty)
        self.assertIsNotNone(self.game_controller.current_player)
        self.assertIsNotNone(self.game_controller.board)
        self.assertEqual(self.game_controller.game_status, 'ACTIVE')

    def test_new_game(self):
        self.game_controller.pre_new_game('Easy', 'Camilo Quiroga, Colombia')
        self.game_controller.new_game()
        self.assertIsNotNone(self.game_controller.target_emoji)
        self.assertIsNotNone(self.game_controller.leaderboard_ranking)

    def test_play(self):
        self.game_controller.pre_new_game('Easy', '')
        self.game_controller.new_game()
        initial_score = self.game_controller.current_player.score

        # Se realiza una jugada en la celda 0
        self.game_controller.play(0)

        # Verifica que el puntaje del jugador haya cambiado en la jugada realizada
        self.assertNotEqual(self.game_controller.current_player.score, initial_score)

        if self.game_controller.board.get_cell_by_idx(0).emoji_img == self.game_controller.target_emoji:
            # Verifica que el puntaje del jugador tenga cinco puntos más que el puntaje inicial pues este es el valor para la dificultad 'Easy'
            self.assertEqual(self.game_controller.current_player.score, initial_score + 5)

            # Verifica que el tablero tenga una celda presionada con valor de True
            self.assertTrue(self.game_controller.board.cells_map[0].verification_result == True)
        else:
            # Verifica que el puntaje del jugador tenga un punto menos que el puntaje inicial pues debería haberse presionado una celda incorrecta
            self.assertEqual(self.game_controller.current_player.score, initial_score - 1)

            # Verifica que el tablero tenga una celda presionada con valor de False
            self.assertTrue(self.game_controller.board.cells_map[0].verification_result == False)

        # Verifica que el estado del juego sea 'ACTIVE'
        self.assertEqual(self.game_controller.game_status, 'ACTIVE')

        # Verifique que en las celdas pendientes no se encuentre la celda presionada
        self.assertNotIn(0, self.game_controller.board.get_unpressed_cells())

    def test_verify_game_status(self):
        self.game_controller.pre_new_game('Easy', 'Camilo Quiroga, Colombia')
        self.game_controller.new_game()
        # Verifica que el estado del juego sea 'ACTIVE'
        self.assertEqual(self.game_controller.verify_game_status(), 'ACTIVE')
