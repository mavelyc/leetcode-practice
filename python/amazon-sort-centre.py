import collections
class Solution:
    def __init__(self,truckSpace, packagesSpace):
        self.main(truckSpace, packagesSpace)
        
    def main(self, truckSpace, packagesSpace):
        paths = collections.defaultdict(int)
        final = []
        for index, item in enumerate(packagesSpace):
            print(item, paths)
            print(truckSpace-item-30)
            if truckSpace-item-30 in paths:
                print("yes")
                final.append([paths[truckSpace-item-30],index])
            paths[item] = index
        
        print(final)

test = Solution(90, [1,10,25,35,60])