import json

def get_random_grade():
    grade = random.choices(
        list(
            GRADES.keys()),
        weights=[
            grade['weight'] for grade in GRADES.values()])[0]
    return grade
    