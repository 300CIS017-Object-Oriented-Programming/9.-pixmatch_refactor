import streamlit as st

from controllers.game_controller import GameController
from view.main_view import  draw_main_page


class GUIController:
    def __init__(self):

        if 'my_state' not in st.session_state:
            self.run_page = self.main()  # Asigna el método main a la variable run_page para ejecutarse
            self.game_controller = GameController()

            # Agregar las variables que necesitan

            # Variable necesasaria para mantener el estado
            st.session_state['my_state'] = self

        else:
            self.game_controller = st.session_state.my_state.game_controller
            self.run_page = st.session_state.my_state.run_page

            # Tomar las variables que se necesitan del estado

    def main(self):
        draw_main_page()

    def read_picture_file(self):
        pass

    def verify_pressed_cell(self):
        pass
