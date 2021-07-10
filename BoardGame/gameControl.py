from BoardGame.user import user
import time

class gameControl(object):
    userDetails = []
    userEmails = []
    #User = user()

    def UPSERT_USER(self, name, country, email):
        isMailPresent = "false"
        for i in range(len(self.userEmails)):
            if(self.userEmails[i] == email):
                isMailPresent = "True"
                break

        try:
            if(isMailPresent == "false"):
                recordedTime = time.localtime()
                users = user(name, country, email, time.strftime("%H:%M:%S",recordedTime))
                self.userDetails.append(users)
                self.userEmails.append(users.email)
                print("{} is added to the leaderboard".format(name))
        
        except:
               print("user with EmailId: {} already present".format(email))
    
    def UPSERT_SCORE(self, email, score):
        count = 0
        for i in range(len(self.userDetails)):
           if(self.userDetails[i].email == email):
              count = count+1
              prevScore = self.userDetails[i].score
              self.userDetails[i].score = score
              print("score of {} is updated from {} to {}".format(self.userDetails[i].email, prevScore, self.userDetails[i].score))

        if(count == 0):
         print("user of mailId:{} not present in the Board".format(email))
               
    def GET_TOP(self, n, country=""):
        countries = 0
        givenCountryUsers = []
        sortedByScoreCountry = []
        print(n)
        print(len(self.userDetails))

        try:
            if(n <= len(self.userDetails)):
               
                if(country != ""):
                    for i in range(len(self.userDetails)):
                        if(self.userDetails[i].country == country):
                            countries = countries+1
                            givenCountryUsers.append(self.userDetails[i])

                    try:
                         if(countries != 0):
                            sortedByScoreCountry = sorted(givenCountryUsers, key=lambda x: x.score, reverse=True)
                    except: 
                          print("No users from the given country")


                
                else:  
                    sortedByScoreCountry = sorted(self.userDetails, key=lambda x: x.score, reverse=True)
               

                print("Top {} users are".format(n))
                i = 0
                while(i<n):
                  print("{}.{}  ".format(i+1,sortedByScoreCountry[i].email))
                  i= i+1

        except:
               print("Exceeds the number of users present in the board")

    
    
    def GET_USERS_WITH_SCORE(self, givenScore):
        count = 0
        try: 
            if(givenScore >= 0):
                for i in range(len(self.userDetails)):
                    if(self.userDetails[i].score == givenScore):
                        count=1
                        print(self.userDetails[i].email)

                if(count == 0):
                 print("No users on the Board with score: {}", givenScore)
        except:
            print("Score should be a non negative integer")