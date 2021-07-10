T= input('Please enter a string ')
def most_frequent(string):
    di = dict()
    for key in string:
        if key not in di:
            di[key] = 1
        else:
            di[key] += 1
    return di

print (most_frequent(T))
