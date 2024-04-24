import streamlit as st

from controllers.game_controller import GameController
from view.main_view import  draw_main_page


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

            # Tomar las variables que se necesitan del estado

        self.main() # LLamaal metodo que controla la vista principal

    def main(self):
        if self.run_page == 'main':
            draw_main_page(self.game_controller)
        else:
            st.write("Pendiente migracion")

    def read_picture_file(self):
        pass

    def verify_pressed_cell(self):
        pass
