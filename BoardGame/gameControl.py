from BoardGame.user import user
import time

class gameControl(object):
    userDetails = []
    userEmails = []

    #checking if given mailid is present in userslist
    def isEmailPresent(self, mail):
        for i in range(len(self.userEmails)):
            if(self.userEmails[i] == mail):
                return "True",i
        return "false", None


    def UPSERT_USER(self, name, country, email):
        isMailPresent, index = self.isEmailPresent(email)
       
        if(isMailPresent == "false"):#adding the user
            recordedTime = time.localtime()
            users = user(name, country, email, time.strftime("%H:%M:%S",recordedTime))
            self.userDetails.append(users)
            self.userEmails.append(users.email)
            print("{} is added to the leaderboard".format(email))
        else:#updating the existing user
             self.userDetails[index].name = name
             self.userDetails[index].country = country
             print("{} is updated in the leaderboard".format(email))



    def UPSERT_SCORE(self, email, score):

        if(score >= 0):
            count = 0
            for i in range(len(self.userDetails)):
                if(self.userDetails[i].email == email):
                    count = count+1
                    prevScore = self.userDetails[i].score
                    self.userDetails[i].score = score
                    print("score of {} is updated from {} to {}".format(self.userDetails[i].email, prevScore, self.userDetails[i].score))
                    break

            if(count == 0):
                print("user of mailId:{} not present in the Board".format(email))
    
        else: 
            print("Score should be a non negative Integer")



    def GET_TOP(self, n, country=""):
        countries = 0
        givenCountryUsers = []
        sortedByScoreCountry = []
        
        if(n <= len(self.userDetails) and n!=0):
            
            if(country != ""):
                for i in range(len(self.userDetails)):
                    if(self.userDetails[i].country == country):
                        countries = countries+1
                        givenCountryUsers.append(self.userDetails[i])

               
                if(countries != 0):
                    sortedByScoreCountry = sorted(givenCountryUsers, key=lambda x: x.score, reverse=True)
                else:
                    print("No users from the given country")
            
            else:  
                sortedByScoreCountry = sorted(self.userDetails, key=lambda x: x.score, reverse=True)
            
            print("Top {} users are".format(n))
            i = 0
            while(i<n):
                print("{}.{}  ".format(i+1,sortedByScoreCountry[i].email))
                i= i+1

        else:
            print("Enter a valid number: postive integer less than number of Users")

    
    
    def GET_USERS_WITH_SCORE(self, givenScore):
        count = 0
        
        if(givenScore >= 0):
            for i in range(len(self.userDetails)):
                if(self.userDetails[i].score == givenScore):
                    count=1
                    print(self.userDetails[i].email)

            if(count == 0):
                print("No users on the Board with score: {}", givenScore)
        else:
            print("Score should be a non negative integer")



    def SEARCH(self, name, score, country):
        searchList = []
       
        if(name is not None):
            for i in range(len(self.userDetails)):
                if(self.userDetails[i].name == name):
                    searchList.append(self.userDetails[i])

        
        if(score is not None):
            if(len(searchList) != 0):
                for i in range(len(searchList)):
                    if(searchList[i].score != score):
                        del searchList[i]
            elif(name is None):
                for i in range(len(self.userDetails)):
                    if(self.userDetails[i].score == score):
                        isScorePresent = "True"
                        searchList.append(self.userDetails[i])


        if(country is not None):
            if(len(searchList) != 0):
                    print("inside country")
                    for i in range(len(searchList)):
                        if(searchList[i].country != country):
                            del searchList[i]
                            print("inside del country")
            elif(name is None and score is None):
                for i in range(len(self.userDetails)):
                    if(self.userDetails[i].country == country):
                        searchList.append(self.userDetails[i])
        
        print("Search result: found {}".format(len(searchList)))
        for i in range(len(searchList)):
            print(searchList[i].email)


    
    def GET_RANGE(self, lowScore, highScore):
        rangeList = []
        if(lowScore >= 0 and highScore >=0):
            for i in range(len(self.userDetails)):
                if(self.userDetails[i].score >= lowScore and self.userDetails[i].score <= highScore):
                    rangeList.append(self.userDetails[i].email)

            if(len(rangeList) == 0):
                print("No users found in given range: [{},{}]".format(lowScore, highScore))        
            
            print("Number of users in the Score range: [{},{}] are {}".format(lowScore, highScore, len(rangeList)))
            for i in range(len(rangeList)):
                print(rangeList[i])
        
        else:
             print("Scores should be non negative number")
        
    #looking for substring in name
    def SEARCH_NAME(self, string):
        stringMatchUsers = []
        for i in range(len(self.userDetails)):
            if string in self.userDetails[i].name:
                stringMatchUsers.append(self.userDetails[i].email)

        if(len(stringMatchUsers) == 0):
           print("No matching name Found")
        else:
            print("Users with matching {} are".format(string))
            for i in range(len(stringMatchUsers)):
                print(stringMatchUsers[i])
        
