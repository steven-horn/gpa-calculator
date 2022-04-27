def valid_score(grade):
    """Function to check that the input is acceptable. If not, it will display an error message."""
    try:
        grade = float(grade)
        if grade < 0 or grade > 120:
            return False
        else:
            return grade
    except ValueError:
        return False


def average(grades):
    """function to find the average of the class' grades"""
    total = 0
    number_of_grades = 0
    for i in grades:
        total += i
        number_of_grades += 1
    final_grade = total/number_of_grades
    return final_grade


def letter_grade(grade):
    """function to find the final grade of a class"""
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'
