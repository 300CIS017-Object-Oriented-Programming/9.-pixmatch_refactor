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

    def return_to_main(self):
        """
        Regresa a la página principal del juego.
        """
        st.session_state.my_state.run_page = 'main'
        st.rerun()

    def score_emoji(self):
        """
           Determina el emoji a mostrar basado en la puntuación actual del jugador almacenada en `my_state.myscore`.

           Esta función evalúa el rango en el que se encuentra la puntuación del jugador y retorna un emoji correspondiente
           que refleja una retroalimentación visual instantánea al jugador sobre su desempeño.

           Returns:
               str: Un string de emoji que representa el estado emocional del jugador.

           Ejemplos:
               - Una puntuación de 0 retorna '😐', indicando una expresión neutral.
               - Puntuaciones negativas retornan emojis tristes, incrementando en tristeza a medida que la puntuación disminuye.
               - Puntuaciones positivas retornan emojis sonrientes, incrementando en alegría a medida que la puntuación aumenta.
        """

        if self.game_controller.current_player.score == 0:
            return '😐'
        elif -5 <= self.game_controller.current_player.score <= -1:
            return '😏'
        elif -10 <= self.game_controller.current_player.score <= -6:
            return '☹️'
        elif self.game_controller.current_player.score <= -11:
            return '😖'
        elif 1 <= self.game_controller.current_player.score <= 5:
            return '🙂'
        elif 6 <= self.game_controller.current_player.score <= 10:
            return '😊'
        elif self.game_controller.current_player.score > 10:
            return '😁'

    def get_score_and_pending_cells_values(self):
        return f"{self.score_emoji()} Score: {self.game_controller.current_player.score} | Pending: {self.game_controller.board.count_pending_cells()}"

    def get_refresh_interval(self):
        """
        Obtiene el intervalo de tiempo en milisegundos para el autorefrescamiento de la página.
        """
        return self.game_controller.selected_difficulty['sec_interval_for_autogen'] * 1000
    def verify_pressed_cell(self):
        pass
