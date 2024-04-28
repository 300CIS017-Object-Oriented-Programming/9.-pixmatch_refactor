class BoardCell:
    """
    Clase que representa una celda en el tablero del juego.
    Util para mantener la información de la celda y verificar si el emoji seleccionado
    por el jugador coincide con el emoji objetivo.
    """
    def __init__(self,cell_idx, row, col):
        self.cell_idx = cell_idx
        self.verification_result = None #No se ha seleccionado, ni se ha verificado ninguna vez
        self.row = row
        self.col = col
        self.emoji_img = ''

    def check_emoji_match(self, target_emoji):
        """ Cambia la lógica de la variable que indica que se ha verificado la coincidencia, el resultado puede ser True o False pero reemplaza el None del punto inicial de partida. """
        if self.emoji_img == target_emoji:
            self.verification_result = True
        else:
            self.verification_result = False


    def set_emoji_img(self, img):
        self.emoji_img = img
    def get_verification_result(self):
        return self.verification_result

    def get_id(self):
        return self.id

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col

    def get_emoji_img(self):
        return self.emoji_img
