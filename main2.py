number = int(input("Please give me a number: "))
number_factor = int(input("Please give a factor of the number: "))

if number%number_factor == 0:
  print("It is a factor")

else:
  print("It is not a factor")