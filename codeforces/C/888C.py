def getCharacters(s):
    res = {}
    for l in s:
        res[l] = 0
    return res

def getLetterSubsPresence(s, k, characters):
    window = [0, k]
    while window[1] <= len(s):
        sub = s[window[0]:window[1]]
        characters = countLetterPresence(characters, sub)
        window[0] += 1
        window[1] += 1
    return characters

def countLetterPresence(characters, sub):
    for char in characters.keys():
        if characters in sub:
            characters[char] += 1
    return characters

def minKValue(characters, s, lenS):
    k = lenS // 2
    kmin = 0
    limR = lenS
    limL = 1
    klant = -1
    krant = -1
    while limR != limL and k >= limL and k <= limR:
        #print("Init: inf: {}, sup: {}, k: {}".format(limL, limR, k))
        ward = False
        qtdParts = lenS - k + 1
        characters = getLetterSubsPresence(s, k, characters)
        #print("map: {}".format(chr))
        for char in characters.keys():
            if characters[char] == qtdParts:
                kmin = k
                ward = True
            characters[char] = 0
        if k == klant or k == krant: break
        if not ward:
            limL = k
            klant = k
            k += k // 2
        else:
            limR = k
            krant = k
            k -= k // 2
    return kmin

def process(s, lenS):
    characters = getCharacters(s)
    if lenS == 1 or len(characters.keys()) == 1:
        return 1
    else:
        return minKValue(characters, s, lenS)

def run():
    s = input()
    lenS = len(s)
    minK = process(s, lenS)
    print(minK)

#print(getCharacters('stesctsc'))
run()