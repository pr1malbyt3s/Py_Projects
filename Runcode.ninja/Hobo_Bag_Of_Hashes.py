#!/usr/bin/env python
#This script will accept two files as input, a hash list and a file list. It will then use the provided hash list to find the file in the supplied directory with that hash.

import sys
import hashlib
import os

#Initiate a list that stores all the hashes read from the hash file.
hashList = [] 

#Generate list of hashes from hashfile list.
hash_file = open(sys.argv[1], "r")
for line in hash_file:
	hashList.append(line.strip())

#Initiate a list that stores all the file names to be evaluated.
fileList = []

#Generate the list of files from the user supplied directory.
eval_dir = sys.argv[2]
for file in os.listdir(eval_dir):
	fileList.append(os.path.join(eval_dir,file))

#Hash checker function. This function will generate various hashes of a different file to check if it matches a provided hash.
def hash_checker(file_name, file_hash):
	fp = open(file_name, "rb")
	bytes = fp.read()
	if hashlib.md5(bytes).hexdigest() == file_hash:
		print("Found the file " + str(file_name) + " with the hash of " + hashlib.md5(bytes).hexdigest())
	elif hashlib.sha1(bytes).hexdigest() == file_hash:
		print("Found the file " + str(file_name) + " with the hash of " + hashlib.sha1(bytes).hexdigest())
	elif hashlib.sha224(bytes).hexdigest() == file_hash:
		print("Found the file " + str(file_name) + " with the hash of " + hashlib.sha224(bytes).hexdigest())
	elif hashlib.sha256(bytes).hexdigest() == file_hash:
		print("Found the file " + str(file_name) + " with the hash of " + hashlib.sha256(bytes).hexdigest())
	elif hashlib.sha384(bytes).hexdigest() == file_hash:
		print("Found the file " + str(file_name) + " with the hash of " + hashlib.sha384(bytes).hexdigest())
	elif hashlib.sha512(bytes).hexdigest() == file_hash:
		print("Found the file " + str(file_name) + " with the hash of " + hashlib.sha512(bytes).hexdigest())

#Nested for loop that iterates through each hash in the hashlist to find the file in the file list that matches the hash.
for hash in hashList:
	for sub_file in fileList:
		hash_checker(sub_file, hash)
		
