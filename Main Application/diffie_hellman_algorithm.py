#  Diffie-Hellman asymmetric key exchange
class Diffie_Hellman:
	def __init__(self, AliceKey, BobKey):
		self.dictionary = {'a':"1",'b':"2","c":"3","d":"4","e":"5","f":"6","g":"7","h":"8","i":"9","j":"11","k":"12","l":"13","m":"14","n":"15","o":"16","p":"17","q":"18","r":"19","s":"21","t":"22","u":"23","v":"24","w":"25","x":"26","y":"27","z":"28", "@":"29", "#":"31", ".":"32",",": "33", "$":"34", "%":"35", "^":"36", "&": "38","*":"39","(":"41",")":"42","_":"43","+":"44", "=":"45", "?":"46", "/":"47",">":"48", "<":"49", "[":"50", "]":"51", "|":"52","!":"53","-":"54",":":"55"}
		self.AliceKey = AliceKey
		self.BobKey = BobKey

		# compute Alice's public key given the global parameters and her private key a
		p = 90934050934953958349857934759345983495734957934875938953475938745953987593487538749
		g = 11
		self.astar=self.publickey(g,self.AliceKey,p)
		# print("the public key of Alice is ", self.astar)

		# compute Bob's public key given the global parameters and her private key b
		self.bstar=self.publickey(g,self.BobKey,p)
		# print("the public key of Bob is ", self.bstar)

	# message_list = input("Enter a message to be encrypted: ").split(" ")

	def superkey(self, xstar,a,p): 
		global x
		x=pow(xstar,a,p)
		return x

	def publickey(self, g,a,p):  
		bstar=pow(g,a,p)
		return bstar

	# define a few functions
	def encrypt(self, message_list, astar, b):
		global word, encrypted_message_list, p

		# compute the superkey x given the public key of Bob and the private key of Alice


		# compute super key x given bstar (Bob's public key), a (Alice's private key)
		# and the parameter p

		# set the global parameters known to everybody
		# p=123456791
		# g=17
		# p = 429384928374923933
		# p = 89382492374972964596851
		p = 90934050934953958349857934759345983495734957934875938953475938745953987593487538749
		g = 11


		# compute super key x given bstar (Alice's public key), b (Bob's private key)
		x = self.superkey(astar,b,p)  
		# print("the superkey is = ", x)

		# encryption (simple solution)
		word = ""
		encrypted_message_list = []
		for item in message_list:
			for char in item:
				for key, value in self.dictionary.items():
					if char.lower() == key:
						char = value
						word = word + char + '0'   #insert 0 to separate between words in a sentence
			word = int(word)
			# print(f"word is {word}")
			encrypted = (word+x) % p
			encrypted_message_list.append(encrypted)
			word = ""
		
		# print("superkey is", x)
		# print(f"The message list is {message_list}")
		# print('encrypted message = ', encrypted_message_list)
		return encrypted_message_list

	# and to decrypt it
	def decrypt(self, encrypted_message_list, bstar, a):
		x = self.superkey(bstar,a,p)  
		decrypted_mes = w = originalMes = ""

		for ele in encrypted_message_list:
			decrypted = (ele-x)%p
			decrypted_mes = decrypted_mes + str(decrypted) + " "

		# print(f"decrypted_message_list = {decrypted_mes.split(' ')}")
		
		for num in decrypted_mes.split(" "):
			for i in num.split("0"):
				for key, value in self.dictionary.items():
					if i == value:
						i = key
						w += i
			originalMes = originalMes + w + " "
			w = ""

		return originalMes


# diffie_hellman = Diffie_Hellman(11, 13)
# diffie_hellman.encrypt(Diffie_Hellman.message_list, diffie_hellman.astar,diffie_hellman.BobKey)
# print(f'The decrypted original message is "{diffie_hellman.decrypt(encrypted_message_list,diffie_hellman.bstar, diffie_hellman.AliceKey).rstrip()}".')