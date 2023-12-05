from questionHandler import QuestionHandler

# Creates a question handler (with a question pool from the JSON file based on the options picked)
questionHand = QuestionHandler()
print(f"Question hand: {questionHand}")


questionHand.createQuestionPool('K', 'Math')
print(questionHand.points)

question1 = questionHand.getQuestion()
print(f"Question 1: {question1.getText()}")
# print(f"Question pool: {questionHand.getQuestion().getText()}")

questionHand.checkAnswer('B')
