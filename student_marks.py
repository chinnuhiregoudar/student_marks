name = input("Enter student name: ")
marks = input("Enter marks: ")
no_of_subjects = input("Enter number of subjects: ")
total = 0

for i in range(int(no_of_subjects)):
    subject_marks = input(f"Enter marks for subject {i + 1}: ")
    total += int(subject_marks)

Average = total / int(no_of_subjects)
print("Average marks:",Average)
if(Average >= 50):
    print("Result: Pass")
else:
    print("Result: Fail")   