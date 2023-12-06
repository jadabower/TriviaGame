import json
from question import Question

class QuestionHandler():
    def __init__(self):
        f = open('questionsObject.json')
        self.data = json.load(f)
        f.close()
        self.questionPool = []
        self.points = 0

    def createQuestionPool(self, grade, subject):
        # Creates a question pool (a list of Question objects)
        questionPoolArray = self.data[grade][subject]["questions"]
        for q in questionPoolArray:
            text = q["question"]
            options = q["options"]
            correctAnswer = q["correctAnswer"]

            currentQ = Question(text, options, correctAnswer)
            # print(f"{q}")
            # print(f"{currentQ.__dict__}")
            # print(f"{currentQ.getText()}")
            self.questionPool.append(currentQ)
        # return questionPool

    def getPoints(self):
        return self.points

    def getQuestion(self):
        if len(self.questionPool) == 0:
            print('help')
        else:
            return self.questionPool[0]

    def checkAnswer(self, answer):
        currentQuestion = self.questionPool[0]
        if currentQuestion.checkAnswer(answer):
            print("correct")
            self.points += 10
            self.questionPool.pop(0)
            return True
        else:
            print("incorrect")
            self.points -= 5
            self.questionPool.append(currentQuestion)
            self.questionPool.pop(0)
            return False