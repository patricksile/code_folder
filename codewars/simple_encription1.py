i = 7
if isinstance(i,int):
    i += 1
elif isinstance(i, str):
    i = int(i)
    i += 1

print isinstance(i,int)
