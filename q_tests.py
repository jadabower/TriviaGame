from questionHandler import QuestionHandler

# Creates a question handler (with a question pool from the JSON file based on the options picked)
questionHand = QuestionHandler()
print(f"Question hand: {questionHand}")


questionPool = questionHand.createQuestionPool('K', 'Math')
question = questionHand.getQuestion(questionPool)
print(f"Question pool: {question}")

question = questionHand.getQuestion(questionPool)
print(f"Question pool: {question}")

for i in questionPool:
    question = questionHand.getQuestion(questionPool)
    print(f"Question pool: {question}")