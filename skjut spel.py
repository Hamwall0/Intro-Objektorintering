import random as ran
class Player():
    def __init__(self,life):
        self.lifes = life
        self.score = 0
      

    def ink_score(self):
        self.score += 1
    def ink_life(self):
        self.lifes += -1
    def fire(self):
        while True:
            input("skjut med enter")
            i = ran.randint(1,5) 
            if i in {1,2,3}:
                self.ink_score()
                print("träff!")
            else:
                self.ink_life()
                print("aj")
                print(self.lifes)
                if self.lifes == 0:
                    print("game over")
                    print(self.score)
                    break
        
a_player = Player(3)
a_player.fire()
