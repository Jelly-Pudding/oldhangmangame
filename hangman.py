import random

random_number = random.randrange(0, 22)

if random_number == 0:
	hidden_string = "boy"
if random_number == 1:
	hidden_string = "jazz"
if random_number == 2:
	hidden_string = "music"
if random_number == 3:
        hidden_string = "story"
if random_number == 4:
        hidden_string = "french toast"
if random_number == 5:
        hidden_string = "azure dream"
if random_number == 6:
        hidden_string = "singer"
if random_number == 7:
        hidden_string = "heaven"
if random_number == 8:
        hidden_string = "rap god"
if random_number == 9:
        hidden_string = "sincere"
if random_number == 10:
        hidden_string = "king"
if random_number == 11:
        hidden_string = "first"
if random_number == 12:
        hidden_string = "cheater"
if random_number == 13:
        hidden_string = "noooooooooo"
if random_number == 14:
        hidden_string = "picnic"
if random_number == 15:
        hidden_string = "lettters"
if random_number == 16:
        hidden_string = "sleeper"
if random_number == 17:
        hidden_string = "deathly gaze"
if random_number == 18:
        hidden_string = "crying man"
if random_number == 19:
        hidden_string = "picture"
if random_number == 20:
        hidden_string = "shadow"
if random_number == 21:
        hidden_string = "aphrodite"


correct_guesses = []
count = 0
tries = 0

for i in range(25):
	tries += 1
	letterguess = input("Guess a letter: ")
	if count == 0:
		if letterguess in hidden_string:
			count += 1
			for letter in range(len(hidden_string)):
				if hidden_string[letter] == letterguess:
					correct_guesses.append(hidden_string[letter])
				elif hidden_string[letter] != letterguess:
					correct_guesses.append(" ")
			print(correct_guesses)
	elif count >= 1:
		for letter in range(len(hidden_string)):
			if hidden_string[letter] == letterguess:
				correct_guesses[letter] = hidden_string[letter]
		print(correct_guesses)
	if "".join(correct_guesses) == hidden_string:
		print("Congratulations, you did it! The word was {word}! This took you {tries} guesses!".format(word=hidden_string, tries=tries))
		break
if "".join(correct_guesses) != hidden_string:
	print("I'm so sorry. You had {tries} guesses but could not solve it. The word was {word}!".format(tries=tries, word=hidden_string))		
					
		

















