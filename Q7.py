import random
print("""
******Welcome To Hangman game******
Rules: 1- Enter your name:
       2- The random word generated and you must enter your guess word by word
       3- You have 7 chances to guess the word or you lose
""")

def hangman():
    words = """ant baboon badger bat bear beaver camel cat clam cobra cougar
       coyote crow deer dog donkey duck eagle fox frog goat goose hawk
       """.split()

    rndm_word=random.choice(words)

    name=input("Enter your name : ")

    print(f"Hey {name}, Good Luck in your game")
    guesses=""
    chances=7
    while chances >0:
        failed = 0
        for char in rndm_word:
            if char in guesses:
                print(char , end=" ")
                # chances+=1
            else:
                print("_")
                print("" )
                failed+=1

        if failed==0:
            print(f"""
            Congrats {name} \"/ you win, the word is {rndm_word}""")
            break
        
        print()
        guess=input("guess a character: ")
        guesses+=guess

        if guesses not in rndm_word:
            chances-=1
            print(f"Wrong answer , you have {chances} chances the word is {rndm_word}")

            if chances==0:
                print("You lose")

hangman()