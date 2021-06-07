import hangman_art
import hangman_words
import random


word_list=hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
stages=hangman_art.stages
end_of_game = False
lives = 6
repeat_flag=''


print(hangman_art.logo)



display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    repeat_flag=False

   
    if guess in display:
      print(f"You already entered {guess}")
      repeat_flag=True
      

    
    for position in range(word_length):
        letter = chosen_word[position]
       
        if letter == guess and repeat_flag!=True:
            print(f"you enter the correct letter {guess}")
            display[position] = letter

    print(f"{' '.join(display)}")
    
    if guess not in chosen_word:
        
        print(f"the letter you entered {guess} is not in the word , You lose a life")
        lives -= 1
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The correct answer was {chosen_word} better luck next time")

    

    
    if "_" not in display:
        end_of_game = True
        print("You win.")

 
    
