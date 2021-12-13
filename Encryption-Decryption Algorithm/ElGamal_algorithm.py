import random
from math import pow
import unicodedata

class ElGamal:
    def __init__(self,k, p):
        self.a = random.randint(2,10)
        self.k = k
        self.p = p

    def setK(self, q):
        self.k = self.gen_key(q)
        
    #To find gcd of two numbers
    def gcd(self,a,b):
        if a<b:
            return self.gcd(b,a)
        elif a%b==0:
            return b
        else:
            return self.gcd(b,a%b)

    #For key generation i.e. large random number
    def gen_key(self,q):
        key = random.randint(pow(10,20),q)
        while self.gcd(q,key)!=1:
            key = random.randint(pow(10,20),q)
        return key

    def power(self,a,b,c):
        x = 1
        y = a
        while b > 0:
            if b % 2 == 0:
                x = (x * y) % c
            y = (y * y) % c 
            b = int(b / 2)
        return x%c

    #For asymetric encryption
    def encryption(self, msg, q, h):
        encrypted_message = []
        # self.k = self.gen_key(q)
        s = self.power(h,self.k,q)
        for i in range(0,len(msg)):
            encrypted_message.append(msg[i])
        # print("g^k used= ", self.p)
        # print("g^ak used= ", s)
        for i in range(0,len(encrypted_message)):
            encrypted_message[i] = s*ord(encrypted_message[i])
        return encrypted_message 

    #For decryption
    def decryption(self, encrypted_mes, key, q, g):
        decrypt = []
        self.p = self.power(g, self.k, q)
        h = self.power(self.p, key, q)
        print("h is", h)
        for i in range(0,len(encrypted_mes)):
            decrypt.append(chr(int(encrypted_mes[i]/h)))
        return decrypt

encrypted_message_list = []
temp = 0
msg = input("Enter message to be encrypted: ")
elgamal = ElGamal(0,0)
q=random.randint(pow(10,20),pow(10,50))
elgamal.setK(q)
g=random.randint(2,q)
key=elgamal.gen_key(q)
h=elgamal.power(g,key,q)
encrypted_mes = elgamal.encryption(msg,q,h)


print("Original Message=", msg)
print("Encrypted Message=", encrypted_mes)


msg1 = ' '.join([str(i) for i in encrypted_mes])
myList = msg1.split(" ")
# print(myList)
for item in myList:
    for i in item:
        temp = temp * 10 + int(i) 
    encrypted_message_list.append(temp)
    temp = 0

print("encrypted list is", encrypted_message_list)

d_msg = elgamal.decryption(encrypted_message_list,key,q, g)
print(d_msg)
decrypted_message=''.join(d_msg)
print(decrypted_message)
output = unicodedata.normalize('NFKD', decrypted_message).encode('ASCII', 'ignore').decode("utf-8") 
print("Decryted Message =", output)