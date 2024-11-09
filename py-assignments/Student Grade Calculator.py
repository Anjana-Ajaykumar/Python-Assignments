#Calculate grades based on scores
def grade(avg_score):
    if (avg_score>=90 and avg_score<=100):
        print("A Grade")
    elif (avg_score>=80 and avg_score<=89):
        print("B Grade")
    elif (avg_score>=70 and avg_score<=79):
        print("C Grade")
    elif (avg_score>=60 and avg_score<=69):
        print("D Grade")
    elif(avg_score<60):
        print("F Grade")

stu_name=input("Enter student name :")# Asks for student name
list=["Maths","Computer Science","Statistics","Language","English"]
total_marks=0
for i in list:
    mark=int(input("Enter the marks in {} :".format(i)))#Ask for marks in each subject
    total_marks+=mark
avg=total_marks/len(list)
grade(avg)#Call grade function to find grade based on average of scores
