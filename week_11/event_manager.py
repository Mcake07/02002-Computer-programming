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

class LimitedEventManager(EventManager):
    def __init__(self,registration_limit):
        self.guests = []
        self.registration_limit = registration_limit
        self.registered = 0
    def register(self,user):
        if not user in self.guests and self.registered < self.registration_limit:
            self.guests.append(user)
            self.registered += 1
            return 1==1
        else:
            return 1==2
    def deregister(self,user):
        if user in self.guests:
            self.guests.remove(user)
            self.registered -= 1
            return 1==1
        else:
            return 1==2