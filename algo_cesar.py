# -*-coding:Utf-8 -*

#import os #If you want make a pause to the program, activ this

def crypte_to_cesar():
	"""This functions is a script to crypte a "phrase" with algorithm of cesar"""


	nocrypt = input("Enter what you want to crypte: ") #Input what you want to crypte ! 
	nocrypt = nocrypt.lower() #We lower the result 

	alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] #Alphabet for use in cryptage

	nocrypt_list = list(nocrypt) #We reate a list from the input 

	#For crypte the input
	i = 0
	crypted = []
	for i,j in enumerate(nocrypt_list): #We enumerate in i (i will contient number of len(nocrypt_list) (0.1......n)) and j (j will contient all the caracter of nocrypt_list) 
		#print(alphabet.index(nocrypt_list[i])) #This is for debug
		#print(alphabet[nocrypt_list.index(j) + 2]) #This is for debug
		if nocrypt_list[i] == ' ' or nocrypt_list[i] == int: #Exception for space and for caractere in int #BUG when he write a number - will resolte in version 1.5
			crypted.append(nocrypt_list[i]) #We append space an int caractere in list crypted
			pass
		else:  #If the caractere is not a space or int
			nocrypt_list[i] = alphabet[alphabet.index(nocrypt_list[i]) + 2] #Crypte ! 
			#print(nocrypt_list[i]) #This is for debug
			crypted.append(nocrypt_list[i]) #We append the new caractere in list crypted
	crypted = "".join(crypted)
	print("The version crypted of your input is:\n","-",crypted) #We print result
			

crypte_to_cesar() #Lunch the function ! 

#os.system("Pause") #DEBUG
