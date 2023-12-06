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
    
    def getA(self):
        return self.options['A']
    def getB(self):
        return self.options['B']
    def getC(self):
        return self.options['C']
    def getD(self):
        return self.options['D']
    
    def getAnswer(self):
        return self.answer

       