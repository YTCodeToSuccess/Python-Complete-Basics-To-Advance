
if __name__ == "__main__":
    
    fruits_basket = ["apple", "banana", "cherry","potato", "date"]

    for fruit in fruits_basket:
        if fruit == "potato":
            print("Skipping vegetable in fruits basket.")
            continue
        print(f"Current fruit: {fruit}")
     
     # marksheets of the students
    marksheets = [85, 42, 67, 90, 33, 76, 58, 49]
    
    # assing grades on the basic of marks
    for roll_number in range(len(marksheets)):
            if marksheets[roll_number] >= 90:
                  grade = 'A'
            elif marksheets[roll_number] >= 75:
                  grade = 'B'
            elif marksheets[roll_number] >= 50:
                  grade = 'C'
            elif marksheets[roll_number] >= 35:
                  grade = 'D'
            else:
                  grade = 'F'
            
            print(f"student with roll number {roll_number} with marks {marksheets[roll_number]} has grade {grade}")
      