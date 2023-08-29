import regex
def split_POJ_sentence(sentence):
    pattern = r'(?=-)|(?<=\p{Punct})|(?=\p{Punct})|(?<=\s)|(?=\s)'
    return [word for word in regex.split(pattern, sentence) if word]
