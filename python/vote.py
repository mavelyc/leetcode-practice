import collections
class Poll:
    def __init__(self):
        self.time = 0
        self.candidates = collections.defaultdict(int)
        self.timestamp = collections.defaultdict(list)

    def vote(self, vote):
        self.time+=1
        self.candidates[vote]+=1
        self.timestamp[self.time] = sorted(self.candidates.items(), key=lambda x: x[1], reverse=True)
    
    def checkPolls(self, time):
        if time > self.time:
            print( "Invalid input for time" )
        print (self.timestamp[time]) 

test = Poll()
test.vote("C")
test.vote("C")
test.vote("D")
test.vote("C")
test.vote("M")

test.checkPolls(4)