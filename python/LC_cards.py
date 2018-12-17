#Leet code - reveal cards
#Python3

class Solution():
    def deckRevealedIncreasing(self, deck):
        final = []
        up = deck.copy()
        down = deck.copy()
        up.sort()
        down.sort(reverse=True)
        t = int(len(down)/2)
        for i in range(t):
            final.append(down[i])
            final.append(up[i])
        print (final)






obj = Solution()
dec = [3,2,5,7,12,15,11,10]
obj.deckRevealedIncreasing(dec)
        