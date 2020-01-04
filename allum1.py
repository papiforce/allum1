import random

def initialisation():
	# initialise les allumettes & le check tour
	global allumettes
	global tour
	global nbr_allumettes
	nbr_allumettes = 11
	allumettes = "|" * nbr_allumettes
	tour = 0
	print(allumettes + " (" + str(nbr_allumettes) + ")")

def player():
	# coup du joueur ainsi que son tour
	global allumettes
	global tour
	global nbr_allumettes
	if nbr_allumettes == 1:
		return
	remove = input("Your turn \nMatches: ")
	while remove < 1 or remove > 3 or isinstance(remove, str) == True:
		remove = input("Error: invalid input \nMatches: ")
	allumettes = allumettes[:-remove]
	nbr_allumettes -= remove
	print("Player removed " + str(remove) + " match(es)\n" + allumettes + " (" + str(nbr_allumettes) + ")")
	tour = 1

def ai():
	# coup de l'ai ainsi que son tour
	global allumettes
	global tour
	global nbr_allumettes
	print("AI's turn...")
	if len(allumettes) > 8:
		remove_ai = random.choice([1,2,3])
		allumettes = allumettes[:-remove_ai]
		nbr_allumettes -= remove_ai
		print("AI removed " + str(remove_ai) + " match(es)\n" + allumettes + " (" + str(nbr_allumettes) + ")")
	elif (len(allumettes) == 8):
		allumettes = allumettes[:-3]
		nbr_allumettes -= 3
		print("AI removed 3 match(es)\n" + allumettes + " (" + str(nbr_allumettes) + ")")
	elif (len(allumettes) == 7):
		allumettes = allumettes[:-2]
		nbr_allumettes -= 2
		print("AI removed 2 match(es)\n" + allumettes + " (" + str(nbr_allumettes) + ")")
	elif (len(allumettes) == 6):
		allumettes = allumettes[:-1]
		nbr_allumettes -= 1
		print("AI removed 1 match(es)\n" + allumettes + " (" + str(nbr_allumettes) + ")")
	elif (len(allumettes) == 5):
		allumettes = allumettes[:-1]
		nbr_allumettes -= 1
		print("AI removed 1 match(es)\n" + allumettes + " (" + str(nbr_allumettes) + ")")
		tour = 0
	elif (len(allumettes) == 4):
		allumettes = allumettes[:-3]
		nbr_allumettes -= 3
		print("AI removed 3 match(es)\n" + allumettes + " (" + str(nbr_allumettes) + ")")
		tour = 0
	elif (len(allumettes) == 3):
		allumettes = allumettes[:-2]
		nbr_allumettes -= 2
		print("AI removed 2 match(es)\n" + allumettes + " (" + str(nbr_allumettes) + ")")
		tour = 0
	elif (len(allumettes) == 2):
		allumettes = allumettes[:-1]
		nbr_allumettes -= 1
		print("AI removed 1 match(es)\n" + allumettes + " (" + str(nbr_allumettes) + ")")
		tour = 0
	elif (len(allumettes) == 1):
		nbr_allumettes -= 1
		print("AI removed 1 match(es) (" + str(nbr_allumettes) + ")")
		tour = 0

def replay_game():
	# permet de relancer une partie
	global replay
	global continuer
	if continuer == "no":
		replay = False
	else:
		replay = True

def total_game():
	# permet de compter le nombre total de parties
	global game
	game += 1
	print("\nTotal number of games played: " + str(game))

def total_ai():
	# permet de compter le nombre de parties gagnees par l'AI
	global win_ai
	win_ai += 1
	print("Total number of games won by AI: " + str(win_ai) + "\n")

def total_player():
	# permet de compter le nombre de partie gagnees par le joueur
	global win_player
	win_player += 1
	print("Total number of games won by Player: " + str(win_player) + "\n")

def start_turn():
	# permet au joueur de choisir si l'AI debute la partie
	global answer
	if answer == "me":
		player()
		ai()
	else:
		ai()
		player()

global replay
global game
global win_ai
global win_player
game = 0
win_ai = 0
win_player = 0
replay = True
while replay:
	global answer
	global continuer
	answer = raw_input("Who starts the game? me/ai\n")
	initialisation()
	while len(allumettes) > 1:
		start_turn()
	if tour == 1:
		print("You win!")
		total_game()
		total_player()
		print("Total number of games won by AI: " + str(win_ai) + "\n")
		continuer = raw_input("Do you want to replay? yes/no\n")
		replay_game()
	else:
		print("You loose!")
		total_game()
		print("Total number of games won by Player: " + str(win_player))
		total_ai()
		continuer = raw_input("Do you want to replay? yes/no\n")
		replay_game()
