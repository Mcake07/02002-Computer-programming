class ScoreTracker:
    def __init__(self):
        self.score_1, self.score_2 = 0,0
        self.name_1, self.name_2 = '',''
    def include(self,score,name):
        if score > self.score_1: self.score_1, self.name_1 = score,name
        elif self.score_1 > score > self.score_2: self.score_2, self.name_2 = score,name
    def __str__(self):
        return f'HIGH SCORES:\nWinner:      {self.score_1} {self.name_1}\nRunner up:      {self.score_2} {self.name_2}'
    def __add__(self, other):
        combined = ScoreTracker()
        combined.include(self.score_1, self.name_1)
        combined.include(self.score_2,self.name_2)
        combined.include(other.score_1, other.name_1)
        combined.include(other.score_2, other.name_2)
        return combined
class UniqueScoreTracker(ScoreTracker):
    def include(self, score, name):
        if score > self.score_1:
            if name == self.name_1:
                self.score_1 = score
            else: 
                self.score_2, self.name_2 = self.score_1, self.name_1
                self.score_1, self.name_1 = score, name
        elif score >= self.score_2:
            if name != self.score_1:
                self.score_2, self.name_2 = score, name

wednesday_scores = ScoreTracker()
wednesday_scores.include(105, 'Alice')
wednesday_scores.include(98, 'Bob')
print('\nWEDNESDAY', wednesday_scores)

thursday_scores = ScoreTracker()
thursday_scores.include(102, 'Charlie')
thursday_scores.include(99, 'Alice')
print('\nTHURSDAY', thursday_scores)

combined_scores = wednesday_scores + thursday_scores
print('\nCOMBINED', combined_scores)