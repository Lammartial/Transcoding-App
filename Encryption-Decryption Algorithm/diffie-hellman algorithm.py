#  Diffie-Hellman asymmetric key exchange
class Diffie_Hellman:
	def __init__(self, a):
		self.dictionary = {'a':"1",'b':"2","c":"3","d":"4","e":"5","f":"6","g":"7","h":"8","i":"9","j":"11","k":"12","l":"13","m":"14","n":"15","o":"16","p":"17","q":"18","r":"19","s":"21","t":"22","u":"23","v":"24","w":"25","x":"26","y":"27","z":"28", "@":"29", "#":"31", ".":"32",",": "33", "$":"34", "%":"35", "^":"36", "&": "38","*":"39","(":"41",")":"42","_":"43","+":"44", "=":"45", "?":"46", "/":"47",">":"48", "<":"49", "[":"50", "]":"51", "|":"52","!":"53","-":"54",":":"55"}

		# here is the private key of Alice -- has to be < p
		self.a = a 
	message_list = input("Enter a message to be encrypted: ").split(" ")

	def superkey(self, bstar,a,p): 
		global x
		x=pow(bstar,a,p)
		return x

	# define a few functions
	def encrypt(self, message_list, a):
		global word, encrypted_message_list, p, bstar, astar
		# compute the superkey x given the public key of Bob and the private key of Alice
		def publickey(g,a,p):  
			astar=pow(g,a,p)
			return astar

		# compute super key x given bstar (Bob's public key), a (Alice's private key)
		# and the parameter p

		# set the global parameters known to everybody
		# p=123456791
		# g=17
		# p = 429384928374923933
		# p = 89382492374972964596851
		p = 90934050934953958349857934759345983495734957934875938953475938745953987593487538749
		g = 11

		
		# compute Alice's public key given the global parameters and her private key a
		astar=publickey(g,a,p)  	
		print("the public key of Alice is= ", astar)

		# private and public keys for Bob 
		b=11     # it is smaller than p
		bstar=publickey(g,b,p)
		print("the public key of Bob is= ", bstar)

		# compute super key x given bstar (Bob's public key), a (Alice's private key)
		x = self.superkey(bstar,self.a,p)  
		print("the superkey is = ", x)

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
			encrypted = (word+x) % p
			encrypted_message_list.append(encrypted)
			word = ""
		
		print("superkey is", x)
		print(f"The message list is {message_list}")
		print('encrypted message = ', encrypted_message_list)
		return encrypted_message_list

	# and to decrypt it
	def decrypt(self, encrypted_message_list, x):
		decrypted_mes = w = originalMes = ""

		for ele in encrypted_message_list:
			decrypted = (ele-x)%p
			decrypted_mes = decrypted_mes + str(decrypted) + " "

		print(f"decrypted_message_list = {decrypted_mes.split(' ')}")
		
		for num in decrypted_mes.split(" "):
			for i in num.split("0"):
				for key, value in self.dictionary.items():
					if i == value:
						i = key
						w += i
			originalMes = originalMes + w + " "
			w = ""

		return originalMes


diffie_hellman = Diffie_Hellman(a=11)
diffie_hellman.encrypt(Diffie_Hellman.message_list, diffie_hellman.a)
print(f'The decrypted original message is "{diffie_hellman.decrypt(encrypted_message_list, diffie_hellman.superkey(bstar,diffie_hellman.a,p)).rstrip()}".')