#Problem Set 1
#Name: pr1malbyt3s
#Description: This program calculates and prints the 1000th prime number.

#Import necessary libraries.


#Create a list of all possible odd integers.
odd_list = []
for x in range(3, 10000, 2):
    odd_list.append(x)

#Create is_prime function to test for primality.
def is_prime(a):
    for b in range(3, a, 2):
        if not (a % b):
                return False
    return True

#Iterate odd_list to check from primality and remove any multiples of numbers.
for y in range (len(odd_list)):
    if is_prime(odd_list[y]):
        odd_list.remove(odd_list[y])
    else:
        for z in range(y, len(odd_list) - 1):
            if (odd_list[z] % odd_list[y]):
                odd_list.remove(odd_list[z])



#Print function to verify list contents.
for j in range(len(odd_list)):
    print(odd_list[j])
#print("test")
