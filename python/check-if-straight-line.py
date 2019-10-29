class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        if len(coordinates) <= 1:
            return False
        
        tmp = 0
        i = 0
        while i + 1 < len(coordinates):
            try:
                if i == 0:
                    tmp = (coordinates[i+1][1] - coordinates[i][1])/(coordinates[i+1][0] - coordinates[i][0])
                else:
                    if tmp != (coordinates[i+1][1] - coordinates[i][1])/(coordinates[i+1][0] - coordinates[i][0]):
                        return False
            except:
                return False
            i+=1
            
        return True