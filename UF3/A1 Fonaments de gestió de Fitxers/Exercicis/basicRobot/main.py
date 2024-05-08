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
        file_path = input("Enter the path to the file with the orders: ")
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