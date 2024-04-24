import json
import os

from settings import MAX_LEADERBOARD_PLAYERS, LEADERBOARD_FILE_NAME


class LeaderBoard:
    def __init__(self):
        self.leaderboard_file_name_path = MAX_LEADERBOARD_PLAYERS + LEADERBOARD_FILE_NAME

    def create_leader_board(self, player):
        # El jugador tiene que tener un nombre para ser agregado al leaderboard
        if not player.get_name() is None:
            if os.path.isfile(self.leaderboard_file_name_path) == False:
                tmpdict = {}
                # Crea el archivo de leaderboard vacío
                json.dump(tmpdict, open(self.leaderboard_file_name_path, 'w'))  # write file

    def read_leader_board(self, player):
        # Escribe en el leaderboard si el jugador ha proporcionado su nombre y el archivo existe
        if not player.get_name() is None:
            if os.path.isfile(self.leaderboard_file_name_path):
                leaderboard = json.load(open(self.leaderboard_file_name_path))
                leaderboard = dict(
                    sorted(leaderboard.items(), key=lambda item: item[1]['HighestScore'], reverse=True))  # sort desc
                return leaderboard  # Se retorna el diccionario con el leaderboard

                """ Todo esto ya no va pq corresponde a la lógica de presentación
                sc0, sc1, sc2, sc3 = st.columns((2, 3, 3, 3))
                rknt = 0
                for key in leaderboard:
                    rknt += 1
                    if rknt == 1:
                        sc0.write('🏆 Ganadores anteriores:')
                        sc1.write(f"🥇 | {leaderboard[key]['NameCountry']}: {leaderboard[key]['HighestScore']}")
                    elif rknt == 2:
                        sc2.write(f"🥈 | {leaderboard[key]['NameCountry']}: {leaderboard[key]['HighestScore']}")
                    elif rknt == 3:
                        sc3.write(f"🥉 | {leaderboard[key]['NameCountry']}: {leaderboard[key]['HighestScore']}")
                """
            else:
                # Controla el caso en el que e lederboard no existe
                raise Exception("Leaderboard file does not exist")

    def update_leader_board(self, player, MAX_PLAYERS):
        leaderboard_dicc = self.read_leader_board(player)
        leaderboard_dict_lngth = len(leaderboard_dicc)

        if leaderboard_dict_lngth >= MAX_PLAYERS:  # Se llegó al máximo de jugadores en el leaderboard
            leaderboard_min_score = min(leaderboard_dicc.values())
            if player.get_current_score() > leaderboard_min_score:
                # El puntaje del jugador actual supera al puntaje mínimo del leaderboard
                # Solo se dejan en el diccionario el máximo de elementos (menos uno) para agregar como último elemento posible el jugador actual
                for i in range(leaderboard_dict_lngth - MAX_PLAYERS - 1):
                    leaderboard_dicc.popitem()
                leaderboard_dicc[MAX_PLAYERS] = {'NameCountry': player.get_country(),
                                                 'HighestScore': player.get_score()}
                # Se ordenan nuevamente el leaderboard
                leaderboard = dict(
                    sorted(leaderboard_dicc.items(), key=lambda item: item[1]['HighestScore'],
                           reverse=True))  # sort desc
        else:
            leaderboard_dicc[str(leaderboard_dict_lngth + 1)] = {'NameCountry': player.get_country(),
                                                                 'HighestScore': player.get_score()}
        # guarda en disco
        json.dump(leaderboard_dicc, open(self.leaderboard_file_name_path, 'w'))
