# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# code below this line v1.0 👇
if year % 4 == 0:
  if year % 100 != 0:
    print("Leap year")
  elif year % 400 == 0:
    print('Leap year')
  else:
    print("Not leap year")
else:
  print("Not leap year")

# code below this line v1.1 👇
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print('Not leap year')
  else:
    print('Leap year')
else:
  print("Not leap year")
