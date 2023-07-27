import hmac
from hashlib import sha1
from itsdangerous import *

secret_key = base64_encode(b'This is my secret')
session_value = base64_encode(b'{"SIGNED-IN":true}')

time = 1690341586 # UNIX時間格式: Jul 26 2023 11:19:46
timestamp = base64_encode(time.to_bytes(4, byteorder='big'))

msg = session_value + (b'.') + timestamp

#方法一：有加salt
s = Signer(secret_key, salt='cookie-session', sep='.', key_derivation='hmac', digest_method=sha1, algorithm=None)
ans1 = base64_encode(s.get_signature(msg))

#方法二：
h = hmac.new(secret_key, msg, sha1)
ans2 = base64_encode(h.hexdigest())

#網頁cookie: eyJTSUdORUQtSU4iOnRydWV9.ZMCQ0g.mQ06_NzwO_qHmHyMrFj-j9ga3ME
print(session_value.decode("utf-8")) #session相符:eyJTSUdORUQtSU4iOnRydWV9
print(timestamp.decode("utf-8"))     #timestamp相符:ZMCQ0g
#方法一不符:QXBWUm85cXBWWUppZ21LUGVjZHNzM095Z1BJ
print(ans1.decode("utf-8"))
#方法二不符:ZmRkZGJmMjZhNTM0ZDVhNmQwMTEyNDkwNjgwMGE5ODY2ODEzNjcxOQ
print(ans2.decode("utf-8"))  