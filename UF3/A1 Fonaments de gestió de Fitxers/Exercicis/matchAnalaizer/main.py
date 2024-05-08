'''
Volem fer un programa que analitzi els resultats d'un partit de bàsquet.
Hem de tenir en compte que en un partit de bàsquet es poden fer 1, 2 o 3 punts.
Donat els diferents resultats analitza que està passant.
L'usuari introduirà la ruta al fitxer, el qual tindrà la següent estructura:
'''
def read_file(file_path):
    with open(file_path, 'r') as f:
        teams = f.readline().strip().split()
        points = [int(point) for point in f.readline().split()]
    return teams, points


def analyze_basketball_results(teams, points):
    team_a_score = 0
    team_b_score = 0
    for i in range(0, len(points), 2):
        point_a = points[i]
        point_b = points[i + 1]
        if point_a == 0:
            print(f"Cistella de {teams[1]}")
            team_b_score += 2
        elif point_a == 1:
            print(f"Tir lliure de {teams[0]}")
            team_a_score += 1
        elif point_a == 2:
            print(f"Triple de {teams[0]}")
            team_a_score += 3
        elif point_a == 3:
            print(f"Tir lliure de {teams[0]}")
            team_a_score += 1
        if point_b == 0:
            print(f"Cistella de {teams[0]}")
            team_a_score += 2
        elif point_b == 1:
            print(f"Tir lliure de {teams[1]}")
            team_b_score += 1
        elif point_b == 2:
            print(f"Triple de {teams[1]}")
            team_b_score += 3
        elif point_b == 3:
            print(f"Tir lliure de {teams[1]}")
            team_b_score += 1
    if team_a_score > team_b_score:
        print(f"Guanya {teams[0]}")
    elif team_a_score < team_b_score:
        print(f"Guanya {teams[1]}")
    else:
        print("Empat")


def main():
    file_path = input("Enter the path to the file with the basketball results: ")
    teams, points = read_file(file_path)
    analyze_basketball_results(teams, points)
main()