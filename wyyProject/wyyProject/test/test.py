# # -*- coding: utf-8 -*-
# import os,shutil,json,requests
# from  binascii import hexlify
# from Crypto.Cipher import AES
# import base64
#
# class Encrypyed():
#     def __init__(self):
#         self.pub_key = '010001'
#         self.modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
#
#         self.nonce = b'0CoJUm6Qyw8W8jud'
#
#     def create_secret_key(self, size):
#         return hexlify(os.urandom(size))[:16].decode('utf-8')
#
#     def aes_encrypt(self,text, key):
#         iv = b'0102030405060708'
#         pad = 16 - len(text) % 16
#         text += pad * chr(pad)
#         text = text.encode('utf-8')
#         encryptor = AES.new(key, AES.MODE_CBC, iv)
#         result = encryptor.encrypt(text)
#         result_str = base64.b64encode(result).decode('utf-8')
#         return result_str
#
#     def rsa_encrpt(self,text, pubKey, modulus):
#         text = text[::-1]
#         rs = pow(int(hexlify(text.encode('utf-8')), 16), int(pubKey, 16), int(modulus, 16))
#         return format(rs, 'x').zfill(256)
#
#     def work(self,text):
#         text = json.dumps(text)
#         i=self.create_secret_key(16)
#         encText =self.aes_encrypt(text, self.nonce)
#         encText=self.aes_encrypt(encText,i.encode('utf-8'))
#         encSecKey=self.rsa_encrpt(i,self.pub_key,self.modulus)
#         data = {'params': encText, 'encSecKey': encSecKey}
#         print(data)
#         return data
#
# do=Encrypyed()
# data=do.work(513360721)

# url='https://music.163.com/weapi/v1/resource/comments/R_SO_4_513360721?csrf_token='
#
# # data = {'params': 'khkGzq258K0cvJhgxEh1ByD0P7GoAuNhl56xem4VsjckStFMNyEBYOSQiG0WR6pH5of2iFoQR829u1EOfzD2gqcHwobCkrHSyZ+w1jjR8iVJ9Dhd3VEkcdWi0Bqfj+b39g6kEXgiMVBwovNErbx1cKqoJ5UwewjXQ8mtAkfzzm163kwfGfyc0uG4D5bnpeEj','encSecKey': '9624dc7399416c32c8a39dcb1dba9c9b7e203fb4973d28e46cf4b28df1ae3d63aebb8e541d783684650ff300f84c9c5bd2bdcd674a19a5fa6ca4cf7c7084e440e3e1cfe8ad06f5b04c5a6f1639e2453388288ee899a17173ea854475a90a965906a45d627cbe6e1685a0e6abd9cc6f596fb9c008142b17521405217d707deaa6'}
# headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
#             'Referer': 'http://music.163.com/'}
# session = requests.Session()
# session.headers=headers
# re=session.post(url,data=data)
# print('***')
# print(re.text)

import random



for page in range(100,500):  # 先爬取前100页
    # offset = (page - 1) * 20
    # print(offset)
    print(page)