class Teacher:
    def __init__(self, arrival_day, lectures, curse_level):
        self.arrival_day = arrival_day
        self.lectures = lectures
        self.curse_level = curse_level

n, d = map(int, input().split())
teachers = []
total_curse_level = 0

# Read input and create Teacher objects
for i in range(n):
    di, ti, si = map(int, input().split())
    teachers.append(Teacher(di, ti, si))

# Sort teachers based on arrival day
teachers.sort(key=lambda teacher: teacher.arrival_day)

# Schedule lectures for each teacher
for teacher in teachers:
    lectures_taught = 0
    for day in range(teacher.arrival_day, d+1):
        if lectures_taught == teacher.lectures:
            break
        lectures_taught += 1
    if lectures_taught < teacher.lectures:
        curse_level = (teacher.lectures - lectures_taught) * teacher.curse_level
        total_curse_level += curse_level

print(total_curse_level)
