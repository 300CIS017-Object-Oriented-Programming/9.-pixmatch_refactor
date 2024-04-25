class BoardCell:
    def __init__(self,cell_idx, row, col):
        self.cell_idx = cell_idx
        self.verification_result = None #No se ha seleccionado, ni se ha verificado ninguna vez
        self.row = row
        self.col = col
        self.emoji_img = ''
        self.emoji_index = 0

    def check_emoji_match(self, target_emoji):
        """ Cambia la lógica de la variable que indica que se ha verificado la coincidencia, el resultado puede ser True o False pero reemplaza el None del punto inicial de partida. """
        if self.emoji_img == target_emoji:
            self.__verification_result = True
        else:
            self.__verification_result = False


    def set_emoji_img(self, img):
        self.emoji_img = img

    def get_emj_index(self):
        return self.emoji_index

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
