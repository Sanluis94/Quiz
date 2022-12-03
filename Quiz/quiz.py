class Quiz:
    def __init__(self,points):
        self.points = points

    def game(self,question,A,B,C,D,correct):

        print(question)
        print(f"A-{A}")
        print(f"B-{B}")
        print(f"C-{C}")
        print(f"D-{D}")

        self.answer = input("What's  your answer (A, B, C or D):\n").upper()

        if self.answer == correct:
            print("You are awesome, you got it right!")
            self.points += 1
            print("Points:",self.points)
        else:
            print(f"It's incorrect, the right answer should be: {correct}")

    def update(self,question,A,B,C,D,correct):

        self.game(question,A,B,C,D,correct)