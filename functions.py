def letter_grade(grade):
    """function to find the final grade of a class"""
    try:
        percent = float(grade)
        if percent <= 100 and percent >= 0:
            if percent >= 90:
                return 'A'
            elif percent >= 80:
                return 'B'
            elif percent >= 70:
                return 'C'
            elif percent >= 60:
                return 'D'
            else:
                return 'F'
        else:
            return False
    except ValueError:
        return False

def conversion(letter):
    if letter == 'A':
        return 4
    elif letter == 'B':
        return 3
    elif letter == 'C':
        return 2
    elif letter == 'D':
        return 1
    else:
        return 0

def average(*args):
    total = 0
    for i in args:
        total += i
    average = total / len(args)
    return average
