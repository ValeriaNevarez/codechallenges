#Given a needle and a haystack (array) return true if the needle is in the haystack.

#Solution
def searchHaystack(needle,haystack):
    for i in range(len(haystack)):
        if haystack[i] == needle:
            return True
    else:
        return False 

#Test
assert(searchHaystack(5,[2,3,4,5,6]) == True)
assert(searchHaystack(1,[2,3,4]) == False)
assert(searchHaystack(0,[])== False)
