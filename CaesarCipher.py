import string
class CaesarCipher:
    def __init__(self,sdvig):
        self.sdvig = sdvig
    def encode(self,stroka):
        a = ''
        for i in range(len(stroka)):
            if stroka[i] in string.ascii_lowercase:
                a+=string.ascii_lowercase[(string.ascii_lowercase.index(stroka[i])+self.sdvig)%26]
            if stroka[i] in string.ascii_uppercase:
                a+=string.ascii_uppercase[(string.ascii_uppercase.index(stroka[i])+self.sdvig)%26]
            if stroka[i] not in string.ascii_letters:
                a+=stroka[i]
        return a
    def decode(self,stroka):
        a = ''
        for i in range(len(stroka)):
            if stroka[i] in string.ascii_lowercase:
                a+=string.ascii_lowercase[(string.ascii_lowercase.index(stroka[i])-self.sdvig)%26]
            if stroka[i] in string.ascii_uppercase:
                a+=string.ascii_uppercase[(string.ascii_uppercase.index(stroka[i])-self.sdvig)%26]
            if stroka[i] not in string.ascii_letters:
                a+=stroka[i]
        return a
cipher = CaesarCipher(5)
print(1)
print(cipher.encode('Beegeek'))      # Gjjljjp
print(cipher.decode('Gjjljjp')) 