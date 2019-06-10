import requests as rs
from Crypto.Cipher import AES
import base64
import json
import os
import time
'''
       Coded by nienie
'''

def Nie_get_params(PageNum,Count):
    PageNum = (PageNum-1)*20
    first_param = "{ rid: \"R_SO_4_418603077\", offset: "+str(PageNum)+", total: \"false\", limit: "+str(Count)+", csrf_token: \"\" }"
    forth_param = "0CoJUm6Qyw8W8jud"
    first_key = forth_param
    second_key ='nienienienienien'
    h_encText = AES_encrypt(first_key,first_param)
    h_encText = AES_encrypt(second_key,h_encText)
    return h_encText

def AES_encrypt(key, text):
    iv = '0102030405060708'
    pad = 16 - len(text) % 16
    text +=  pad * chr(pad)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    encrypt_text = encryptor.encrypt(text)
    encrypt_text = base64.b64encode(encrypt_text)
    return encrypt_text

def Nie_get_encSecKey():
    encSrcKey = "6469da86a183fc2fc9df65ac98f67138c8d3048d0626714fe646ecb564d4f8cd386a9c9618bb8a4f2929e50ba32e8991266aba783975e39cc7cf8a61cc3ba76c81c64a3414f38d604ca1bf9f4647c29cd92d5b362eff15cf7bb1e3a52df798a52aafac2f09420a68af9686e2c1a294ccf426b5aac64899486011fc7eca8e79b8"
    return encSrcKey


def N_comment(id,ReviewCount):
    ReviewKeep = 0
    KeepFile = os.getcwd() + os.sep + "Review" + os.sep + str(id) + ".nie"
    fp = open(KeepFile, 'w')
    PageNum = ReviewCount/100
    Count = 100
    if ReviewCount%100 != 0:
        PageNum +=1
    for RP in range(1,PageNum+1):
        if RP == PageNum:
            Count = ReviewCount%100
        data = {
        'params':Nie_get_params(RP,Count),
        'encSecKey':Nie_get_encSecKey()
        }
