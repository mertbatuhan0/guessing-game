import random 

class User:
    def __init__(self, name):
        self.name = name 
        self.attempt = 0    
        
    def make_guess(self):
        guess_number = int(input(f"{self.name}, please enter a number: "))
        self.attempt += 1 
        return guess_number


class Number:
    def __init__(self):
        self.max_val = 100
        self.min_val = 1
        self.random_num = random.randint(self.min_val, self.max_val)


class Result:
    @staticmethod
    def evaluate(guess, secret):
        if guess < secret:
            return "Too low!"
        elif guess > secret:
            return "Too high!"
        else:
            return "Correct!"


class Game:
    def __init__(self):
        self.user = User(input("What is your name? "))
        self.number = Number()
        self.is_working = True

    def start(self):
        print(f"Good luck {self.user.name}!")
        while self.is_working:
            guess = self.user.make_guess()
            feedback = Result.evaluate(guess, self.number.random_num)
            
            print(feedback)
         
            if feedback == "Correct!": 
                print(f"Done! It took you {self.user.attempt} tries.")
                self.is_working = False

if __name__ == "__main__":
    game = Game()
    game.start()








        





