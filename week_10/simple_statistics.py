class SimpleStatistics:
    def __init__(self, samples):
        self.samples = samples
    def get_mean(self):
        return sum(self.samples) / len(self.samples)
    def get_standard_deviation(self):
        thing = 0
        for i in range(len(self.samples)):
            thing += (self.samples[i] - self.get_mean()) ** 2
        return (1 / (len(self.samples) - 1) * thing ) ** (1/2)
    def one_sample_ttest(self, mu0): 
        return abs((self.get_mean() - mu0) / ((self.get_standard_deviation() / (len(self.samples) ** (1/2))))) >= 1.96