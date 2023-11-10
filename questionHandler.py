import json

class QuestionHandler():
    def __init__(self, grade, subject):
        f = open('questionsObject.json')
        data = json.load(f)
        self.grade = grade
        self.subject = subject
        self.questionIndex = 0
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
        elif self.grade == "2":
            if self.subject == "Math":
                self.questionPool = data["2"]["Math"]["questions"]
            elif self.subject == "Science":
                self.questionPool = data["2"]["Science"]["questions"]
            elif self.subject == "History":
                self.questionPool = data["2"]["History"]["questions"]
            else:
                self.questionPool = data["2"]["ELA"]["questions"]
        elif self.grade == "3":
            if self.subject == "Math":
                self.questionPool = data["3"]["Math"]["questions"]
            elif self.subject == "Science":
                self.questionPool = data["3"]["Science"]["questions"]
            elif self.subject == "History":
                self.questionPool = data["3"]["History"]["questions"]
            else:
                self.questionPool = data["3"]["ELA"]["questions"]
        self.numberOfQuestionsBase0 = len(self.questionPool) - 1
        f.close()