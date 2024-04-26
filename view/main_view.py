import random

import streamlit as st
from PIL import Image

from settings import HORIZONTAL_BAR_HTML_TEMPLATE, IMAGES_PATH,DIFFICULTY_LEVELS_OPTIONS, PURPLE_BUTTON_HTML_TEMPLATE, \
    IMAGES_PATH


def draw_instructions(st):
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

def draw_main_page(gui_controller):

        # Ajustar el estilo de la barra lateral y los botones
        st.markdown('<style>[data-testid="stSidebar"] > div:first-child {width: 310px;}</style>',
                    unsafe_allow_html=True, )  # reduce sidebar width
        st.markdown(PURPLE_BUTTON_HTML_TEMPLATE, unsafe_allow_html=True)

        with st.sidebar:
            st.subheader("🖼️ Pix Match:")
            st.markdown(HORIZONTAL_BAR_HTML_TEMPLATE, True)

            # Cargar y mostrar el logo del juego en la barra lateral
            sidebar_logo = Image.open(IMAGES_PATH + 'sidebarlogo.jpg').resize((300, 390))
            st.image(sidebar_logo, use_column_width='auto')

        # Mostrar la página inicial con reglas e instrucciones
        draw_instructions(st)

        # Configuración de la barra lateral para entradas de usuario y opciones
        with st.sidebar:
            # Selección de nivel de dificultad
            selected_difficulty = st.radio('Difficulty Level:', options=('Easy', 'Medium', 'Hard'), index=1,
                                           horizontal=True, )

            st.write(f'La dificultad seleccionada fue {selected_difficulty}')
            # Entrada para el nombre del jugador y el país
            player_name_country = st.text_input("Player Name, Country", placeholder='Shawn Pereira, India',
                                                help='Optional input only for Leaderboard')
            # Botón para iniciar un nuevo juego
            if st.button(f"🕹️ New Game", use_container_width=True):
                gui_controller.pre_new_game_gui(selected_difficulty, player_name_country)

            st.markdown(HORIZONTAL_BAR_HTML_TEMPLATE, True)  # Barra decorativa horizontal


def draw_main_board(gui_controller):

        reduce_gap_from_page_top('sidebar')

        st.subheader("Picture Positions:")
        st.markdown(HORIZONTAL_BAR_HTML_TEMPLATE, True)

        # Set Board Dafaults
        st.markdown("<style> div[class^='css-1vbkxwb'] > p { font-size: 1.5rem; } </style> ",
                    unsafe_allow_html=True)  # make button face big

        # Configura y muestra los botones del tablero del juego de forma programatrica
        for i in range(1, gui_controller.game_controller.board.board_size + 1):
            # Configura las columnas para los botones del tablero.
            # Cada fila del tablero de juego está compuesta por un número de columnas igual al total de celdas por fila.
            # La variable 'tlst' define el espacio de cada columna, y luego se crea un objeto de columna para cada posición.

            tlst = ([1] * gui_controller.game_controller.board.board_size) + [2]  # 2 = espacio al lado derecho
            globals()['cols' + str(i)] = st.columns(tlst)

        # FIXME terminar de pintar el tablero principal y todas sus interacciones
        st.write("Soy tablero principal")
        if st.button("Cambiar a uno"):
            st.session_state.my_state.run_page = 'main'
            st.rerun()

def draw_leaderboard_ranking(st, leaderboar):
    pass

def draw_target_emoji(st, emoji):
    pass

def read_picture_file(self):
    pass

def reduce_gap_from_page_top(section_to_adjust):
    if section_to_adjust == 'main page':
        st.markdown(" <style> div[class^='block-container'] { padding-top: 2rem; } </style> ",
                    True)  # Ajusta el espacio en la página principal
    elif section_to_adjust == 'sidebar':
        st.markdown(" <style> div[class^='st-emotion-cache-10oheav'] { padding-top: 0rem; } </style> ",
                    True)  # Ajusta el espacio en la barra lateral
    elif section_to_adjust == 'all':
        # Ajusta el espacio tanto en la página principal como en la barra lateral
        st.markdown(" <style> div[class^='block-container'] { padding-top: 2rem; } </style> ", True)
        st.markdown(" <style> div[class^='st-emotion-cache-10oheav'] { padding-top: 0rem; } </style> ", True)


