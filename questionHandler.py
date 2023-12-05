import json
import Question

class QuestionHandler():
    def __init__(self):
        f = open('questionsObject.json')
        self.data = json.load(f)
        f.close()
        self.quesstionPool = []
        self.points = 0

    def createQuestionPool(self, grade, subject):
        # Creates a question pool (a list of Question objects)
        questionPoolArray = self.data[grade][subject]["questions"]
        for question in questionPoolArray:
            text = question["question"]
            options = question["options"]
            correctAnswer = question["correctAnswer"]

            question = Question.Question(text, options, correctAnswer)
            self.quesstionPool.append(question)
        # return questionPool

    def getQuestion(self):
        if self.quesstionPool.count == 0:
            return False
        else:
            self.questionPool[0]

    def checkAnswer(self, answer):
        currentQuestion = self.questionPool[0]
        if currentQuestion.checkAnswer(answer):
            self.points += 10
            self.questionPool.pop(0)
        else:
            self.points -= 5
            self.quesstionPool.append(currentQuestion)
            self.quesstionPool.pop(0)

        

    # def points(self, correct):