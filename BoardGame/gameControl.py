from BoardGame.user import user
import time

class gameControl(object):
    userDetails = []
    userEmails = []
    #User = user()

    def UPSERT_USER(self, name, country, email):
        recordedTime = time.localtime()
        users = user(name, country, email, time.strftime("%H:%M:%S",recordedTime))
        self.userDetails.append(users)
        self.userEmails.append(users.email)
        print(users.email)
        print("{} is added to the leaderboard".format(name))
    
    def UPSERT_SCORE(self, email, score):
        count =0
        for i in range(len(self.userDetails)):
           if(self.userDetails[i].email == email):
             count=1
             self.userDetails[i].score = score

        if(count == 0):
         print("user of mailId:{} not present in the Board".format(email))
               
    def GET_TOP(self, n, country=""):
        i =0
        givenCountryUsers = []

        try:
            if(n <= len(self.userDetails)):
                if(country != ""):
                    for i in range(len(self.userDetails)):
                        if(self.userDetails[i].country == country):
                            givenCountryUsers.append(self.userDetails[i])

                if(len(givenCountryUsers) == 0 and country == ""):
                   sortedByScore = sorted(self.userDetails, key='score')
                else: sortedByScore = sorted(givenCountryUsers, key='score')

                print("Top {} users are".format(n))
                while(i<n):
                  print("{}.{}  ".format(i+1,sortedByScore[i].email))
                  i= i+1

        except:
               print("Exceeds the number of users present in the board")

    def GET_USERS_WITH_SCORE(self, givenScore):
        count =0
        for i in range(len(self.userDetails)):
           if(self.userDetails[i].score == givenScore):
             count=1
             print(self.userDetails[i].email)

        if(count == 0):
         print("No users on the Board with score: {}", givenScore)