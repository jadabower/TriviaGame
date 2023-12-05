from questionHandler import QuestionHandler

# Creates a question handler (with a question pool from the JSON file based on the options picked)
questionHand = QuestionHandler()
print(f"Question hand: {questionHand}")


kMathQP = questionHand.createQuestionPool('K', 'Math')

print(f"Question pool: {kMathQP.getQuestion()}")

kMathQP.questionPool.count()