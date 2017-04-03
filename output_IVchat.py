#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import ipfsapi
api = ipfsapi.connect('127.0.0.1', 5001)

ipns_addr1 = 'Put the ipns address of your companion here'
DEBUG = 0
point = 0

def printt(x, *kargs):
    if DEBUG == 1:
        print(x)


with open('rand_plain.txt', 'r') as f:
    all_random = f.read()

def encrypt(string, key):
    return "".join(chr(ord(i) ^ ord(j)) for (i, j) in zip(string, key))
    
    
def decrypt(ciphertext, key):
    return encrypt(ciphertext, key)

print('Not you:')
data1 = [None]
data2 = [None]

while True:
    try:
        data2 = api.get_pyobj('/ipns/' + ipns_addr1)
        printt(['data2',data2])
        point = data2[1] 
        printt(['point', point])
        end = data2[2]
        printt(['end', end])
        key = all_random[point:end]
        printt(['key',key])
        decr = decrypt(data2[0], key)
        printt(['decr',decr])

    except Exception as e:
        printt(['Nope,', e])
        decr = data1
 
    if decr != data1:
            
        print(decr)
        data1 = decr


    time.sleep(5)
