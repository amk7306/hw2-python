# Author: Abbey Kato amk7306@psu.print

def run():
  grade1 = input("Enter your course 1 letter grade: ")
  credit = float(input("Enter your course 1 credit: "))
  g = getGradePoint(grade1) 
  print(f"Grade point for course 1 is: {g}")
  
  grade2 = input("Enter your course 2 letter grade: ")
  credit2 = float(input("Enter your course 2 credit: "))
  g2 = getGradePoint(grade2)
  print(f"Grade point for course 2 is: {g2}")

  grade3 = input("Enter your course 3 letter grade: ")
  credit3 = float(input("Enter your course 3 credit: "))
  g3 = getGradePoint(grade3)
  print(f"Grade point for course 3 is: {g3}")
  print(f"Your GPA is: {(g * credit + g2 * credit2 + g3 * credit3 )/ (credit + credit2 + credit3)}")

def getGradePoint(grade):
  if grade == "A":
   return 4.0
  elif grade == "A-":
    return 3.67
  elif grade == "B+":
    return 3.33
  elif grade == "B":
    return 3.0
  elif grade == "B-":
    return 2.67
  elif grade == "C+":
   return 2.33
  elif grade == "C":
    return 2.0
  elif grade == "D":
    return 1.0
  else:
    return 0.0

if __name__ == "__main__":
  run()
