#Leet code - unique morse code words

class Solution():
    def uniqueMorseRepresentations(self,words):
        CODE = {'a': '.-','b': '-...',   'c': '-.-.', 
        'd': '-..',    'e': '.',      'f': '..-.',
        'g': '--.',    'h': '....',   'i': '..',
        'j': '.---',   'k': '-.-',    'l': '.-..',
        'm': '--',     'n': '-.',     'o': '---',
        'p': '.--.',   'q': '--.-',   'r': '.-.',
     	's': '...',    't': '-',      'u': '..-',
        'v': '...-',   'w': '.--',    'x': '-..-',
        'y': '-.--',   'z': '--..',
        
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }
        
        final = set()
        for word in words:
            tmp = ""
            for i in word:
                tmp+=CODE[i]
            final.add(tmp)
        
        return len(final)


obj = Solution()
words = ["gin", "zen", "gig", "msg","trt"]
obj.uniqueMorseRepresentations(words)