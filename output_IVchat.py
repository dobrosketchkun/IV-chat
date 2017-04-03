#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import time
import ipfsapi
from roster import roster as roster


api = ipfsapi.connect('127.0.0.1', 5001)

DEBUG = 0
point = 0

def printt(x, *kargs):
    if DEBUG == 1:
        print(x)


with open('TEST_RANDOM_DO_NOT_USE_IN_REAL_CONVERSATION.txt', 'r') as f:
    all_random = f.read()

def encrypt(string, key):
    return "".join(chr(ord(i) ^ ord(j)) for (i, j) in zip(string, key))
    
    
def decrypt(ciphertext, key):
    return encrypt(ciphertext, key)

print('Chat:')
data1 = [None]
data2 = [None]

data1 = [None for x in roster]
data2 = [None for x in roster]


while True:
    try:
        for number in range(len(roster)):
            printt('number', number)
            printt(roster[number][0])
            data = api.get_pyobj('/ipns/' + roster[number][0])
            printt(['data2',data])
            point = data[1] 
            printt(['point', point])
            end = data[2]
            printt(['end', end])
            key = all_random[point:end]
            printt(['key',key])
            decr = decrypt(data[0], key)
            printt(['decr',decr])
            data2[number] = data
            printt(data2)
            
            
            if decr != data1[number]:
            
                print(roster[number][1] + ':',decr)
                data1[number] = decr

    except Exception as e:
        printt(['Nope,', e])
#        decr = data1
 



#    time.sleep(5)


