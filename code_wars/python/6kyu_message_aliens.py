# Problem: Message from Aliens(6kyu)
"""
Task

Aliens send messages to our planet. They use very strange language. Try to decode their messages.
"""
# My Solution:
def decode(m):
    alien_dict = {
    "__":' ', "/\\":'a', "]3":'b',"(":'c',"|)":'d' ,"[-":'e',"/=":'f',"(_,":'g' ,"|-|":'h' ,"|":'i',"_T":'j',
    "/<":'k', "|_":'l',"|\/|":'m' ,"|\\|":'n' ,"()":'o' ,
    "|^":'p' ,"()_":'q' ,
    "/?":'r' ,"_\\~":'s' ,"~|~":'t' ,"|_|":'u',"\/":'v' ,"\/\/":'w',"><":'x' ,"`/":'y',"~/_":'z'}

    return "".join(alien_dict[key] for key in m.split(m[0]) if key in alien_dict)[::-1]


# Other Solutions:
# Solution 1: By dcieslak
# def decode(m):
    # return ''.join(list(map(lambda x: dic[x] ,filter(len, m.split(m[0]))))[::-1])


assert decode("]()]|_]|_]][-]|-|]") ==  'hello'
assert decode("{|^{|{{|_{]3{") == 'blip'
assert decode('..[-.|_.|^....().[-.|^.__..|)...|.|^.|_|..~|~._\\~.__...[-..|.|)..') == 'die stupid people'
assert decode("'''_\\~'|_|'()'|''('|'|_'[-'|)''__'_\\~'/<'()'()'|_'''__'|\\|'|''/\\'/?']3'__''/?'|_|''()'`/''") ==  'your brain looks delicious'
assert decode('}/\\}~|~}/\\}/<}__}|)}}}[-}~|~}/\\}(}|}|_}|^}|_|}|)}__}|)}}}|\\|}|}/=}__}()}}}~|~}__}`/}/?}}~|~}') == 'try to find duplicated kata'
