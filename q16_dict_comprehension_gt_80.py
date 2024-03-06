# [dictionary comprehension] Given a dictionary with students' names as keys and their respective scores as values, create a new dictionary that contains only the students who scored more than 80 using dictionary comprehension.


student_score = {"Luffy":40, "Zoro":60, "Robin":95, "Nami":85, "Ussop":83, "Chopper":90}
student_score_gt_80 = {key:value for key, value in student_score.items() if value > 80}

print(student_score_gt_80)