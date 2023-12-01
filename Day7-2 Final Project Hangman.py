stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
import random
print("--------WELCOME--TO--THE--COLOR--GUESS--GAME--------")
word_list = ["black", "white", "blue", "red", "green", "purple", "gray", "pink", "brown"]
choose_word = random.choice(word_list).lower()
answer_list = []
guess_time = 6
for letter in range(0,len(choose_word)):
    answer_list.append(" _ ")
# print(choose_word)
p = 0
# cheak_list[k] = " _ "
# for replay in range(0,len(choose_word)):
while not end_of_game:
    if p==7:
        print("---------YOU-LOSE-----------")
        break
    i = 0
    guess = str(input("Guess the letter-> "))
    for ans in range(0,len(choose_word)):
        if choose_word[i] == guess:
            answer_list[i] = guess
        i += 1 
    if guess not in choose_word:
        print(stages[guess_time])
        guess_time-=1
        p+=1
    temp_print = ""
    for inner in answer_list:
        temp_print += inner
    print(temp_print)
    if " _ " not in answer_list:
        end_of_game = True 
        print("----------YOU-WIN-----------")
    
    
answer = ""
for ineerletters in answer_list:
    answer += ineerletters
if end_of_game==True:
    print(f"Your Guess is {answer}")
