import streamlit as st
from streamlit_autorefresh import st_autorefresh

from controllers.game_controller import GameController
from settings import PRESSED_EMOJI_HTML_TEMPLATE
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

    def main(self):
        if self.run_page == 'main':
            draw_main_page(self)
            # FIXME
            # Crear el leaderboard

        elif self.run_page == 'new_game':
            self.game_controller.new_game()
            draw_main_board(self)

    def pre_new_game_gui(self, selected_difficulty, player_name_country):
        # Inicializa el tablero
        self.game_controller.pre_new_game(selected_difficulty, player_name_country)
        # Actualiza la página a la vista del tablero de juego
        st.session_state.my_state.run_page = 'new_game'
        st.rerun()

    def new_game_gui(self):
        # Configura y muestra los botones del tablero del juego de forma programatica
        for i in range(0, self.game_controller.board.board_size):
            # Configura las columnas para los botones del tablero.
            # Cada fila del tablero de juego está compuesta por un número de columnas igual al total de celdas por fila.
            # La variable 'tlst' define el espacio de PressedCheckcada columna, y luego se crea un objeto de columna para cada posición.

            tlst = ([1] * self.game_controller.board.board_size) + [2]  # 2 = espacio al lado derecho
            globals()['cols' + str(i)] = st.columns(tlst)

        cell_cont = 0
        for row in range(self.game_controller.board.board_size):
            row_str = str(row)
            for col in range(self.game_controller.board.board_size):
                cell_to_draw = self.game_controller.board.cells_map[cell_cont]
                globals()['cols' + row_str][col] = globals()['cols' + row_str][col].empty()
                if cell_to_draw.verification_result is None:
                    vemoji = cell_to_draw.emoji_img
                    globals()['cols' + row_str][col].button(vemoji, on_click=self.game_controller.play, args =(cell_cont,),
                                                            key=f"B{cell_cont}")
                elif cell_to_draw.verification_result == True:
                    globals()['cols' + row_str][col].markdown(
                        PRESSED_EMOJI_HTML_TEMPLATE.replace('|fill_variable|', '✅️'), unsafe_allow_html=True)

                elif cell_to_draw.verification_result == False:
                    globals()['cols' + row_str][col].markdown(
                        PRESSED_EMOJI_HTML_TEMPLATE.replace('|fill_variable|', '❌'), unsafe_allow_html=True)
                cell_cont += 1

        # Lógica para autorefrescar la página y cambiar el score si pasado un tiempo no se ha seleccionado nada
        # self.autorefresh_page()


    def autorefresh_page(self):
        """
        Lógica para autorefrescar la página y cambiar el score si pasado un tiempo no se ha seleccionado nada.
        """
        # Temporizador de autorefrescamiento que resta puntos si el tiempo se agota pendiente por agregar
        aftimer = st_autorefresh(interval=(self.get_refresh_interval()), key="aftmr")

        if aftimer > 0:
        # Se agotó el tiempo para seleccionar un emoji, entonces reduce el puntaje del jugador
            self.game_controller.current_player.decrease_score()

    def get_emoji_for_score(self):
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
        return f"{self.get_emoji_for_score()} Score: {self.game_controller.current_player.score} | Pending: {self.game_controller.board.count_pending_cells()}"

    def get_refresh_interval(self):
        """
        Obtiene el intervalo de tiempo en milisegundos para el autorefrescamiento de la página.
        """
        return self.game_controller.selected_difficulty['sec_interval_for_autogen'] * 1000

    def back_to_main(self):
        """
        Regresa a la página principal del juego.
        """
        st.session_state.my_state.run_page = 'main'
        st.rerun()