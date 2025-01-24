import random
#FASE1
#lista di parole random
#keyword scelta tra le parole random con choice
#chiedo l'input al giocatore
#verifico l'input
#FASE2 
#Se la lettera è corretta inserirla in guessed letters
#Rimpiazzo ogni lettera con un underscore così da sapere la lunghezza della parola

def main():
    words = ["random", "spirale", "moto", "joker", "pokerev"]
    keyword = random.choice(words)
    display_word = []
    for l in keyword:
        display_word.append("_")
    print(display_word)

    guessing(keyword, display_word)




def guessing(word, display):
    complete = False
    correct_guess = False
    while complete == False:
        
        guess = input("Input your guess here: ").lower()
        if len(guess) > 1:
            print("Input only one letter at a time.")
            continue
        for letter in range(len(word)):
            
            if guess == word[letter]:
                correct_guess = True
                display[letter] = guess
                print(display)
                if ''.join(display) == word:
                    print(f"Congratulations, you guessed the word {word.upper()}")
                    complete = True
                    break
        if not correct_guess:
            print("No corrispondence found, try again.")
            print(display)
            
                        
        
main()


