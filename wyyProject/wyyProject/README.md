这是一个爬取网易云音乐评论的脚本：

源：https://music.163.com/

目标字段：评论用户，评论，评论时间，点赞数

分析：
评论的接口url是：https://music.163.com/weapi/v1/resource/comments/R_SO_4_513360721?csrf_token=
请求方式为：post
参数为：①params②encSecKey（两个很长的字符串）


四个参数：
参数①：{"rid":"R_SO_4_25713016","offset":"20","total":"false","limit":"20","csrf_token":"aeafba538aee576e95a9222fa765f67b"}
参数②：010001
参数③：00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7
参数④：0CoJUm6Qyw8W8jud


#window.asrsea  js代码部分
!function() {
    function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {
        var h = {}
          , i = a(16);
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        h
    }
    function e(a, b, d, e) {
        var f = {};
        return f.encText = c(a + e, b, d),
        f
    }
    window.asrsea = d,
    window.ecnonasr = e
}();


###
var bYc0x = window.asrsea(JSON.stringify(i9b), bkY0x(["流泪", "强"]), bkY0x(VM5R.md), bkY0x(["爱心", "女孩", "惊恐", "大笑"]));
            e9f.data = k9b.cz0x({
                params: bYc0x.encText,
                encSecKey: bYc0x.encSecKey
            })
            
            
分析：window.asrsea = d,说明这个window.asrsea函数就是d  
function d(d, e, f, g) {
    var h = {}
      , i = a(16);
    return h.encText = b(d, g),
    h.encText = b(h.encText, i),
    h.encSecKey = c(i, e, f),
    h
}


时间：2019年6月10日16:59:24
找到一个未加密的接口：http://music.163.com/api/v1/resource/comments/R_SO_4_513360721?limit=20&offset=0
