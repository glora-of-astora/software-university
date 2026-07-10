name_of_student = input()

grade = 1
total_score = 0.0
average_score = 0.0
strikes = 0

while True:
    new_score = float(input())

    if new_score < 4.00:
        strikes += 1

        if strikes == 2:
            print(f'{name_of_student} has been excluded '
                  f'at {grade} grade')
            break
        continue

    total_score += new_score
    average_score = total_score / grade

    if (grade == 12) and (average_score >= 4.00):
        print(f'{name_of_student} graduated. '
          f'Average grade: {average_score:.2f}')
        break
    grade += 1