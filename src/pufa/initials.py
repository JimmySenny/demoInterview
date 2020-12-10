#!/usr/bin/python3
# -*- coding:utf-8 -*-

#def initials(s:'char')->char:
def initials(s):
    out = '';
    s = s.split( ' ' );
    l = len(s);
    for i in range( l ):
        tmp = chr(ord(s[i][0]) - 32 );
        out = out + tmp;
    return out;



def main():
    while True:
        i = input();
        if i == '0':
            break;
        else:
            print( initials( i ) );

if __name__ == '__main__':
    main();
