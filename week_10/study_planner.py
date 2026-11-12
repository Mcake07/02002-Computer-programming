class StudyPlanner:
    def __init__(self,blocks, points):
        self.registered_courses = {}
        for block in blocks:
            self.registered_courses[block] = []
        self.points_left = {}
        for i in range(len(blocks)):
            self.points_left[blocks[i]] = points[i]
    def add_course(self,name,block,ects):
        if self.points_left[block] >= ects:
            self.registered_courses[block].append(name)
            self.points_left[block] -= ects
            return 1
        else:
            return -1
    def print_courses(self):
        print('---------------')
        for block in self.registered_courses:
            print(f'BLOCK {block.upper()}')
            print(f'    Points left: {self.points_left[block]}')
            print(f'    Courses:')
            for course in self.registered_courses[block]:
                print(f'        {course}')
        print('---------------')

blocks = ['foundations', 'directions', 'projects', 'electives']
points = [55, 55, 25, 45]
planner = StudyPlanner(blocks, points)
planner.print_courses()
planner.add_course('Programming', 'foundations', 5)
planner.print_courses()
planner.add_course('Mathematics 1a', 'foundations', 10)
planner.add_course('Mathematics 1b', 'foundations', 10)
planner.add_course('Signals and systems', 'directions', 5)
planner.add_course('Optics and photonics', 'directions', 5)
planner.add_course('BSc project', 'projects', 15)
planner.add_course('Prototyping', 'projects', 10)
planner.add_course('Acoustics and noise', 'electives', 5)
planner.print_courses()