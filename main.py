import random

HANGMAN_PICS = [''' 
       +---+
           |
           |
           |
          ===''', '''
       +---+
       O   |
           |
           |
          ===''', '''
       +---+
       O   |
       |   |
           |
          ===''', '''
       +---+
       O   |
      /|   |
           |
          ===''', '''
       +---+
       O   |
      /|\  |
           |
          ===''', '''
       +---+
       O   |
      /|\  |
      /    |
          ===''', '''
       +---+
       O   |
      /|\  |
      / \  |
          ===''']

words = """
ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow 
deer dog donkey duck eagle ferret fox frog goat goose hawk
lion lizard llama mole monkey moose mouse mule newt otter owl panda
parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
skunk sloth snake spider stork swan tiger toad trout turkey turtle
weasel whale wolf wombat zebra""".split()

name= input('Please Enter your name: \n')

print(f"Welcome to hangman game, {name}")

print('---------------------')
print('')
print('Try to guess the word in less than 7 attempts:')
word = random.choice(words)
print(word)
validletters= 'abcdefghijklmnopkrstuvwxyz'
uword = ['-' for i in word]
num = 0
att = 7
guessed = []
while '-' in uword:
    print(''.join(uword))
    guess = input('Guess a letter: \n').lower()
    if guess == '' or guess not in validletters :
        print('This letter is not a valid guess, try again')
        continue
    elif guess in word and guess not in guessed:
        index=word.index(guess)
        uword[index] = guess
        guessed.append(guess)
        if '-' not in uword:
            print('Congratulations, you did it')
            break

    elif guess in word and guess in guessed:
        index=word.index(guess)
        sindex=word.index(guess, index+1)
        uword[sindex] = guess
        if '-' not in uword:
            print('Congratulations, you did it')
            break

    else:
        att -= 1
        print(f"You have {att} left")
        if att == 0:
            print('You ran out of attempts, Game Over')
            break
        try:
            print(HANGMAN_PICS[num])
            num+=1
        except IndexError:
            print('Game Over')
            break

