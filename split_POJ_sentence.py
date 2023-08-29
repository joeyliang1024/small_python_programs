import regex
sentence = "(bîn-tsú-tóng) , 「tsóng-thóng. hāu「-suán-jîn. Obama sì-ji̍t。!"
def split_POJ_sentence(sentence):
    pattern = r'(?=-)|(?<=\p{Punct})|(?=\p{Punct})|(?<=\s)|(?=\s)'
    return [word for word in regex.split(pattern, sentence) if word]
