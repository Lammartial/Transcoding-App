
class RSA:
	def __init__(self):
		self.dictionary = {'a':"1",'b':"2","c":"3","d":"4","e":"5","f":"6","g":"7","h":"8","i":"9","j":"11","k":"12","l":"13","m":"14","n":"15","o":"16","p":"17","q":"18","r":"19","s":"21","t":"22","u":"23","v":"24","w":"25","x":"26","y":"27","z":"28", "@":"29", "#":"31", ".":"32",",": "33", "$":"34", "%":"35", "^":"36", "&": "38","*":"39","(":"41",")":"42","_":"43","+":"44", "=":"45", "?":"46", "/":"47",">":"48", "<":"49", "[":"50", "]":"51", "|":"52","!":"53","-":"54",":":"55"}
		
		self.p = 90934050934953958349857934759345983495734957934875938953475938745953987593487538749
		self.q = 18532395500947174450709383384936679868383424444311405679463280782405796233163977
		self.e = 13
	# function for extended Euclidean Algorithm 
	def gcdExtended(self, a, b): 
		# Base Case 
		if a == 0 :  
			return b,0,1
				
		gcd,x1,y1 = self.gcdExtended(b%a, a) 
		
		# Update x and y using results of recursive 
		# call 
		x = y1 - (b//a) * x1 
		y = x1 
		
		return gcd,x,y


	def expMod(self,a,k,n):
		if k == 0:
			return 1
		else:
			return (self.expMod(a,k//2, n)**2)*(a**(k%2))%n

	def rsa_encryption(self, msg_list, e, p, q):
		# en = math.pow(msg,e)
		# c = en % n
		word = ""
		encrypted_message_list = []
		for item in msg_list:
			for char in item:
				for key, value in self.dictionary.items():
					if char.lower() == key:
						char = value
						word = word + char + '0'   #insert 0 to separate between words in a sentence
			word = int(word)
			# print(f"word is {word}")
			encrypted = self.expMod(word, e, p * q)
			encrypted_message_list.append(encrypted)
			
			word = ""
		return encrypted_message_list


	def rsa_decryption(self,p,q,e, encryptedMsg):
		decrypted_mes = w = originalMes = ""
		phi_n = (p-1)*(q-1)
		n = p*q
		gcd,d,y = self.gcdExtended(e,phi_n)

		if d<0:
			d += phi_n

		for ele in encryptedMsg:

			decrypted = self.expMod(ele,abs(d), n)
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

		
# rsa = RSA()
# msg = input("Enter a message to be encrypted: ").split(" ")
# encryptedMes = rsa.rsa_encryption(msg, rsa.e, rsa.p, rsa.q)
# print("The encrypted message is", encryptedMes)
# print(rsa.rsa_decryption(rsa.p,rsa.q,rsa.e, encryptedMes))




