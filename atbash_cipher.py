import string
import sys
from queue import Queue
import threading

lookup_table = {

		'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V', 
        'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q', 
        'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L', 
        'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G', 
        'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A'

      } 

# user_input = input("Enter you text here:- ")
# print(user_input)

punctuations = string.punctuation
numbers = string.digits
que = Queue()

def atbash(message):
	print(lookup_table)
	result = ''
	for i in message:
		if (i != ' ' and i not in punctuations and i not in numbers):
			result += lookup_table[i.upper()]
		elif (i in punctuations):
			result += i
		elif (i in numbers):
			result += i
		else:
			result += ' '
	return result

data = ''

def openFile():
	global data
	with open("original_data.txt", "r") as f:
		data = atbash(f.read().rstrip("\n"))
		print(data)
	


print("Vishvajit:- ", data)
#read text from original_data.txt file
# with open("original_data.txt", "r") as f:
# value = f.read().rstrip("\n")
# print(value)
t = threading.Thread(target = openFile())
t.start()
t.join()





#convert first character in upper case
result = data[0].upper() + data[1:]
print("Result:- ", result)

#empty list to store encrypted data
encrypt_data = []

#Convert w to W when input is Chrimstmas is the 25 th december 
for i in result.split(' '):

	if (i.startswith('w')):
		encrypt_data.append(i[0].upper() + i[1:])

	elif not (i.startswith('w')):
		encrypt_data.append(i)
		
#write the output in encrypt_data.txt after encryption
with open("encrypt_data.txt", "w") as f:
	f.write(' '.join(encrypt_data))


