def most_frequent(word):
    di = dict()
    for key in word:
        if key not in di:
            di[key] = 1
        else:
            di[key] += 1
    return di

def sortingdic(dic):
   return dict(reversed(sorted(dic.items(), key=lambda item: item[1])))

T= input('Please enter a string ')
word = list(T)
dic = most_frequent(word)
print (sortingdic(dic))
