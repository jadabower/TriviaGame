class Question():

    def __init__(self, text, options, answer):
        self.text = text
        self.options = options
        self.answer = answer

    def checkAnswer(self, userAnswer):
        if userAnswer == self.answer:
            return True
        else:
            return False

    def getText(self):
        return self.text

       