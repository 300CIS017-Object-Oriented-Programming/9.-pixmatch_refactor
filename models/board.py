class Board:
    def __init__(self, board_size):
        self.cells_map = {}
        self.expired_cells_list = []
        self.board_size = board_size**2 # El tamaño del tablero es el cuadrado del tamaño de la cuadrícula

    def prepare_board(self, difficulty):
        pass

    def get_unpressed_cells(self):
        #TODO Implementar aqui la lógica para devolver solo las celdas que  no se han presionado

        pass

    def add_expired_cell(self, cell_id):
        pass

    def get_cell_by_idx(self, cell_id):
        return self.cells_map[cell_id]
