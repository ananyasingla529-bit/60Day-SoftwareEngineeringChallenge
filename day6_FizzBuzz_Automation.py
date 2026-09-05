N = int(input("Enter N: "))
r=[]
for i in range(1, N+1):
  if(i%3==0):
    result="Fizz"
  elif(i%5==0):
    result="Buzz"
  elif(i%3==0 and i%5==0):
    result="FizzBuzz"
  else:
    result=str(i)
  print(result)
  r.append(result)

#output in new file
with open("fizzbuzz_output.txt", "w") as file:
  for i in r:
    file.write(i + "\n")

print("\nOutput saved to fizzbuzz_output.txt")
