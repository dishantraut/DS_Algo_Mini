a = "I love python and python programming"
b = "There is a dog"

def FW (sen,w):
    """ Find word and index """
    if w in sen.split():
        return sen.find(w)
    else:
        return "Word Not Found In Given Sentance"

print(FW (a,"python"))
