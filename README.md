# Ejercicio de migración parte 2

## Migración a objetos

### Objetivo

Incorporar el paradigma de programación orientada a objetos (OOP) y transformar la aplicación en una aplicación en
Streamlit
para favorcer la mantenibilidad del código fuente.

## Código original

* Ver el código fuente del proyecto https://github.com/shakamoushie/pixmatch/blob/main/pixmatch.py . Este proyecto tiene
  un clone del proyecto original
* Interactuar con el juego para entener las funcionalidades principales https://pixmatchgame.streamlit.app
* Instalar el proyecto en su computador local. Escriba desde la línea de comandos y ubicado en la carpeta raíz del
  proyecto `pip install -r requirements.txt`. Note que si no tiene un ambiente virtual primero debe configurarlo.
* Ejecutar el juego localmente. Escriba en consola `streamlit run docs/legacy_version/pixmatch.py`. Su navegador debería
  abrir el juego
  ![img.png](docs/img/ejecucion.png)

## Código orientado a objetos

* Este código fuente cumple las mismas funcionalidades que el código legacy pero tiene orientación a objetos
* **Análisis del código actual**
    * Compare la lógica del método ```PreNewGame``` en el código original y en el nuevo código orientado a objetos.
      Identifique como esta separada la lógica relacionada con la visualización con la lógica de negocio
    * Identifique en la versión orientada a objetos en qué puntos se controla la lectura y escritura del leaderboard.
      Considere que una restricción es que solo se escribe y se lee el leaderboard si el jugador escribe su nombre

### Por hacer

1. Agregar caso de prueba que verifique el correcto funcionamiento de la asignación del emoji de la barra lateral en el tablero
2. Agregar caso de prueba para verificar que cuando se pierde el status del juego cambia a 'LOST'.
3. Agregar casos de prueba para clase Player
4. Agregar casos de prueba a cualquiera de las clases ya existentes para los que falten casos de prueba
## Diagrama del proyecto

```mermaid
classDiagram
    class GameController {
        -selected_difficulty
        -current_player
        -emoji_bank
        -target_emoji
        -game_status
        -board
        -leaderboard_ranking
        +pick_emoji_bank()
        +choose_sidebar_emoji()
        +reset_board()
        +pre_new_game(selected_difficulty, player_name_country)
        +new_game()
        +verify_game_status()
        +play(cell_idx)
    }
    class GUIController {
        -game_controller
        -run_page
        -st_matrix
        +main()
        +pre_new_game_gui(selected_difficulty, player_name_country)
        +new_game_gui()
        +get_emoji_for_score()
        +get_score_and_pending_cells_values()
        +get_refresh_interval()
        +back_to_main()
    }
    class Board {
        -cells_map
        -expired_cells_list
        -board_size
        -total_cells 
        +prepare_board()
        +get_unpressed_cells()
        +count_pending_cells()
        +get_cell_by_idx()
        +add_expired_cell(cell_idx)
    }
    class BoardCell {
        -cell_idx
        -verification_result
        -row = 0
        -col = 0
        -emoji_img: string
        +BoardCell(cell_idx,row,col)
        +verify_emoji_match(target_emoji)
    }
    class LeaderBoardManager {
        -leaderboard_file_name_path
    
        +create_leader_board()
        +read_leader_board()
        +sort_leader_board_data()
        +update_leader_board(player, MAX_PLAYERS)
    }
    class Player {
        -player_name_country
        -score
        
        +Player(player_name_country)
        +get_player_info(
        +increase_score(difficulty_points)
        +decrease_score()
    }
    class MainView {
        +draw_instructions()
        +draw_main_page(gui_controller)
        +draw_new_game_board(gui_controller)
        +draw_end_game_info(gui_controller)
        +draw_lateral_bar_new_game(gui_controller)
        +reduce_gap_from_page_top(section_to_adjust)
    }
    class App {
        +main()
    }
    GUIController --> GameController : has
    Board <-- GameController : has
    Board o-- BoardCell : has
    GameController --> Player : has
    GameController ..> LeaderBoardManager : uses
    LeaderBoardManager ..> Player : uses
    MainView ..> GameController : uses
    GUIController <..> MainView : uses
    App ..> GUIController : launches
```

Editor:https://diagrams.helpful.dev/s/s:MAdFfNUs

### Diagrama de secuencia que representa la interacción cuando se da click en new game
```mermaid
sequenceDiagram
    participant GUIController as GUIController
    participant GameController as GameController
    participant Board as Board
    participant main_view as main_view

    GUIController->>GameController: pre_new_game(selected_difficulty, player_name_country)
    GameController->>GameController: selected_difficulty = DIFFICULTY_LEVELS_OPTIONS[selected_difficulty]
    GameController->>GameController: current_player = Player(player_name_country)
    GameController->>Board: board = Board(selected_difficulty['board_size'])
    GameController->>GameController: pick_emoji_bank()
    GameController->>Board: prepare_board()
    GameController->>GameController: game_status = 'ACTIVE'
    GameController->>GameController: create_leader_board()
    GUIController->>GUIController: run_page = 'new_game'
    GUIController->>GUIController: rerun()
    GUIController->>GameController: new_game()
    GameController->>GameController: reset_board()
    GameController->>GameController: read_leader_board()
    GameController->>GameController: verify_game_status()
    GUIController->>main_view: draw_new_game_board(self)
```