class MultipleChoice:
    def __init__(self, num_questions):
        self.num_questions = num_questions
        self.answers = None
    def record_answer(self,question_num,answer):
        self.answers = {}
        self.answers[question_num] = answer
    def get_answer(self,question_num):
        return self.answers[question_num]
    def completion_percentage(self):
        return len(self.answers) / self.num_questions
    
class MultipleChoiceRestricted(MultipleChoice):
    def __init__(self,num_questions,attempts):
        super.__init__(self,num_questions)
        self.attempts = attempts
        self.num_attempts = 0
    def record_answer(self,question_num,answer):
        if self.num_attempts <= self.attempts:
            super().record_answer(self,question_num,answer)
            self.num_attempts += 1