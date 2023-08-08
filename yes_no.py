# Functions go here
def yes_no(qestion):
  valid = False
  while not valid:
    response = input("Have you played this game before?").lower()
    if response == "yes" or response == "y":
      response = "yes"
      return response
    elif response == "no" or response == "n":
      response ="no"
      return response
    else:
      print("Please enter yes or no")
# Main Routine goes here

   
# If they say yes, output program continues
played_before = yes_no("Have you played this game before?")

if played_before == "no":
  print("Display instructions")
elif played_before == "yes":
    name = input("What is your name ?")
print("Welcome to the times table quiz {}".format(name))
  
times = int(input("Please enter the times table you wan to get tested on"))
max_num = int(input("Enter the max number"))
score = 0
  
for i in range(1, max_num):
  
      answer = i * times
      guess = int(input("What is {} x {} = ".format(i, times)))
      if guess != answer:
          print("incorrect")
      else:
          print("Correct")
          score += 1
  