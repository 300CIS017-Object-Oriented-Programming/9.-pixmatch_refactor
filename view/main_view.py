import random

import streamlit as st
from PIL import Image

from settings import HORIZONTAL_BAR_HTML_TEMPLATE, IMAGES_PATH, PURPLE_BUTTON_HTML_TEMPLATE, DIFFICULTY_LEVELS_OPTIONS


def draw_instructions():
    """Configura y muestra la página inicial del juego, incluyendo la barra lateral y las reglas del juego."""
    with st.sidebar:
        st.subheader("🖼️ Pix Match:")
        st.markdown(HORIZONTAL_BAR_HTML_TEMPLATE, True)

        # Cargar y mostrar el logo del juego en la barra lateral
        sidebar_logo = Image.open(IMAGES_PATH + 'sidebarlogo.jpg').resize((300, 390))
        st.image(sidebar_logo, use_column_width='auto')

    # Detalles y ayuda del juego
    instruccions_html_text = f"""<span style="font-size: 26px;">
           <ol>
           <li style="font-size:15px";>Game play opens with (a) a sidebar picture and (b) a N x N grid of picture buttons, where N=6:Easy, N=7:Medium, N=8:Hard.</li>
           <li style="font-size:15px";>You need to match the sidebar picture with a grid picture button, by pressing the (matching) button (as quickly as possible).</li>
           <li style="font-size:15px";>Each correct picture match will earn you <strong>+N</strong> points (where N=5:Easy, N=3:Medium, N=1:Hard); each incorrect picture match will earn you <strong>-1</strong> point.</li>
           <li style="font-size:15px";>The sidebar picture and the grid pictures will dynamically regenerate after a fixed seconds interval (Easy=8, Medium=6, Hard=5). Each regeneration will have a penalty of <strong>-1</strong> point</li>
           <li style="font-size:15px";>Each of the grid buttons can only be pressed once during the entire game.</li>
           <li style="font-size:15px";>The game completes when all the grid buttons are pressed.</li>
           <li style="font-size:15px";>At the end of the game, if you have a positive score, you will have <strong>won</strong>; otherwise, you will have <strong>lost</strong>.</li>
           </ol></span>"""

    # Configuración de columnas para mostrar las reglas del juego y una imagen de ayuda
    sc1, sc2 = st.columns(2)
    random.seed()
    game_help_image_path = IMAGES_PATH + random.choice(
        ["MainImg1.jpg", "MainImg2.jpg", "MainImg3.jpg", "MainImg4.jpg"])
    game_help_image = Image.open(game_help_image_path).resize((550, 550))
    sc2.image(game_help_image, use_column_width='auto')

    sc1.subheader('Rules | Playing Instructions:')
    sc1.markdown(HORIZONTAL_BAR_HTML_TEMPLATE, True)
    sc1.markdown(instruccions_html_text, unsafe_allow_html=True)
    st.markdown(HORIZONTAL_BAR_HTML_TEMPLATE, True)

    # Detalles del autor
    author_details = "<strong>Happy  play: 😎 Shawn Pereira: shawnpereira1969@gmail.com</strong>"
    st.markdown(author_details, unsafe_allow_html=True)
    st.info("Modified by: Luisa Rincon")

def draw_main_page(game_controller):

    # Ajustar el estilo de la barra lateral y los botones
    st.markdown('<style>[data-testid="stSidebar"] > div:first-child {width: 310px;}</style>',
                unsafe_allow_html=True, )  # reduce sidebar width
    st.markdown(PURPLE_BUTTON_HTML_TEMPLATE, unsafe_allow_html=True)

    # Mostrar la página inicial con reglas e instrucciones
    draw_instructions()

    # Configuración de la barra lateral para entradas de usuario y opciones
    with st.sidebar:
        difficulty_levels_values = DIFFICULTY_LEVELS_OPTIONS.keys()
        # Selección de nivel de dificultad
        selected_difficulty_key = st.radio('Difficulty Level:', options=difficulty_levels_values, index=1,
                                           horizontal=True)
        # Busca en el diccionario de dificultaes la llave de la dificultad seleccionada y la asigna al controlador
        game_controller.selected_difficulty = DIFFICULTY_LEVELS_OPTIONS[selected_difficulty_key]

        # Entrada para el nombre del jugador y el país
        player_info = st.text_input("Player Name, Country", placeholder='Shawn Pereira, India',
                                    help='Optional input only for Leaderboard')
        # Asigna la información del jugador a
        game_controller.define_player(player_info)

        # Botón para iniciar un nuevo juego
        if st.button(f"🕹️ New Game", use_container_width=True):
            st.write("voy a iniciar el juego")
            # Crear el leaderboard si no existe, preparar el juego y cambiar a la pantalla de juego
            # Leaderboard('create')

            # PreNewGame()
            # mystate.runpage = play
            # st.rerun()

        st.markdown(HORIZONTAL_BAR_HTML_TEMPLATE, True)  # Barra decorativa horizontal


def reduce_gap_from_page_top(self, section_to_adjust):
    pass


def draw_leaderboard_ranking(self):
    pass


def draw_target_emoji(self):
    pass


def draw_main_board(self):
    pass


def draw_playing_gui(self):
    pass

