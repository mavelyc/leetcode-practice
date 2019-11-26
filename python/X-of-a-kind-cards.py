from functools import reduce
from fractions import gcd
import collections
class Solution(object):
    def hasGroupsSizeX(self, deck):
        vals = collections.Counter(deck).values()
        return reduce(gcd, vals) >= 2