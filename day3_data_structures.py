numbers = list(map(int, input("Enter the numbers: ").split()))
sum=0
max=numbers[0]
min=numbers[0]
freq={}
for num in numbers:
  sum+=num
  if(num>max):
    max=num
  if(num<min):
    min=num

#Frequency
for num in numbers:
  if num in freq:
    freq[num]+=1
  else:
    freq[num]=1
print("Sum: ", sum)
print("Max: ", max)
print("Min: ", min)
print("Frequency: ")
for num in freq:
  print(num, ":", freq[num])

#Reverse list
rev=[]
for i in range(len(numbers)-1, -1, -1):
  rev.append(numbers[i])
print("Reversed list: ", rev)
  
