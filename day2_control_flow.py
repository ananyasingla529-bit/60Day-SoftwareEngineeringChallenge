try:
  marks = float(input("Enter your marks: "))
  if(marks<0 or marks>100):
    print("Invalid marks! Please enter marks between 0 and 100.")
  elif(marks>90):
    print("A \nPassed")
  elif(marks>75):
    print("B \nPassed")
  elif(marks>50):
    print("C\nPassed")
  else:
    print("Fail\nFailed")
except ValueError:
  print("Invalid input! Please enter a number.")
