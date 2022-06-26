'''
Problem
Asked by Amazon.

Given a string, find the length of the smallest window that contains every distinct character.
Characters may appear more than once in the window.

For example, given "jiujitsu", you shoud return 5, corresponding to the final five letters.
'''

'''
Solution

map d
l = list()
large = 0 
for c in string:
    if c in d.keys():
       d.clear()
       if len(l) > large:
          large = l
       l = l.clear()
    else:
      l.append(c)
      d[c] = True

return large
'''

def find_smallest_window(string):
    d = dict()
    l = list()
    large = 0
    for c in string:
        if c in d.keys():
            d.clear()
            if len(l) > large:
                large = len(l)
            l.clear()
        l.append(c)
        d[c] = True

    if len(l) > large:
        large = len(l)
    return large


if __name__ == '__main__':
    string = "jiujitsu"
    print(find_smallest_window(string))
