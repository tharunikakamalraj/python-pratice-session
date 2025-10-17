student_name=[]
student_mark=[]
num_student = int(input("How many students?"))
for i in range(num_student):
    name = input(f"Enter student name{i+1}:")
    mark = int(input(f"Enter the  mark of {name}:"))
    student_name.append(name)
    student_mark.append(mark)
print("\n---All student records---")
for i in range(len(student_name)):
    print(f"{student_name[i]}-{student_mark[i]} mark")

highest = max(student_mark)
lowest = min(student_mark)
average = sum(student_mark)/ len(student_mark)

print("/n---statistcs---")
print("Highest mark:",highest)
print("Lowest mark ",lowest)
print("Average mark",average)
print("/n---passed student---")
for i in range(len(student_name)):
    if student_mark[i] >= 40:
        print(f"{student_name[i]}-{student_mark[i]}")
print("\n---failed student---")
for i in range(len(student_name)):
    if student_mark[i] < 40:
        print(f"{student_name[i]}-{student_mark[i]}")
            
    