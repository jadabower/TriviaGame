import json

class QuestionHandler():
    def __init__(self):
        f = open('questionsObject.json')
        self.data = json.load(f)
        f.close()

    def createQuestionPool(self, grade, subject):
        questionPool = self.data[grade][subject]["questions"]
        return questionPool
        

    def getQuestion(self, questionPool):
        return questionPool.pop()

    # def checkAnswer(self, answer):