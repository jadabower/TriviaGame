import pygame
import random
import json

class QuestionHandler():
    def __init__(self, grade, subject):
        f = open('questionsObject.json')
        data = json.load(f)
        self.grade = grade
        self.subject = subject
        if self.grade == "K":
            if self.subject == "Math":
                self.questionPool = data["K"]["Math"]["questions"]
            elif self.subject == "Science":
                self.questionPool = data["K"]["Science"]["questions"]
            elif self.subject == "History":
                self.questionPool = data["K"]["History"]["questions"]
            else:
                self.questionPool = data["K"]["ELA"]["questions"]
        elif self.grade == "1":
            if self.subject == "Math":
                self.questionPool = data["1"]["Math"]["questions"]
            elif self.subject == "Science":
                self.questionPool = data["1"]["Science"]["questions"]
            elif self.subject == "History":
                self.questionPool = data["1"]["History"]["questions"]
            else:
                self.questionPool = data["1"]["ELA"]["questions"]
        f.close()

    def getRandomQuestion(self):
        index = random.randint(0, len(self.questionPool) - 1)
        print(self.questionPool[index])