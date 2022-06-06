letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
#creates a dict with letters as key and points as value.
letter_to_points = {key:value for key, value in zip(letters, points)}
letter_to_points[" "] = 0 #adds new element to dict.

#Func that can take a number and return how many points its worth.
def scored_word(word):
  point_total = 0
  for letter in word:
    if letter in letter_to_points:
      point_total += letter_to_points.get(letter)
    else:
      point_total += 0
  return point_total

brownie_points = scored_word("BROWNIE") #testing scored_word

#Creating a dictionary that map players to a list of words they have played.
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points = {} #Empty dict.

def update_point_totals(dict):                 
  for player, words in dict.items():           #updates the the given dict and adds the points to player_to_points as scoreboard.
    player_points = 0
    for word in words:
      player_points += scored_word(word)
    player_to_points[player] = player_points

update_point_totals(player_to_words)

def play_word(player, word):
  # Implementing a func that can take in a player and a word, add it to the list of words they've played.
  if player in player_to_words:
    player_to_words[player].append(word)

play_word("player1", "BABY")


print(player_to_points)