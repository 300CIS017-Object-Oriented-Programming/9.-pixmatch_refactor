import random

import streamlit as st
from PIL import Image

from controllers.game_controller import GameController
from models.player import Player
from settings import IMAGES_PATH, HORIZONTAL_BAR_HTML_TEMPLATE, PURPLE_BUTTON_HTML_TEMPLATE, DIFFICULTY_LEVELS_OPTIONS
from view.main_view import draw_instructions, draw_main_page, draw_main_board


class GUIController:
    def __init__(self):

        if 'my_state' not in st.session_state:

            self.game_controller = GameController()
            # Agregar las variables que necesitan

            self.run_page = 'main'  # Asigna el método main a la variable run_page para ejecutarse
            # Variable necesaria para mantener el estado
            st.session_state['my_state'] = self

        else:
            self.game_controller = st.session_state.my_state.game_controller
            self.run_page = st.session_state.my_state.run_page
            st.write("Estoy construyendo otra vez la pagina")

            # Tomar las variables que se necesitan del estado

        self.main() # LLamaal metodo que controla la vista principal

    def main(self):
        if self.run_page == 'main':
            draw_main_page(self)
            # FIXME
            # Crea el leaderboard

        elif self.run_page == 'new_game':
            self.game_controller.new_game()
            draw_main_board()


    def pre_new_game(self, selected_difficulty, player_name_country):
        self.game_controller.selected_difficulty = DIFFICULTY_LEVELS_OPTIONS[selected_difficulty]
        self.game_controller.current_player = Player(player_name_country)
        # Inicializa el tablero
        self.game_controller.pre_new_game()
        # Actualiza la página a la vista del tablero de juego
        self.run_page = 'new_game'


    def verify_pressed_cell(self):
        pass



