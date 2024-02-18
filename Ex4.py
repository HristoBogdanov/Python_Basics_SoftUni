num_students = int(input())

top_students = 0
between_4_and_499 = 0
between_3_and_399 = 0
fail_students = 0
total_score = 0

for _ in range(num_students):
    grade = float(input())
    total_score += grade
    if grade >= 5.00:
        top_students += 1
    elif 4.00 <= grade <= 4.99:
        between_4_and_499 += 1
    elif 3.00 <= grade <= 3.99:
        between_3_and_399 += 1
    else:
        fail_students += 1

percent_top_students = (top_students / num_students) * 100
percent_between_4_and_499 = (between_4_and_499 / num_students) * 100
percent_between_3_and_399 = (between_3_and_399 / num_students) * 100
percent_fail_students = (fail_students / num_students) * 100
average_score = total_score / num_students

print(f"Top students: {percent_top_students:.2f}%")
print(f"Between 4.00 and 4.99: {percent_between_4_and_499:.2f}%")
print(f"Between 3.00 and 3.99: {percent_between_3_and_399:.2f}%")
print(f"Fail: {percent_fail_students:.2f}%")
print(f"Average: {average_score:.2f}")
