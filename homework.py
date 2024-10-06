import random

WORDS = ("banana", "school", "keyboard", "videogame", "television",
         "mathemathic")
word = random.choice(WORDS)
correct_word = word

shuffled_word = ""

while word:
  position = random.randrange(len(word))
  shuffled_word = shuffled_word + word[position]
  word = word[:position] + word[(position + 1):]

print("Let's play the word shuffle game!")

print("The shuffled word is:", shuffled_word)

guess = input("Your guess: ")
guess = guess.lower()
while (guess != correct_word) and (guess != ""):
  print("Sorry, wrong answer!")
  guess = input("Your guess: ")
  guess = guess.lower()

if guess == correct_word:
  print("Nice job, you got it!")

print("Thanks for your participation.")
