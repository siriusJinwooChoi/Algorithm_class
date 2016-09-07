#-*- coding: utf-8 -*-
"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#Testcase_1
def gcd(num1, num2):
    while True:
        n = num1 % num2
        if n == 0:
            return num2
        num1 = num2
        num2 = n    

if __name__ == '__main__':
    for testcase in range(input()):
        s = raw_input()
        values = s.split()
        print gcd(int(values[0]), int(values[1]))
        print (int(values[0]) * int(values[1])) / gcd(int(values[0]), int(values[1]))
"""
#Testcase_2
def gcd(a, b):
    while True:
        r = a % b
        if r == 0:
            return b
        a = b
        b = r


if __name__ == '__main__':
    for testcase in range(input()):
        strin = raw_input()
        values = strin.split()
        print '%d' % gcd(int(values[0]), int(values[1]))
        #print gcd(int(values[0]), int(values[1]))
        print '%d' % ((int(values[0]) * int(values[1])) / gcd(int(values[0]), int(values[1])))
        #print (int(values[0]) * int(values[1])) / gcd(int(values[0]), int(values[1]))
