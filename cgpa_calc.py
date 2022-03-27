def cgpa_calc():
    cgpa=0
    year=int(input("Enter the year of student: "))
    sem=int(input("Enter the number of semester: "))
    for i in range(1,sem+1):
        cpa=float(input(f"Enter GPA of sem{i}: "))
        cgpa=cgpa+cpa
    res=cgpa/sem
    print("Your CGPA is: ",round(res,2))


cgpa_calc()
    