#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ipfsapi

DEBUG = 0
point = 0

api = ipfsapi.connect('127.0.0.1', 5001)


with open('TEST_RANDOM_DO_NOT_USE_IN_REAL_CONVERSATION.txt', 'r') as f:
    all_random = f.read()


def spoint(point):
    with open('pointt', 'w') as fpoint:
        fpoint.write(str(point))


def printt(x, *kargs):
    if DEBUG == 1:
        print(x)


def encrypt(string, key):
    return "".join(chr(ord(i) ^ ord(j)) for (i, j) in zip(string, key))

    
print ("You:")
while True:
    data = input("")
    
    printt(['point',point])
    end = point + len(data)
    printt(['end',end])
    key = all_random[point:end]
    printt(['key',key])
    data_enc = encrypt(data, key)
    printt(['data_enc',data_enc])
    
    data_ipfs = api.add_pyobj([data_enc, point, end])
    printt(['data_ipfs', [data_enc, point, end]])
    data_ipns = api.name_publish('/ipfs/' + data_ipfs)
    printt(['ipfned. Do it again.'])
    point = end
    spoint(point)
