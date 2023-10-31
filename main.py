import random
print("Please select your difficulty. Choose A number 1-5")
print("1 Easy (1-100)" )
print("2 Medium (1-500)")
print("3 Hard (1-1000)")
print("4 Impossible (????)")
print("5 Impossibler (?????)")
# Stating Difficulties

while True:
  diff = input("Start. Select Difficulty:")
# Selects Difficulty
  if diff == '1': 
    Number = int(random.randrange(1, 100, 4))
# Creates Random Number
    Attempts = 25
# Creates Attempts
    break
# So Loop Won't Repeat
  if diff == '2':
    Number = int(random.randrange(1, 500, 4))
    Attempts = 23
    break
  if diff == '3':
    Number = int(random.randrange(1, 1000, 4))
    Attempts = 21
    break
  if diff == '4':
    Number = int(random.randrange(1, 5000, 4))
    Attempts = 19
    break
  if diff == '5':
    Number = int(random.randrange(1, 10000, 4))
    Attempts = 17
    break
  else:
    print("Please select a number 1-5")
# So It Can't Break On Invalid Input
while True:
  Guess = input("Guess a number:")
# Guesses number
  try:
    if int(Guess) < Number:
  # Checks The Guess compared to numver
     print("Too Low,", Attempts, "Attempts Left")
     Attempts = int(Attempts) - 1
# Makes Attempts Work

     if int(Attempts) < int(1):
       print("You Lost, Please Try Again")
       diff = input("Select The Difficulty Again:")
       if diff == '1':
         Number = int(random.randrange(1, 100, 4))
         Attempts = 25
       if diff == '2':
         Number = int(random.randrange(1, 500, 4))
         Attempts = 23
       if diff == '3':
         Number = int(random.randrange(1, 1000, 4))
         Attempts = 21
       if diff == '4':
         Number = int(random.randrange(1, 5000, 4))
         Attempts = 19
       if diff == '5':
         Number = int(random.randrange(1, 10000, 4))
         Attempts = 17
       else:
        print("Please select a number 1-5")
# Loops The Game
    elif int(Guess) > Number:
# Same As Above
     print("Too high,", Attempts, "Attempts Left")
     Attempts = int(Attempts) - 1
     if int(Attempts) < int(1):
       print("You Lost, Please Try Again")
       diff = input("Select The Difficulty Again:")
       if diff == '1':
         Number = int(random.randrange(1, 100, 4))
         Attempts = 25
       if diff == '2':
         Number = int(random.randrange(1, 500, 4))
         Attempts = 23
       if diff == '3':
         Number = int(random.randrange(1, 1000, 4))
         Attempts = 21
       if diff == '4':
         Number = int(random.randrange(1, 5000, 4))
         Attempts = 19
       if diff == '5':
         Number = int(random.randrange(1, 10000, 4))
         Attempts = 17
       else:
        print("Please select a number 1-5")
    elif int(Guess) == Number:
  # In Case Of Correct Guess
      print("You guessed it!")
      print("1 Easy (1-100)" )
      print("2 Medium (1-500)")
      print("3 Hard (1-1000)")
      print("4 Impossible (????)")
      print("5 Impossibler (?????)")
      diff = input("Select The Difficulty Again:")
      if diff == '1':
       Number = int(random.randrange(1, 100, 4))
       Attempts = 25
      if diff == '2':
       Number = int(random.randrange(1, 500, 4))
       Attempts = 23
      if diff == '3':
       Number = int(random.randrange(1, 1000, 4))
       Attempts = 21
      if diff == '4':
       Number = int(random.randrange(1, 5000, 4))
       Attempts = 19
      if diff == '5':
       Number = int(random.randrange(1, 10000, 4))
       Attempts = 17
      else:
       print("Please select a number 1-5")

  except ValueError:
   print("Invalid Input")
# Allows Code To Continue With Invalid Inputs
   continue
