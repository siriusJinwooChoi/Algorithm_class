#-*- coding :utf-8 -*-

def gcd(num1, num2):
    while True:
        r = num1 % num2
        if r == 0:
            return num2
        num1 = num2
        num2 = r

if __name__ == '__main__':
    s = raw_input()
    for a in range(int(s)):
        string = raw_input()
        #values = string.split()
        a, b = string.split()
        #print gcd(int(values[0]), int(values[1]))
        print 'gcd is %d' % (gcd(int(a), int(b)))
