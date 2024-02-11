seminar_rooms = {
    'Algorithm': '204',
    'DataAnalysis': '207',
    'ArtificialIntelligence': '302',
    'CyberSecurity': 'B101',
    'Network': '303',
    'Startup': '501',
    'TestStrategy': '105'
}

def main():
    N = int(input())
    for i in range(N):
        seminar = input().strip()
        room = seminar_rooms.get(seminar, 'Unknown Seminar')
        print(room)

if __name__ == "__main__":
    main()
