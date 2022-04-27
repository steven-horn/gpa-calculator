def valid_score(grade):
    """Function to check that the input is acceptable. If not, it will display an error message."""
    try:
        float(grade)
        if grade < 0 or grade > 120:
            return False
        else:
            return grade
    except ValueError:
        return False

def average(grades):
    total = 0
    for i in range(grades):
        total += grades[i]
    final_grade = total/range(grades)
    return final_grade

def letter_grade(grade):
    if grade >= 90:
        print('Grade: A')
    elif grade >= 80:
        print('Grade: B')
    elif grade >= 70:
        print('Grade: C')
    elif grade >= 60:
        print('Grade: D')
    else:
        print('Grade: F')
