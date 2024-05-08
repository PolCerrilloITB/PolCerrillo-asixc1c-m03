class Lamp:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def toggle(self):
        self.is_on = not self.is_on

    def __str__(self):
        return str(self.is_on)


def main():
    try:
        lamp = Lamp()
        with open('actions.txt', 'r') as f:
            for line in f:
                action = line.strip()
                if action == 'TURN ON':
                    lamp.turn_on()
                elif action == 'TURN OFF':
                    lamp.turn_off()
                elif action == 'TOGGLE':
                    lamp.toggle()
                elif action == 'END':
                    break
                else:
                    print(f"Unknown action: {action}")
                print(f">{action}")
                print(lamp)
    except:
        print("Warning: File did not end with END action")


if __name__ == "__main__":
    main()