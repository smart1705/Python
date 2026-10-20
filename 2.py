def calculate_performance(marks):
    total=sum(marks)
    average=total/len(marks)
    percentage=(total/500)*100
    highest=max(marks)
    lowest=min(marks)

    print("\nStudent academic Performance")
    print("Total:",total,"/500")
    print("Average:",average)
    print("Percentage:",percentage,"%")
    print("Highest:",highest)
    print("Lowest:",lowest)

def main():
    marks=[]
    try:
        for i in range(1,6):
           mark=float(input("Enter marks for subjects:"+str(i)+":"))
           if mark<0 or mark>100:
            print("Error:marks must be between 0 and 100")
            return
           marks.append(mark)
        calculate_performance(marks)
    except ValueError:
       print("Error:Enter valid numerical values.")
if __name__=="__main__":
    main()