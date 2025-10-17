try:
  age=int(input("enter your age:"))
  if age >=19:
    print("you are eligible to vot")
  else:
    print("you are not eligible to vote")
except valueerrors:
  print("please enter a valid integer")
