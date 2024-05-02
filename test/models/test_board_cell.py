import unittest
from models.board_cell import BoardCell

class TestBoardCell(unittest.TestCase):

    def setUp(self):
        # Se crea una celda en la posición 0,0
        self.cell = BoardCell(1, 0, 0)

    def test_initialization(self):
        """Verifica que la inicialización de la celda se realiza correctamente"""
        self.assertEqual(self.cell.cell_idx, 1)
        self.assertEqual(self.cell.row, 0)
        self.assertEqual(self.cell.col, 0)
        self.assertIsNone(self.cell.verification_result)
        self.assertEqual(self.cell.emoji_img, '')

    def test_emoji_match_verification(self):
        """Verifica que la verificación de coincidencia de emojis se realiza correctamente"""
        self.cell.emoji_img = '🤔'
        self.cell.verify_emoji_match('🤔')
        self.assertTrue(self.cell.verification_result)

        self.cell.verify_emoji_match('😃')
        self.assertFalse(self.cell.verification_result)

    def test_emoji_match_verification_with_no_emoji(self):
        """Verifica que la verificación de coincidencia de emojis maneja correctamente el caso cuando no hay emoji"""
        self.cell.verify_emoji_match('😀')
        self.assertFalse(self.cell.verification_result)

    def test_emoji_match_verification_with_different_emoji(self):
        """Verifica que la verificación de coincidencia de emojis maneja correctamente el caso cuando el emoji es diferente"""
        self.cell.emoji_img = '😎'
        self.cell.verify_emoji_match('😃')
        self.assertFalse(self.cell.verification_result)

if __name__ == '__main__':
    # Cuando se llama sin parametros
    unittest.main()