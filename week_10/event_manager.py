class EventManager:
    def __init__(self):
        self.guests = []
    def register(self,user):
        if not user in self.guests:
            self.guests.append(user)
            return 1==1
        else:
            return 1==2
    def deregister(self,user):
        if user in self.guests:
            self.guests.remove(user)
            return 1==1
        else:
            return 1==2
    def get_num_registrations(self):
        return len(self.guests)