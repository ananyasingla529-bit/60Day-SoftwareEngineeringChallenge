num1 = float(input("Enter first number: "))
op = input("Enter operator(+, -, *, /): ")
num2 = float(input("Enter second number: "))
if(op == "+"):
  print("Sum: ", num1+num2)
elif(op=="-"):
  print("Diff: ", num1-num2)
elif(op=="*"):
  print("Multipy: ", num1*num2)
elif(op=="/"):
  if(num2==0):
    print("Error: Cannot divide by zero.")
  else:
    print("Divide: ", num1/num2)
else:
    print("Invalid operator!")
