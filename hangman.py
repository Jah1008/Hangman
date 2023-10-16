import random
import time

global game, color, uword, score
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def endTime():
    game=False
    print("Timer expired, game over!--------------------------------------------------------------------------")
    print(color.BOLD + 'GAME OVER!!' + color.END)
    print("Correct word is",uword)
    print("Total score:",score)
    end

game=True
print(color.BOLD + 'WELCOME TO THE HANGMAN GAME!! \n' + color.END)
print("TOPICS")

menu=[[["tiger","lion","monkey","alligator","walrus","seal","jaguar","giraffe"],["python","rhinocerous","leopard","cheetah","jackal","zebra"],["rabbit","dinosaurous","cat","dog","horse","wolf","bear","yak"]],[["hibiscus","ivy","lavender","hyacinth"],["jasmine","sunflower","marigold","honeysuckle","violet"],["lily","daisy","rose","daffodil","lotus","tulip"]],[["noodles","kulcha","chicken","brownies"],["fish","pulav","burger","fries"],["mutton","pulao","bread","pasta","prawns","taco"]],[["shinchan","oggyandcockroaches","doreamon","spiderman"],["pokemon","kiteratsu","benten","batman","ironman"],["mickeymouse","dora","chotabheem","littlekrishna"]],[["capsicum","brinjal","saffron"],["beetroot","carrot","cauliflower","turnip","radish"],["ladysfinger","cabbage","peas","beans"]],[["dragonfruit","muskmelon","avocado"],["watermelon","orange","pineapple","custardapple"],["pear","apple","grapes","mango","strawberry","kiwi"]]]
try:
    selectedmenu=int(input("1-ANIMALS, 2-FLOWERS, 3-FOOD, 4-CARTOONS, 5-VEGETABLES, 6-FRUITS\n"));
    if selectedmenu not in range(1,7):
         print("DEFAULT-TOPIC is ANIMALS")
         selectedmenu=1
    
except:
    print("ERROR!")
    print("DEFAULT-TOPIC is ANIMALS")
    selectedmenu=1
print(color.BOLD + "--------------------------------------------------------------------------------------------" + color.END)

print("DIFFICULTY LEVEL")
try:
    difficulty=int(input("1-HARD, 2-MEDIUM, 3-EASY\n"));
    if difficulty not in range(1,4):
         print("DEFAULT-DIFFICULTY is EASY")
         difficulty=3
        
except:
    print("ERROR!")
    print("DEFAULT-DIFFICULTY is EASY")
    difficulty=3
    

try:            
    uwords=menu[selectedmenu-1][difficulty-1]
except:
    print("DEFAULT-Topic is ANIMALS,Difficulty is EASY")
    uwords=menu[0][2]

print(color.BOLD + "--------------------------------------------------------------------------------------------" + color.END)

t=int(input("how long will you take to guess the word in seconds?:"))

uword=random.choice(uwords) 

count=0
guesses=7
score=100
wrong_letter=[]
l=[]


HANGMANPICS = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
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
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
    
for i in uword:
    l.append(i)
    

g=['__']*len(uword)

ready=input("are you ready?(press y):")
if ready in ["Y",'y']:
    start=time.time()
end=time.time()

while (game):
    while guesses :
        print(g)
        print(end-start);
        if(end-start>t):
           print("Time Up");
           break;
        if (g==l):
            print(color.BOLD + 'YOU GUESSED THE WORD!!' + color.END)
        else:
            choice=input("Did you guess the word? y/n: \n")
            if choice in ["y","Y"]:
                word=input("Guess a word: \n")
                word=word.lower()

                if word==uword:
                    print(color.BOLD + "--------------------------------------------------------------------------------------------" + color.END)
                    print(color.BOLD + 'YOU GUESSED THE WORD!!' + color.END)
                    print("Your score: ",score)
                    game=False
                    break

                else:
                    print("Wrong guess \n")
                    score=score-10

            else: 
                letter=input("\n guess a letter: ")
                letter=letter.lower()
                if letter not in uword:
                    print(color.BOLD + '\n TRY AGAIN!! \n' + color.END)
                    score=score-10
                    wrong_letter=wrong_letter+[letter]
                    print(HANGMANPICS[7-guesses])
                    guesses-=1
                    print("Number of mistakes allowed: ",guesses)
                    print("wrong letters","  ",wrong_letter)
                    print(color.BOLD + "--------------------------------------------------------------------------------------------" + color.END)

                for i in range(len(uword)):
                    if uword[i]==letter:
                        g[i]=letter
                        print(color.BOLD + "----------------------------------------------------------------------------------------" + color.END)
                    
                        
            end=time.time();
            if(g==l):
                  game=False;
                  print(color.BOLD + "--------------------------------------------------------------------------------------------" + color.END)
                  print("Guessed the word");
                  print("Total score:",score)
                  break;
                    

    if(end-start>t)|(not guesses):
        print(color.BOLD + "--------------------------------------------------------------------------------------------" + color.END)
        print(color.BOLD + 'GAME OVER!!' + color.END)
        print("Correct word is",uword)
        print("Total score:",score)
        break;
