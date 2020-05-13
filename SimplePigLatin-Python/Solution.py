def pig_it(text):

    pig_str = ''
    punc = '!?,.:;()'

    for word in text.split():

        if word == text.split()[0]:
            pig = word[1:] + word[0] + 'ay'
            pig_str = pig_str + pig

        elif word in punc:
            pig_str = pig_str + ' ' + word

        else:
            pig = word[1:] + word[0] + 'ay'
            pig_str = pig_str + ' ' + pig

    return pig_str
