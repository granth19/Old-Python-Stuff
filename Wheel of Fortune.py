import random
import time
HANGMANPICS = []
money=0
money2=0
money3=0
money4=0
money5=0
money6=0
spin=0
flag1=False
#words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
#words=["ant"]
TvShow=[ "How To Get Away With Murder", "Nbc Nightly News With Brian Williams", "So You Think You Can Dance", "The Daily Show With Jon Stewart", "The Real Housewives Of Beverly Hills", "The Tonight Show Starring Jimmy Fallon", "Then And Now With Andy Cohen", "Through The Wormhole With Morgan Freeman", "How I Met Your Mother", "Late Show With David Letterman", "Law And Order Special Victims Unit", "Men Of A Certain Age", "Say Yes To The Dress", "Star Trek Deep Space Nine", "The Bold And The Beautiful", "The Young And The Restless", "America's Funniest Home Videos", "America's Next Top Model"]
InTheKitchen=["A Jar Of Spaghetti Sauce", "A New Mixer", "A Package Of Brown Gravy Mix", "A Pan Of Hot Oil", "A Roll Of Paper Towels", "A Well-Stocked Pantry", "Abrasive Pads", "Adhesive Shelf Liners", "Airtight Canisters", "All-In-One Appliance", "All-Purpose Flour", "Alphabet Refrigerator Magnet", "Aluminum Cheese Grater", "Angel Food Cake Mix", "Antique Salt & Pepper Shakers", "Appetizer & Dessert Plates", "Arm & Hammer Baking Soda", "Asian Kitchen", "Automatic Coffee Machine", "Automatic Dishwasher"]
songAndArtist=["Adventure Of A Lifetime By Coldplay", "Again By Janet Jackson", "American Pie By Don Mclean", "An Old Fashioned Love Song By Three Dog Night", "Animal By Def Leppard", "Another Brick In The Wall By Pink Floyd", "Baby Baby By Amy Grant", "Backroad Song By Granger Smith", "Best Friend By Brandy", "Best Of My Love By The Eagles", "Biscuits By Kacey Musgraves", "Black Cow By Steely Dan", "Black Magic Woman By Santana", "Blank Space By Taylor Swift", "Blueberry Hill By Fats Domino", "Boombastic By Shaggy", "Born To Run By Bruce Springsteen", "Breathless By Sam Riggs", "Burning House By Cam", "Candle In The Wind By Elton John"]
people=["A Friend Of A Friend", "A Good Sport", "A Man Of Great Character", "A Member In Good Standing", "A Millionaire Many Times Over", "A Real Crowd-Pleaser", "A Source Who Asked Not To Be Identified", "A Special Someone", "A World Traveler", "A Worthy Opponent", "Able Seaman", "Acclaimed Actor", "Acclaimed Film Director", "Acclaimed Filmmaker", "Accordion Player", "Accordionist", "Acting Mayor", "Active Bicyclist", "Adolescent Clowning Around", "Adorable Baby", "Advanced Beginner"]
words2=[ "A Bag Of Baby Spinach", "A Big Batch Of Hot Chili", "A Big Box Of Assorted Chocolates", "A Big Plate Of SpaghettI", "A Bowl Of Fresh Berries", "A Bowl Of Homemade Warm Biscuits", "A Bowl Of Pico De Gallo With Chips", "A Bowl Of Warm Biscuits", "A Bowl Of Wonton Noodles", "A Box Of Chewy Caramels", "A Can Of Condensed Tomato Soup", "A Cup Of Coffee And A Cookie", "A Cup Of Hot Chocolate", "A Delicious Meat Soup Called Fatta", "A Dollop Of Yogurt", "A Glass Of Ginger Juice", "A Glass Of Vino", "A Huge Bowl Of Fresh Raw Oysters", "A Large Glass Bowl Of Green Candy"]
words1=[ "Brave New World", "Clifford The Big Red Dog", "East Of Eden", "Encyclopedia Britannica", "Gullivers Travels", "Jane Eyre", "Main Branch", "My Life In France", "Out Of Africa", "Outline Of History", "Patriot Games", "Pride And Prejudice", "Rebecca Of Sunnybrook Farm", "Something Wicked This Way Comes", "The Brass Verdict", "The Call Of The Wild", "The Chronicles Of Narnia", "The Gourmet Cookbook", "The Grapes Of Wrath", "The Great Gatsby"]
words=["A Pile Of Coats", "A Shelf Full Of Knickknacks", "Accent Cabinet", "Accent Furniture", "Address Labels", "Adjustable Shoes", "Afghan Rug", "After-Shave Lotion", "Air Freshener", "Air Mattress", "Alarm Clock", "Antibacterial Hand Wipes", "Antiplaque Mouthwash", "Antique Bathtub", "Antique Desk Lamp", "Antique Dining Table", "Antique Furnishings", "Antique Jewelry Box", "Antique Polaroid Camera", "Antique Porcelain Vase"]
wheel=[500,200,550,400,200,900,250,300,900,350,500,"Bankrupt",700,500,800,300,500,500,250,350,200,600,"Bankrupt"]
#wheel =["Bankrupt", 100]
def getRandomWord(wordList):
  # This function returns a random string from the passed list of strings.
  wordIndex = random.randint(0, len(wordList) - 1)
  return wordList[wordIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
  #print(HANGMANPICS[len(missedLetters)])
  #print()

  print 'Missed letters:',
  for letter in missedLetters:
      print letter,
  print()

  blanks = '_' * len(secretWord)

  for i in range(len(secretWord)): # replace blanks with correctly guessed letters
      if secretWord[i] in correctLetters:
          blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

  for letter in blanks:       # show the secret word with spaces in between each letter
      print letter,
  print()

def getGuess(alreadyGuessed):
  # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
  while True:
      #print()
      guess = raw_input('Guess a letter:')
      guess = guess.lower()
      if len(guess) != 1:
          print('Please enter a single letter.')
      elif guess in alreadyGuessed:
          print('You have already guessed that letter. Choose again.')
      elif guess not in 'abcdefghijklmnopqrstuvwxyz':
          print('Please enter a LETTER.')
      elif guess in "aeiou":
          print "You have to buy a vowel"
      else:
          return guess

def playAgain():
  # This function returns True if the player wants to play again, otherwise it returns False.
  print('Do you want to play again? (yes or no)')
  return raw_input().lower().startswith('y')
wins=0
#print('H A N G M A N')
print "Wheel of Fortune"
missedLetters = ''
correctLetters = ' '
secretWord = getRandomWord(random.choice([words,words1, words2, people, songAndArtist, InTheKitchen, TvShow]))
if secretWord in words:
  hint = "Hint: Around the House"
  print hint
if secretWord in words1:
  hint = "Hint: Book Title"
  print hint
if secretWord in words2:
    hint ="Hint: Food and Drink"
    print hint
if secretWord in people:
    hint = "Hint: People"
    print hint
if secretWord in songAndArtist:
    hint= "Hint: Song and Artist"
    print hint
if secretWord in InTheKitchen:
    hint= "Hint: In the Kitchen"
    print hint
if secretWord in TvShow:
    hint= "Hint: TV Show Title"
    print hint
secretWord=secretWord.lower()
gameIsDone = False
gamesPlayed=0
placeHolder=True
spinChoice=0
guess=""
player=1
player1Win=False
player2Win=False
player3Win=False
while True:
  flag=False
  time.sleep(.1)
  displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
  if player ==4:
      player=1
  if player ==1:
      print "Player 1"
  if player ==2:
      print "Player 2"
  if player==3:
      print "Player 3"
  spinChoice = raw_input("Do you want to spin(s), buy a vowel(v) for $250, or solve the puzzle(p)?")
  while spinChoice not in "svp":
      spinChoice = raw_input("Do you want to spin(s), buy a vowel(v) for $250, or solve the puzzle(p)?")
  if spinChoice == "p":
      solution = raw_input("What do you think the answer is?")
      solution = solution.lower()
      if solution == secretWord:
          if player ==1:
              player1Win=True
          if player ==2:
              player2Win=True
          if player==3:
              player3Win=True
          print('Yes! The secret word is "' + secretWord + '"! You have won!')
          wins = wins + 1
          gameIsDone = True
      if solution != secretWord:
        print "Sorry!!! Incorrect"
        print
        player = player + 1
        #displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
        #spinChoice = raw_input("Do you want to spin(s) or buy a vowel(v) or solve the puzzle(p)?")
        #if spinChoice not in "sv":
         #   solution = raw_input("What do you think the answer is?")
  if spinChoice == "v" and "a" in (missedLetters + correctLetters) and "e" in (missedLetters + correctLetters) and "i" in (missedLetters + correctLetters) and "o" in (missedLetters + correctLetters) and "u" in (missedLetters + correctLetters):
      print "You have guessed all vowels"
      #spinChoice = raw_input("Do you want to spin(s) or buy a vowel(v) or solve the puzzle(p)?")
  if player==1:
    if money < 250 and spinChoice == "v":
      #player=player-1
      print "You don't have enough money for a vowel"
      print
  if player == 2:
    if money2 < 250 and spinChoice == "v":
      #player = player - 1
      print "You don't have enough money for a vowel"
      print
  if player == 3:
     if money3 < 250 and spinChoice == "v":
            #player = player - 1
            print "You don't have enough money for a vowel"
            print
      #spinChoice = raw_input("Do you want to spin(s) or buy a vowel(v) or solve the puzzle(p)?")
  if player ==3:
      if spinChoice == "v" and money3 >= 250:
          money3 = money3 - 250
          vowelChoice = raw_input("What vowel do you want?")
          while vowelChoice in (correctLetters + missedLetters):
              print "You already chose that letter"
              vowelChoice = raw_input("What vowel do you want?")
          while vowelChoice not in "aeiou":
              print "Choose a vowel"
              vowelChoice = raw_input("What vowel do you want?")
          if vowelChoice in secretWord:
            correctLetters = correctLetters + vowelChoice
          else:
            player = player + 1
            missedLetters = missedLetters + vowelChoice
  if player ==2:
      if spinChoice == "v" and money2 >= 250:
          money2 = money2 - 250
          vowelChoice = raw_input("What vowel do you want?")
          while vowelChoice in (correctLetters + missedLetters):
              print "You already chose that letter"
              vowelChoice = raw_input("What vowel do you want?")
          while vowelChoice not in "aeiou":
              print "Choose a vowel"
              vowelChoice = raw_input("What vowel do you want?")
          if vowelChoice in secretWord:
            correctLetters = correctLetters + vowelChoice
          else:
            player = player + 1
            missedLetters = missedLetters + vowelChoice
  if player==1:
      if spinChoice == "v" and money >= 250:
          money = money - 250
          vowelChoice = raw_input("What vowel do you want?")
          while vowelChoice in (correctLetters + missedLetters):
              print "You already chose that letter"
              vowelChoice = raw_input("What vowel do you want?")
          while vowelChoice not in "aeiou":
              print "Choose a vowel"
              vowelChoice = raw_input("What vowel do you want?")
          if vowelChoice in secretWord:
            correctLetters = correctLetters + vowelChoice
          else:
            player = player + 1
            missedLetters = missedLetters + vowelChoice
  spin1 = random.choice(wheel)
  if spinChoice == "s":
      if spin1=="Bankrupt":
          guess=""
          flag=True
          print "You spun Bankrupt"
          print
          if player == 1:
              money=0
          if player == 2:
              money2=0
          if player == 3:
              money3=0
          player = player + 1
  if spinChoice not in "vp" and gameIsDone==False and spin1 != "Bankrupt":
    print "You spun $", spin1
    time.sleep(.1)
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
    guess = getGuess(missedLetters + correctLetters)
  else:
      spin1=0
  if guess in secretWord:
      correctLetters = correctLetters + guess
      if player ==1:
          money = money + spin1 * (secretWord.count(guess))
      if player == 2:
          money2= money2 + spin1 * (secretWord.count(guess))
      if player==3:
          money3= money3 + spin1 * (secretWord.count(guess))
  if guess not in secretWord and spinChoice not in "vp" and flag ==False:
    player = player + 1
    if guess not in missedLetters:
        missedLetters = missedLetters + guess
  if gameIsDone==False:
      print hint
      if player == 1:
          print "Player 1 Total is $", money
      if player == 2:
          print "Player 2 Total is $", money2
      if player == 3:
          print "Player 3 Total is $", money3

  # Let the player type in a letter.
  #guess = getGuess(missedLetters + correctLetters)
  correctLetters = correctLetters + guess + " "

              # Check if player has guessed too many times and lost
      #if len(missedLetters) == len(HANGMANPICS) - 1:
         # displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
          #print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
          #gameIsDone = True

  # Ask the player if they want to play again (but only if the game is done).
  if gameIsDone:
      guess=""
      gamesPlayed = gamesPlayed + 1
      if player1Win:
          print "Player 1 won the round"
      if player2Win:
          print "Player 2 won the round"
      if player3Win:
          print "Player 3 won the round"
      if player1Win:
          money4 = money + money4
      if player2Win:
          money5 = money2 + money5
      if player3Win:
          money6 = money3 + money6
      money=0
      money2=0
      money3=0
      print "Total Money"
      print "Player 1 $", money4
      print "Player 2 $", money5
      print "Player 3 $", money6
      print "You have played", gamesPlayed, "round(s)."
      #player = 1
      player=player+1
      missedLetters = ''
      correctLetters = ' '
      gameIsDone = False
      secretWord = getRandomWord(random.choice([words, words1, words2, people, songAndArtist, InTheKitchen, TvShow]))
      if secretWord in words and gamesPlayed < 5:
          print "Hint: Around the House"
          hint = "Hint: Around the House"
      if secretWord in words1 and gamesPlayed < 5:
          print"Hint: Book Title"
          hint = "Hint: Book Title"
      if secretWord in words2 and gamesPlayed < 5:
          hint = "Hint: Food and Drink"
          print hint
      if secretWord in people and gamesPlayed < 5:
          hint = "Hint: People"
          print hint
      if secretWord in songAndArtist and gamesPlayed < 5:
          hint = "Hint: Song and Artist"
          print hint
      if secretWord in InTheKitchen and gamesPlayed < 5:
          hint = "Hint: In the Kitchen"
          print hint
      if secretWord in TvShow and gamesPlayed < 5:
          hint = "Hint: TV Show Title"
          print hint
      secretWord = secretWord.lower()
      player1Win = False
      player2Win = False
      player3Win = False
      spin1 = 0
      if gamesPlayed==5:
          if money4> money5 and money4>money6:
              print "PLayer 1 has won the game with $", money4
          if money5>money4 and money5>money6:
              print "Player 2 has won the game with $", money5
          if money6>money4 and money6>money5:
              print "Player 3 has won the game with $", money6
          break
