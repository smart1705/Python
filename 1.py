def display_profile(name, roll_no, course, age, percentage):    
    print("\n--- Student Academic Profile ---")     
    print("Name       :", name)     
    print("Roll Number:", roll_no)     
    print("Course     :", course)    
    print("Age        :", age)     
    print("Percentage :", percentage, "%")  

def main():    
    name = input("Enter student name: ").strip()     
    roll_no = input("Enter roll number: ").strip()     
    course = input("Enter course: ").strip()
    try:         
            age = int(input("Enter age: "))         
            percentage = float(input("Enter percentage: "))         
            if not name or not roll_no or not course:             
             print("Error: Fields cannot be empty.")        
            elif age < 16 or age > 100:            
             print("Error: Invalid age.")        
            elif percentage < 0 or percentage > 100:             
             print("Error: Invalid percentage.")        
            else:             
             display_profile(name, roll_no, course, age, percentage)      
    except ValueError:         
      print("Error: Enter valid numeric values.")   
if __name__ == "__main__":
      main() 