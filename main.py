import hashlib


test = 'test.jpeg'

print("Полный путь до файла :",end = ' ')
filename = rf'{input()}' # введите путь до файла (полный)


def getBitesInFile(filename):
    with open(filename,'rb') as f:
        bites = f.read()
        f.close()
    return bites


def sha256(filename):
    b = getBitesInFile(filename)
    hash_b = hashlib.sha256(b)
    return hash_b.hexdigest()


def md5(filename):
    b = getBitesInFile(filename)
    hash_b = hashlib.md5(b)
    return hash_b.hexdigest()


def sha512(filename):
    b = getBitesInFile(filename)
    hash_b = hashlib.sha512(b)
    return hash_b.hexdigest()

def returnHash(filename):
    print('\n'+filename+' : ')
    print( sha256(filename) + ' = sha256')
    print(md5(filename)+' = md5')
    print(sha512(filename)+' = sha512'+'\n')


if __name__ == '__main__':
    returnHash(test)
    returnHash(filename)

    #чтобы программа не закрывалась     
    input()
