# Given a string, determine if it has the word "ok".

# Setup
def searchOk(word):
    for i in range(len(word)-1):
        if word[i] == 'o' and word[i+1] == 'k':
            return True
    else:
        return False


# Test
assert(searchOk('Hellok')==True)
assert(searchOk('Hello')==False)
assert(searchOk('')==False)
