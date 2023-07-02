import random
import hangam_stages
import word_file
#word_list=['apple','beautiful','potato']
lives=6
choosen_word=random.choice(word_file.words)
print(choosen_word)     #Task 1 :- generating a random word from the given word list
display=[]
'''
for letter in choosen_word:
    display+='_'
print(display) '''         #Task 2 :- genarting blank spaces fr the randomly choosen word which will be displayed to second player
for i in range(len(choosen_word)): # Another way to generate blanks
    display+='_'
print(display)
game_over=False
while not game_over:
     guessed_letter=input("Guess a letter:").lower()
     for position in range(len(choosen_word)):  # 0 1 2 3 4 
         letter=choosen_word[position]
         if letter==guessed_letter:
             display[position]=guessed_letter
     print(display)
     if guessed_letter not in choosen_word:
             lives-=1
             if lives==0:
                  game_over=True
                  print("You Lose !!")
     if '_' not in display:
          game_over=True
          print("You Win!!")
     print(hangam_stages.stages[lives])