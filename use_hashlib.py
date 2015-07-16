import hashlib

md5=hashlib.md5()
md6=hashlib.md5()
md5.update("how to use md5 in python hashlib?".encode("utf-8"))
md6.update("how to use md5 in ".encode("utf-8"))
md6.update("python hashlib?".encode("utf-8"))
print(md5.hexdigest())
print(md6.hexdigest())


sha1=hashlib.sha1()
sha1.update("how to use sha1 in ".encode("utf-8"))
sha1.update("python hashlib?".encode("utf-8"))
print(sha1.hexdigest())

def calc_md5(password):
    pwmd5=hashlib.md5()
    pwmd5.update(password.encode("utf-8"))
    return pwmd5.hexdigest()

db={'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'}

def login(user,password):
    if user in db:
        if calc_md5(password)==db[user]:
            print("login successfully")
        else:
            print("wrong password")
    else:
        print("unknown user")

#print(calc_md5("password"))
login("michael","123456")
login("asd","123")
login("michael","nishiyigedashabi")
