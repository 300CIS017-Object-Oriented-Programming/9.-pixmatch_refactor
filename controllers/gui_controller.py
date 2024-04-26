import streamlit as st

from controllers.game_controller import GameController
from view.main_view import draw_main_page, draw_main_board


class GUIController:
    def __init__(self):

        if 'my_state' not in st.session_state:

            self.game_controller = GameController()
            # Agregar las variables que necesitan

            self.run_page = 'main'  # Asigna el método main a la variable run_page para ejecutarse
            # Variable necesaria para mantener el estado
            st.session_state['my_state'] = self

        else:
            # Si ya existe en la sesión, entonces actualiza los valores
            self.game_controller = st.session_state.my_state.game_controller
            self.run_page = st.session_state.my_state.run_page
            st.write("Estoy construyendo otra vez la pagina")

    def main(self):
        if self.run_page == 'main':
            draw_main_page(self)
            # FIXME
            # Crear el leaderboard

        elif self.run_page == 'new_game':
            st.write("Dos")

            self.game_controller.new_game()
            draw_main_board(self)

    def pre_new_game_gui(self, selected_difficulty, player_name_country):
        # Inicializa el tablero
        self.game_controller.pre_new_game(selected_difficulty, player_name_country)
        # Actualiza la página a la vista del tablero de juego
        st.session_state.my_state.run_page = 'new_game'
        st.rerun()

    def verify_pressed_cell(self):
        pass
