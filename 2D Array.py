marks = [
    [45, 60, 70],   # Student 1
    [90, 85, 88],   # Student 2
    [0, 55, 40],    # Student 3 (scored 0 in Subject1)
    [72, 0, 65],    # Student 4 (scored 0 in Subject2)
    [50, 60, 55]    # Student 5
]

students = 5
subjects = 3
def show_marks():
    print("\n--- Marks Table ---")
    print("Student   Sub1  Sub2  Sub3")
    for i in range(students):
        print("Student", i + 1, "  ",
              marks[i][0], "   ", marks[i][1], "   ", marks[i][2])

def find_maximum():
    max_marks = marks[0][0]
    for i in range(students):
        for j in range(subjects):
            if marks[i][j] > max_marks:
                max_marks = marks[i][j]
    return max_marks

def find_minimum():
    min_marks = marks[0][0]   # start by assuming the first value is min
    for i in range(students):
        for j in range(subjects):
            if marks[i][j] < min_marks:
                min_marks = marks[i][j]
    return min_marks

def find_average():
    total = 0
    count = 0
    for i in range(students):
        for j in range(subjects):
            total = total + marks[i][j]
            count = count + 1
    average = total / count
    return average

def find_zero_scorers():
    zero_students = []
    for i in range(students):
        for j in range(subjects):
            if marks[i][j] == 0:
                zero_students.append("Student " + str(i + 1))
                break   # no need to check other subjects for this student
    return zero_students
show_marks()

print("\nMaximum Marks:", find_maximum())
print("Minimum Marks:", find_minimum())
print("Average Marks:", find_average())

zero_list = find_zero_scorers()
if zero_list:
    print("Students with zero marks in any subject:", zero_list)
else:
    print("No student scored zero marks in any subject.")