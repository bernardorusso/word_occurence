# Bag of all words within the text (no punctuation)
def getfeatures(txt):
    bag = nltk.word_tokenize(txt.upper())
    bag = [w for w in bag if w.isalpha() and len(w)>2 and len(w)<20]
    return unique_elts(bag)

# Strips all punctuation from a string
def rem_punct(w):
    ps = string.punctuation
    while ps.__contains__(w[0]) or ps.__contains__(w[-1]):
        for p in ps:
            w=w.strip(p)
    return w

# Flattens a multi-leveled list
# [A,[B,[C]]] -> [A,B,C]
def flatten(a_list):
    new_list = []
    for e in a_list:
        if type(e)==list:
            new_list.extend(flatten(e))
        else:
            new_list.append(e)
    return new_list

# Unique elements of a list
def unique_elts(alist):
    uni_elts = []
    for elt in alist:
        if not uni_elts.__contains__(elt):
            uni_elts.append(elt)
    return uni_elts
