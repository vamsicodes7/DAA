#instance of class
class Teacher:
    def __init__(self, di, ti, si):
        self.di = di
        self.ti = ti
        self.si = si

def minimize_curse(n, d, teachers):
    # Sort teachers by curse level (Si) in descending order
    teachers.sort(key=lambda teacher: teacher.si, reverse=True)

    total_curse = 0
    current_day = 1
# O(n log n)
    for teacher in teachers:
        # Check if the teacher arrives after the lockdown day   O(n)
        if teacher.di > d:
            total_curse += teacher.ti * teacher.si
        else:
            # Check if there are enough days left to schedule all lectures
            if current_day <= teacher.di:
                # Schedule all lectures for this teacher
                lectures_scheduled = min(teacher.ti, d - teacher.di + 1)
                total_curse += teacher.si * (teacher.ti - lectures_scheduled)
                current_day = teacher.di + lectures_scheduled
            else:
                # Calculate the number of lectures that can be scheduled  O(1)
                lectures_scheduled = min(teacher.ti, d - current_day + 1)
                total_curse += teacher.si * (teacher.ti - lectures_scheduled)
                current_day += lectures_scheduled

    return total_curse

# O(n log n)
# Example usage and input reading
n, d = map(int, input().split())
teachers = []
for _ in range(n):
    di, ti, si = map(int, input().split())
    teachers.append(Teacher(di, ti, si))

# Calculate and print the minimum total curse
result = minimize_curse(n, d, teachers)
print(result)
