number = int(input("Enter the number to check for Strong Arms: "))
number = str(number)
digits= len(number)

print(f"Checking if {number} with {digits} is an armstrong number or not")
sum = 0
for i in number:
  sum=sum+int(i)**digits
print(sum)

if sum == int(number):
  print("It is an armstrong number!")
else:
  print("It is not an armstrong number")