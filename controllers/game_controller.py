import random

from models.board import Board
from models.board_cell import BoardCell
from models.player import Player
from settings import EMOJIS_CATEGORIES_EASY, EMOJIS_CATEGORIES_MEDIUM, EMOJIS_CATEGORIES_HARD


class GameController:
    def __init__(self):
        self.selected_difficulty = None
        self.current_player = None
        self.emoji_bank = []
        self.target_emoji = None
        self.game_status = None
        self.board = None

    def pick_emoji_bank(self):
        random.seed()
        # Selección de categoría de emojis según la dificultad del juego

        # Version mejorada de la selección de categoría de emojis según la dificultad del juego
        difficulty_emoji_map = {
            'Easy': EMOJIS_CATEGORIES_EASY,
            'Medium': EMOJIS_CATEGORIES_MEDIUM,
            'Hard': EMOJIS_CATEGORIES_HARD
        }

        difficulty_name = self.selected_difficulty['name']
        if difficulty_name in difficulty_emoji_map:
            # Define el banco de emojis
            self.emoji_bank = random.choice(difficulty_emoji_map[difficulty_name])


    def choose_sidebar_emoji(self):
        # Seleccionar un emoji para la barra lateral de forma aleatoria
        sidebar_emoji_index = random.randint(0, len(self.emoji_bank) - 1)
        self.target_emoji = self.emoji_bank[sidebar_emoji_index]

    def reset_board(self):
        """
            Reinicia el tablero del juego, configurando emojis aleatorios en cada celda de la cuadrícula,
            y asegurándose de que el emoji de la barra lateral esté presente al menos una vez en el tablero.
            """

        # Define el emoji que se buscará
        self.choose_sidebar_emoji()
        sidebar_emoji_in_list = False  # Controla si el emoji de la barra lateral está en el tablero

        """ FIXME. Separar esta lógica para que la clase board haga algunas partes. PUede hacer ajustes sobre las clases propuestas
        # Configurar emojis para cada celda del tablero
        for vcell in range(1, self.board.board_size + 1):
            if not mystate.plyrbtns[vcell]['isPressed']:  # Solo cambia los emojis de celdas no presionadas
                emoji_index = random.randint(0, len(mystate.emoji_bank) - 1)
                vemoji = mystate.emoji_bank[emoji_index]
                mystate.plyrbtns[vcell]['eMoji'] = vemoji

                if vemoji == mystate.sidebar_emoji:
                    sidebar_emoji_in_list = True

        # Asegurar que el emoji de la barra lateral está al menos una vez en el tablero
        if not sidebar_emoji_in_list:
            unpressed_cells = [cell for cell in range(1, (total_cells_per_row_or_col ** 2) + 1)
                               if not mystate.plyrbtns[cell]['isPressed']]
            if unpressed_cells:
                selected_cell = random.choice(unpressed_cells)
                mystate.plyrbtns[selected_cell]['eMoji'] = mystate.sidebar_emoji
        """

    def pre_new_game(self):
        """
               Prepara el juego para una nueva sesión, inicializando las celdas y los puntajes.

               Esta función se encarga de reiniciar todos los estados relevantes para comenzar un nuevo juego.
               Reinicia las celdas del juego y selecciona de manera aleatoria los emojis
               que aparecerán en el tablero según la dificultad del juego. Asegura que todos los botones de
               la cuadrícula estén configurados para el inicio de una nueva partida.
               """

        # Inicializa el tablero
        self.board = Board(self.selected_difficulty['board_size'])

        # Selecciona el banco de emojis
        self.pick_emoji_bank()

        # Reinicia la información de los botones del juego
        # FIXME pasar esto para la clase Board, por principio de responsabilidad, esta logica es mas del Board que del controller
        cont_row = 1
        cont_col = 1
        for vcell in range(1,self.board.board_size + 1):
            # Crea un objeto de celda y lo agrega al mapa de celdas del tablero
            self.board.cells_map[vcell] = BoardCell(cell_idx=vcell, row=cont_row, col=cont_col)
            cont_col += 1
            if cont_col > self.selected_difficulty['board_size']:
                cont_col = 1 # Reinicia el contador de columnnas cada vez que termina una fila
                cont_row += 1 # Incrementa el contador de filas para indicar que va en la fila siguiente

        self.game_status = 'ACTIVE'

    def new_game(self):

        # Tome la logica de newgame de la versión legacy y adaptela para que se ajuste a la estructura de clases definida en este proyecto
        self.reset_board()

        # Faltan el resto de elementos
        pass

    def verify_game_status(self):
        pass

    def play(self, cell_idx):
        pass
