class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        maxtime=releaseTimes[0]
        slowest=keysPressed[0]
        for i in range(1,len(keysPressed)):
            duration=releaseTimes[i]-releaseTimes[i-1]
            if duration>maxtime or(duration==maxtime and keysPressed[i]>slowest):
                maxtime=duration
                slowest=keysPressed[i]
        return slowest        
        
        