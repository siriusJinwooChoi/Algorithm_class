import sys

def firsttest():
    s = raw_input()
    print s
    s = s.split()
    print s
    s.sort()
    print s

def secondtest():
    s = raw_input()
    tlist = s.split()

    #First Solution
    """
    for a in range(len(tlist)-1):
        for b in range(1, len(tlist)-a):
            if int(tlist[b-1]) > int(tlist[b]):
                temp = tlist[b-1]
                tlist[b-1] = tlist[b]
                tlist[b] = temp
    print tlist[0]
    print tlist[len(tlist)-1]
    """

    #Second Solution
    """
    mini = int(tlist[0])
    maxi = int(tlist[0])
    for a in range(len(tlist)):
        if int(tlist[a] < mini):
            mini = tlist[a]
        else:
            maxi = tlist[a]
    print mini
    print maxi
    """

def thirdtest():
    data = []
    n = int(raw_input())
    for k in range(n):
        a = len(data)
        s = sys.getsizeof(data)
        print('length: {0:3d}, bytes: {1:4d}'.format(a,s))
        data.append(None)
    
if __name__ == '__main__':
    #firsttest()
    secondtest()
    #thirdtest()
