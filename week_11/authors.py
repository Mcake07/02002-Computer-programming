class Authors:
    def __init__(self, first_name, last_name):
        self.author_list = [first_name + ' ' + last_name]
    def add_author(self, first_name, last_name):
        self.author_list.append(first_name + ' ' + last_name)
    def get_authors(self):
        string = ''
        for i in range(len(self.author_list)):
            string += self.author_list[i]
    def __str__(self):
        name = []
        string = ''
        last_names = []
        if len(self.author_list) < 1: return 'ERROR'
        elif len(self.author_list) == 1:
            name = (self.author_list).split()
            return name[-1]
        elif len(self.author_list) == 2:
            for i in range(2):
                name = (self.author_list[i]).split()
                last_names.append(name[-1])
            return last_names[0] + ' and ' + last_names[1]
        else:
            name = (self.author_list[0]).split()
            last_name = name[-1]
            return last_name + 'et al.'