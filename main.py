import random
print("Please select your difficulty. Choose A number 1-5")
print("1 Easy (1-100)" )
print("2 Medium (1-500)")
print("3 Hard (1-1000)")
print("4 Impossible (????)")
print("5 Impossibler (?????)")

while True:
  diff = input("Start. Select Difficulty:")
  if diff == '1':
    Number = int(random.randrange(1, 100, 4))
    break
  if diff == '2':
    Number = int(random.randrange(1, 500, 4))
    break
  if diff == '3':
    Number = int(random.randrange(1, 1000, 4))
    break
  if diff == '4':
    Number = int(random.randrange(1, 5000, 4))
    break
  if diff == '5':
    Number = int(random.randrange(1, 10000, 4))
    break
  else:
    print("Please select a number 1-5")

while True:
  Guess = input("Guess a number: ")
  if int(Guess) < Number:
     print("Too low")
  elif int(Guess) > Number:
     print("Too high")
  elif int(Guess) == Number:
    print("You guessed it!")
    print("1 Easy (1-100)" )
    print("2 Medium (1-500)")
    print("3 Hard (1-1000)")
    print("4 Impossible (????)")
    print("5 Impossibler (?????)")
    diff = input("Select The Difficulty Again:")
    if diff == '1':
     Number = (random.randrange(1, 100, 4))
    if diff == '2':
     Number = (random.randrange(1, 500, 4))
    if diff == '3':
     Number = (random.randrange(1, 1000, 4))
    if diff == '4':
      Number = (random.randrange(1, 5000, 4))
    if diff == '5':
     Number = (random.randrange(1, 10000, 4))
  else:
   print("Invalid Input")
   continue