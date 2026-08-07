import random
def game():
    print("you are palying the game")
    score=random.randint(1,62)
#randint gives number betwen the range
    print(f"your score{score}")
    with open("highscore.txt")as f:
        highscore=f.read()  #gives in form of str
        if(highscore!=""):
            highscore=int(highscore)  #typecasting
        else:
            highscore=0
    print(f"your score{score}")
    if(score>highscore):
        with open("highscore.txt","w")as f:
            f.write(str(score))

    return score
game()
