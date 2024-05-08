'''
Volem fer un marcador per un partit de squash a partir de la història d'esdeveniments del partit
continguda a un fitxer de text.
Encara que hi ha diferents formes de puntuar, una de les més utilitzades pels jugadors amateurs és jugar al
millor de cinc sets, és a dir, el jugador que abans guanyi tres sets guanya el partit i acaba el joc.
Els sets es juguen a 9 punts:
Cal guanyar amb un avantatge de com a mínim dos punts. Si s'arriba a un empat a 8, guanyarà el que arribi a 10.
Si s'empata a 9, es jugarà a 11, etc…
Els punts només pugen al marcador si el que guanya el punt tenia el servei. És a dir, es fa servir el que es coneix
com a "recuperació del servei". Si el jugador A saca i guanya el punt, aquest puja al seu marcador.
Però si el punt el guanya B, atès que no ha sacat ell, recupera el servei però no puntua.
El jugador que guanya un set comença sacant en el següent.
Ens demanen esbrinar el marcador final de cada un dels sets d'un partit d'esquaix coneixent els
guanyadors de tots els punts. És possible que el partit no acabi a causa que el lloguer
de la pista arriba a la seva fi: és a dir, la història del partit continguda al fitxer no té per què resultar
en un guanyador. En aquest cas es presentarà el resultat parcial.
L'usuari primer introduirà la ruta al fitxer amb la història del partit.
De cada partit, escriurà qui guanya cada punt i finalitzarà amb una F.
'''
class Scoreboard:
    def __init__(self):
        self.player_a_score = 0
        self.player_b_score = 0
        self.player_a_serve = True

    def update_score(self, player):
        if player == 'A' and self.player_a_serve:
            self.player_a_score += 1
        elif player == 'B' and not self.player_a_serve:
            self.player_b_score += 1
        self.player_a_serve = not self.player_a_serve

    def get_score(self):
        return (self.player_a_score, self.player_b_score)

    def check_game_over(self):
        if self.player_a_score >= 9 and self.player_a_score >= self.player_b_score + 2:
            return 'A'
        elif self.player_b_score >= 9 and self.player_b_score >= self.player_a_score + 2:
            return 'B'
        else:
            return None

    def reset(self):
        self.player_a_score = 0
        self.player_b_score = 0
        self.player_a_serve = True


def main():
    file_path = input("Introduce el archivo: ")
    with open(file_path, 'r') as f:
        scoreboard = Scoreboard()
        for line in f:
            points = line.strip()
            for point in points:
                scoreboard.update_score(point)
                game_over = scoreboard.check_game_over()
                if game_over:
                    print(f"{scoreboard.get_score()[0]}-{scoreboard.get_score()[1]}")
                    scoreboard.reset()
                    break
            else:
                continue
            break
        else:
            print("Warning: Match history did not end with a F")
main()