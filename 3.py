def calculate_grade(percentage):
    if percentage>=90:
        grade="A"
    elif percentage>=75:
        grade="B"
    elif percentage>=60:
        grade="C"
    elif percentage>=35:
        grade="D"
    else:
        grade="F"

    if percentage>=35:
        status="Pass"
    else:
        status="Fail"

    print("\nStudent Academic Performance")
    print("Percentage:",percentage)
    print("Grade:",grade)
    print("Status:",status)

def main():
    try: 
        percentage=float(input("Enter percentage:"))
        if percentage<0 or percentage>100:
           print("Error: Percentage must be between 0 and 100.")
        else:
           calculate_grade(percentage)        
    except ValueError:
      print("Error:Enter valid numerical values.")
if __name__=="__main__":
    main()