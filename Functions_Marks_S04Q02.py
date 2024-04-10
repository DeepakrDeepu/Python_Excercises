def Percentage(score):
    if score >= 90:
        print("Student obtained first class")
    elif 75 <= score < 90:
        print("Student obtained second class")
    elif 35 <= score < 75:
        print("Just Pass")
    else: 
        print("Failed in exam")
        
def get_number(subject):
    return float(input(f"Enter the marks obtained in {subject} subject: "))

English = get_number("English")
Science = get_number("Science")
Maths = get_number("Maths")

Total_Marks_Obtained = English + Science + Maths
Total_Maximum_Marks = 80 + 90 + 100
Percentage_Marks = (Total_Marks_Obtained / Total_Maximum_Marks) * 100

Percentage(Percentage_Marks)
