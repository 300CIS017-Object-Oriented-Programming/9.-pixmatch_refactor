class BoardCell:
    def __init__(self):
        self.__cell_idx = None
        self.__verification_result = None
        self.__row = 0
        self.col = 0
        self.emoji_img = ''
        self.emoji_index = None

    # Constructor que recibe todos los parametros de la clse
    def __int__(self, id, row, col, emoji_index):
        self.id = id
        self.__verification_result = False  # Inicialmente no se ha verificado si hay coincidencia
        self.__row = row
        self.col = col
        self.emoji_img = ''
        self.emoji_index = emoji_index

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
        return self.__verification_result

    def get_id(self):
        return self.id

    def get_row(self):
        return self.__row

    def get_col(self):
        return self.col

    def get_emoji_img(self):
        return self.emoji_img
