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