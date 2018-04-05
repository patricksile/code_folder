sentence = "should return the correct value for a single word"

def to_weird_case(sentence):
    counter = 0
    weird_sentence = ""
    for char in sentence:
        if char == " " and counter % 2 == 0:
            weird_sentence += char
            counter += 1
        elif char != " " and counter % 2 == 0:
            weird_sentence += char.upper()
        else:
            weird_sentence += char.lower()
        counter += 1
    return weird_sentence

print (to_weird_case(sentence))
