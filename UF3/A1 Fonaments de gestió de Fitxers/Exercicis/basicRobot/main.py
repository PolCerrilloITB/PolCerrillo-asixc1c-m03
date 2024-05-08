'''
Fes un programa que permeti moure un robot en un pla 2D a partir de les instruccions contingudes a un fitxer de text.
El robot ha de guardar la seva posició (X, Y) i la velocitat actual. Per defecte, la posició serà
(0, 0) i la velocitat és 1. La velocitat indica la distància que recorre el robot en cada acció.
El robot té les següents accions:
DALT: El robot es mou cap a dalt (tenint en compte la velocitat).
BAIX: El robot es mou cap a baix (tenint en compte la velocitat).
DRETA: El robot es mou cap a la dreta (tenint en compte la velocitat).
ESQUERRA: El robot es mou cap a l'esquerra (tenint en compte la velocitat).
ACCELERAR: El robot augmenta en 0.5 la velocitat. La velocitat màxima és 10.
DISMINUIR: El robot augmenta en 0.5 la velocitat. La velocitat mínima és 0.
POSICIO: El robot imprimeix la seva posició.
VELOCITAT: El robot imprimeix la seva velocitat.
El programa acaba quan llegeix del fitxer l'acció END.
Exemple
Les línies que comencen per > són les que el programa ha llegit del fitxer. Com és habitual,
el programa demanarà a l'usuari la ruta al fitxer que conté les ordres.
'''
class Robot:
    def __init__(self):
        self.position = (0, 0)
        self.velocity = 1

    def move_up(self):
        self.position = (self.position[0], self.position[1] + self.velocity)

    def move_down(self):
        self.position = (self.position[0], self.position[1] - self.velocity)

    def move_right(self):
        self.position = (self.position[0] + self.velocity, self.position[1])

    def move_left(self):
        self.position = (self.position[0] - self.velocity, self.position[1])

    def accelerate(self):
        self.velocity = min(self.velocity + 0.5, 10)

    def decelerate(self):
        self.velocity = max(self.velocity - 0.5, 0)

    def print_position(self):
        print(f"La posició del robot és {self.position}")

    def print_velocity(self):
        print(f"La velocitat del robot és {self.velocity}")

    def __str__(self):
        return f"({self.position[0]}, {self.position[1]})"


def main():
    try:
        robot = Robot()
        file_path = input("Introduce el archivo: ")
        with open(file_path, 'r') as f:
            for line in f:
                action = line.strip()
                if action == 'DALT':
                    robot.move_up()
                elif action == 'BAIX':
                    robot.move_down()
                elif action == 'DRETA':
                    robot.move_right()
                elif action == 'ESQUERRA':
                    robot.move_left()
                elif action == 'ACCELERAR':
                    robot.accelerate()
                elif action == 'DISMINUIR':
                    robot.decelerate()
                elif action == 'POSICIO':
                    robot.print_position()
                elif action == 'VELOCITAT':
                    robot.print_velocity()
                elif action == 'END':
                    break
                else:
                    print(f"Unknown action: {action}")
                print(f">{action}")
                print(robot)
    except:
        print("Warning: File did not end with END action")
main()