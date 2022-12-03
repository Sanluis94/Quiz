from quiz import Quiz
from questions import questions

quiz = Quiz(0)

for i in range(len(questions)):
    question = questions[i]
    quiz.update(question['question'],question['A'],question['B'],question['C'],question['D'],question['correct'])