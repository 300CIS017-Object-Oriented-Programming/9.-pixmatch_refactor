import unittest
from models.board import Board
from models.board_cell import BoardCell

class TestsBoard(unittest.TestCase):

    def setUp(self):
        # Se crea un tablero de 3x3
        self.board = Board(3)

    def test_initialization_estimate_board_size(self):
        # Verifica que el tablero se inicializa con la cantidad correcta de celdas
        self.assertEqual(9, self.board.total_cells)

    def test_prepare_board_creates_correct_cells(self):

       # Se prepara el tablero lo que crea las celdas
        self.board.prepare_board()
        # Verifica que el tablero tenga las celdas creadas en la cantidad esperada
        self.assertEqual(9, len(self.board.cells_map))
        for i in range(9):
            # Verifica que LOS objetos creados sean de tipo BoardCell
            self.assertIsInstance(self.board.cells_map[i], BoardCell)
            # Verifica que las celdas tengan el índice correcto
            self.assertEqual(self.board.cells_map[i].cell_idx, i)

    def test_get_unpressed_cells_returns_correct_cells(self):
        """
        Verifica que las celdas no presionadas se retornan correctamente
        Returns:

        """
        self.board.prepare_board()
        self.board.add_expired_cell(0)

        # Revisa que retorna otras celdas que no sean la 0
        self.assertNotIn(0, self.board.get_unpressed_cells())

    def test_count_pending_cells_returns_correct_count(self):
        self.board.prepare_board()
        self.board.add_expired_cell(0)
        # Se esperan 8 celdas porque la celda 0 ya fue presionada y el tablero se creo con 9 celdas
        self.assertEqual(self.board.count_pending_cells(), 8)

    def test_get_cell_by_idx_returns_correct_cell(self):
        self.board.prepare_board()
        cell = self.board.get_cell_by_idx(0)
        # Verifica que la celda retornada sea la celda 0
        self.assertEqual(cell.cell_idx, 0)

    def test_add_expired_cell_adds_cell_to_expired_list(self):
        self.board.prepare_board()
        self.board.add_expired_cell(0)
        # Verifica que la celda 0 se agrega a la lista de celdas expiradas
        self.assertIn(0, self.board.expired_cells_idx_list)
