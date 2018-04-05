

def nerdy(words):
    dict_ = {'a':'4', 'A': '4', 'e': '3', 'E': '3', 'l': '1'}
    for key in dict_:
        if key in words.lower():
            words = words.replace(key, dict_[key])
    return words


# Test Zone
x = "AaEel"
print(nerdy(x))
