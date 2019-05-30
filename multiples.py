'''
The idea is to calculate a key, based on the idea that
 n%3 ==0 if it is a multiple of 3 and n%5==0 if it is multiple
 of 5. Therefore if:

 A = ((n%3)*3)/(n%3) = 0
 B = ((n%5)*5)/(n%5) = 5
 C = 5+3 = 8
 
 then n is multiple of C-(A+B) = 3

 We cna use this fact to detect if a number is multiple of 3 or 5 and
 in the case it is multiple of both, then the result will be 8, for anything
 else we just print the number

 3,5 and 8 then can be keys to a dictionary storing the messages we want to
 display on each case

'''

# Messages we want to display on specific multiples
msgs = {3:"Linio",5:"IT",8:"Linianos"}

# This function claculates the possible key of the dict
# From where we are going to retrieve the message
def calc_key_component(d_r):
	try:
		# if the remainder is zero then we will get a ZeroDivisionError
		return (d_r[1]*d_r[0])/d_r[1]
	except ZeroDivisionError:
		# we found a multiple of 3 or 5
		return 0


def modifyMultiples(custom_range = None):
	#This method will print  the numbers that are not multiple of 3,5 or both, if the number
	#is a multiple of any of the above numbers the will repalce the number like this:
	#multiple of 3 = Linio, multiples of 5= IT or if number is multiple of 3 and 5 = Linianos

	#this variable is meant to be used by the unittest
	multiples = []
	for n in range(1,101) if custom_range == None else custom_range:
		#create a tuple with the multilple and the reminder of n%multiple
		d_r_3 = (3,n%3)
		#create a tuple with the multilple and the reminder of n%multiple
		d_r_5 = (5,n%5)
		# calculate the key 
		k = (8 - int(calc_key_component(d_r_3)+calc_key_component(d_r_5))) 

		try:
			#IF the key is in the dictionary then retrieve the correct message for the key
			msg = msgs[k]
		except KeyError:
			# else use the actual digit
			msg = n
		
		multiples.append(msg)	
		#print(msg)
	#return the multiples list, this is meant to be used by the unittest
	return multiples



if __name__ == '__main__':
	print(modifyMultiples())
