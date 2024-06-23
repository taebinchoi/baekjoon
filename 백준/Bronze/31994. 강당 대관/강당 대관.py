seminars = []

for i in range(7):
    seminar_info = input().strip()
    seminars.append(seminar_info)

max_attendees = 0
seminar_name = ""

for seminar in seminars:
    name, attendees = seminar.split()
    attendees = int(attendees)
    
    if attendees > max_attendees:
        max_attendees = attendees
        seminar_name = name

print(seminar_name)