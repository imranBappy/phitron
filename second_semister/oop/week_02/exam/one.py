l = ["This", "is", "very", "fantastic"]

def create_string(l):
    s = ""
    for i in l:
        s += i + " "
    return s

print(create_string(l))
