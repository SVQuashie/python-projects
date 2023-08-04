# Let user input year to be checked
year = int(input("Which year do you want to check? "))

# Determine whether year is a leap year
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print(" Not Leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")