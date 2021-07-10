# This is the base class for initalising a new user

class user(object):
     
     def __init__(self, name, country, email, recordedTime):
        self.name = name
        self.country = country
        self.email = email
        self.recordedTime = recordedTime
        self.score = 0
        
       
