class Board:
    """
    Clase que representa el tablero de juego con celdas y emojis. Util para mantener la información del tablero
    """
    def __init__(self, board_size):
        self.cells_map = {}
        self.expired_cells_list = []
        self.board_size = board_size
        self.total_cells = board_size**2 # El tamaño del tablero es el cuadrado del tamaño de la cuadrícula

    def prepare_board(self, difficulty):
        pass

    def get_unpressed_cells(self):
        """
        Retorna una lista de celdas no presionadas que es la diferencia entre las celdas expiradas y las celdas totales del tablero
        """
        all_cells = self.cells_map.keys()
        unpressed_cells = list(set(all_cells) - set(self.expired_cells_list))
        return unpressed_cells

    def count_pending_cells(self):
        """
        Retorna la cantidad de celdas pendientes que no han sido presionadas
        """
        pending_cells = self.total_cells - len(self.expired_cells_list)
        return pending_cells

    def get_cell_by_idx(self, idx):
        return self.cells_map.get(idx)

    def add_expired_cell(self, idx):
        pass
