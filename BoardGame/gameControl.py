from BoardGame.user import user
import time

class gameControl(object):
    userDetails = []
    userEmails = []

    #checking if given mail id is present in userslist
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
            isMailPresent, index = self.isEmailPresent(email)
            if(isMailPresent == "True"):
                prevScore = self.userDetails[index].score
                self.userDetails[index].score = score
                print("score of {} is updated from {} to {}".format(self.userDetails[index].email, prevScore, self.userDetails[index].score))

            else:
                print("user of mailId:{} not present in the Board".format(email))
    
        else: 
            print("Score should be a non negative Integer")


    #print top n users with country if given
    def GET_TOP(self, n, country=""):
        countries = 0
        givenCountryUsers = []
        sortedByScoreCountry = []
        
        if(n <= len(self.userDetails) and n!=0): #n shud be less than lenth of userslist
            
            #if country is given
            if(country != ""):
                for i in range(len(self.userDetails)):      #filtering users with country
                    if(self.userDetails[i].country == country):
                        countries = countries+1
                        givenCountryUsers.append(self.userDetails[i])

               
                if(countries != 0):
                    sortedByScoreCountry = sorted(givenCountryUsers, key=lambda x: x.score, reverse=True)
                else:  #if given country users not present
                    print("No users from the given country")
            
            else: 
                sortedByScoreCountry = sorted(self.userDetails, key=lambda x: x.score, reverse=True)
            
            for i in range(len(sortedByScoreCountry)-1): #checking for same score and sorting by time
                if(sortedByScoreCountry[i].score == sortedByScoreCountry[i+1].score):
                    if(sortedByScoreCountry[i].recordedTime > sortedByScoreCountry[i+1].recordedTime):
                        temp= sortedByScoreCountry[i]
                        sortedByScoreCountry[i]=sortedByScoreCountry[i+1]
                        sortedByScoreCountry[i+1] = temp

            print("Top {} users are".format(n))
            i = 0            
            while(i<n):
                print("{}.{}".format(i+1,sortedByScoreCountry[i].email))
                i= i+1

        else:
            print("Enter a valid number: postive integer less than number of Users")

    
    #print users with givenscore
    #assumption:score should be non negative integer
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
                        del searchList[i]             #delete from list if score doesn't match
            elif(name is None):  #if name is not given
                for i in range(len(self.userDetails)):
                    if(self.userDetails[i].score == score):
                        isScorePresent = "True"
                        searchList.append(self.userDetails[i])


        if(country is not None):
            if(len(searchList) != 0):
                    
                    for i in range(len(searchList)):
                        if(searchList[i].country != country):
                            del searchList[i]         #delete from list if country doesn't match
                            
            elif(name is None and score is None): #if only country is given
                for i in range(len(self.userDetails)):
                    if(self.userDetails[i].country == country):
                        searchList.append(self.userDetails[i])
        
        print("Search result: found {}".format(len(searchList)))
        for i in range(len(searchList)):
            print(searchList[i].email)


    #printing users in the score range
    # assumption: lowscore and highscore values need to be non negative
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
           print("No matching name Found for {}".format(string))
        else:
            print("Users with matching {} are".format(string))
            for i in range(len(stringMatchUsers)):
                print(stringMatchUsers[i])
        
