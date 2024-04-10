def Percentage(score):
    if score >= 90:
        print("Student obtained first class")
    elif 75 <= score < 90:
        print("Student obtained second class")
    elif 35 <= score < 75:
        print("Just Pass")
    else: 
        print("Failed in exam")

# Get marks obtained in English, Science, and Mathematics from the user
English = float(input("Enter the marks obtained in English subject: "))
Science = float(input("Enter the marks obtained in Science subject: "))
Maths = float(input("Enter the marks obtained in Mathematics subject: "))

Total_Marks_Obtained = English + Science + Maths
Total_Possible_Marks = 80 + 90 + 100
Percentage_Marks = (Total_Marks_Obtained / Total_Possible_Marks) * 100

Percentage(Percentage_Marks)
