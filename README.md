# Transcoding App
## A GUI app for message encryption and decryption
#### Main programming language: Python

#### Motivation:
A huge amount of private data is transmitted across the Internet every day, making it a potential target to be stolen and used by hackers in today's world. Therefore, it is important for us to secure our data by using encryption and decryption techniques during the communication process. However, given the vast number of cryptographic algorithms available nowadays, people may find it difficult to determine the best encryption type for the data they are storing or transmitting. In this project, we will try to implement different algorithms to encode and decode the messages in real-time. Our approach will be to incorporate these implementation functions into a single GUI app that allows users to test different algorithms for their encryption and decryption process. Furthermore, this application will also provide users with a unique feature of analyzing and measuring the algorithmic efficiency by comparing and evaluating the resource usage as well as the executing time of the algorithms, based on a wide range of random input data.\
In this work, our strategy will be to implement some well-known cryptographic algorithms into the app as its main function. However, we only plan to deal with a small sample of asymmetric public key algorithms instead of investigating other algorithms and cryptographic techniques for message integrity, authentication, and digital signatures. In short, assymmetric encryption uses the public key for the encryption, and a private key is used for decryption. \
Some of the cryptographic algorithms we are going to use in this app is Diffie_Hellman key-exchange algorithm, ElGamal algorithm and RSA algorithm. However, we are still trying to update our app with the implementation of as many algorithms as possible other than the algorithms mentioned above. In this code, the Diffie_Hellman algorithm and RSA algorithm is working as expected, however, due to some error, we are still having troubles executing other algorithms and we look forward to fixing these issues in the future.\

#### Note: Make sure you have Python installed, and you will also have to install additional python packages via pip to make the app function properly on your local machine. Type these commands in your cmd to install the needed packages:
pip install PyQt5\
pip install PySide2


Below are some of the results for Diffie-Hellman:
### Encoding
![result_encoding](https://user-images.githubusercontent.com/91274419/145750514-65f6913b-66f2-4f31-a640-7288e4df42b9.PNG)
### Decoding
![result_decoding](https://user-images.githubusercontent.com/91274419/145750782-27b1efec-680f-483f-a15b-9d13a06ff1d2.PNG)

Below are some of the results for RSA:
### Encoding
![result_encoding](https://user-images.githubusercontent.com/91274419/201384994-4078ebad-be14-4954-9f23-8d45112817df.png)
### Decoding
![result-decoding](https://user-images.githubusercontent.com/91274419/201385196-73eafdc7-56cf-4d62-a391-4f8835d06240.png)

