class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        arr = str.split(" ")
        if len(pattern) != len(arr):
            return False
        if len(arr) == 1:
            return True
        ref = {}
        visited = set()
        count = 0
        
        while count < len(pattern):
            if pattern[count] in ref:
                if ref[pattern[count]] != arr[count]:
                    return False
            else:
                if arr[count] in visited:
                    return False
                ref[pattern[count]] = arr[count]
                visited.add(arr[count])
            count+=1
            
        return True
                