# [**kwargs] Create a function create_student_report that takes the student's name as the first argument, the student's age as the second argument, and an arbitrary number of keyword arguments for the subjects and their respective scores. The function should return a dictionary with the student's information and a list of subjects along with their scores.

def create_student_report(name, age, **kwargs):
    student_info = {"name": name, 
              "age" : age}
    scores = []
    for subject, score in kwargs.items():
        scores.append((subject, score)) 

    return student_info, scores

student_info, scores = create_student_report(name="John", age=23, science=60, math=80, social=50, computer=90)
print(student_info)
print(scores)