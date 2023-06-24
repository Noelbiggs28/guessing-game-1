import random
class GuessingGame():
    def __init__(self):
        self.answer = random.randint(1,100)
        self.last_right = False

    def guess_number(self,number):
        if number > self.answer:
            self.last_right = False
            return 'high'
        elif number < self.answer:
            self.last_right = False
            return 'low'
        else:
            self.last_right = True
            return 'correct'
        
    def solved(self):
        return self.last_right
    
    def guess_letter(self, letter):
        if len(letter) > 1:
            print('guess one letter at a time')
            return
        if letter in self.correct_list or letter in self.incorrect_list:
            print('already guess the letter '+ letter)
            return
        for let in self.word:
            if let == letter:
                print('correct')
                self.last_right = True
                self.correct_list.append(letter)
                if len(self.correct_list) == self.correct_guess_for_win:
                    return print('you win the word was ' + self.word)
                return
        self.incorrect_list.append(letter)
        self.last_right = False
        print('incorrect guess')
        print(self.incorrect_list)


    
