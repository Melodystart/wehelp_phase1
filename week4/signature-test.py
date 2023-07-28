import hmac
from hashlib import sha1
from itsdangerous import *

secret_key = base64_encode(b'This is my secret')
session_value = base64_encode(b'{"SIGNED-IN":true}')

time = 1690341586 # UNIX時間格式: Jul 26 2023 11:19:46
timestamp = base64_encode(time.to_bytes(4, byteorder='big'))

msg = session_value + (b'.') + timestamp

print(session_value.decode("utf-8")) #session相符:eyJTSUdORUQtSU4iOnRydWV9
print(timestamp.decode("utf-8"))     #timestamp相符:ZMCQ0g

#方法一簽章：(加salt)
s = Signer(secret_key, salt='cookie-session', sep='.', key_derivation='hmac', digest_method=sha1, algorithm=None)
ans1 = base64_encode(s.get_signature(msg))
print(ans1.decode("utf-8"))
#方法一驗證簽章是否正確：
deans1 = base64_decode(ans1)
print(s.verify_signature(msg,deans1))

#方法二簽章：
h = hmac.new(secret_key, msg, sha1)
ans2 = base64_encode(h.hexdigest())
print(ans2.decode("utf-8"))
#方法二驗證簽章是否正確：
deans2 = base64_decode(ans2)
print(hmac.compare_digest(bytes(h.hexdigest(), 'utf-8'), deans2))
