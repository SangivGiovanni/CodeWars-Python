def anagrams(word, words):

    a_list = []

    for w in words:
        if sorted(w) == sorted(word):
            a_list.append(w)

    return a_list
