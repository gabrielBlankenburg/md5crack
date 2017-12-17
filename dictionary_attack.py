#!/usr/bin/python
# -*- coding: utf-8 -*-
import hashlib
import sys
import getopt

def dictionaryAttack(known, words, hash):
	# Tries the list of known hashes
	if hash in known:
		print hash + ':' + known[hash].decode('utf8')
		return known, words

	# Go through a copy of words so won't have any problem removing its indexes
	for i in words[:]:
		# Creates a hash of the current word, add to the known and then remove it from the wordlist
		h = hashlib.md5(i)
		attempt = h.hexdigest()
		known[attempt] = i
		words.remove(i)

		# Compares the hash created with the word and the hash to find
		if attempt == hash:
			print hash + ':' + i.decode('utf8')
			return known, words

	print 'Could not crack this hash. Try another dictionary'
	return known, words

def createListFromFile(file_name):
	file = open(file_name, 'r')
	content = file.read()
	list = content.splitlines()
	file.close()
	return list


def main(argv):
	arg_file_hashes = ""
	arg_dictionary_file = ""
	arg_output_file = ""
	arg_hash = ""
	arg_dictionary = ""
	# Check the arguments
	try:
		opts, args = getopt.getopt(argv,"h",["fhashes=","fdic=","foutpass=", "hashes=", "dictionary=", "foutpass="])
	except getopt.GetoptError:
		print 'Invalid syntax. Type dictionary_attack.py -h for help'
		sys.exit()

	# Go through the options
	for opt, arg in opts:
		if opt == '-h':
			'dictionary_attack.py --fhashes <file_with_hashes> --fdic <dictionary_file> --fout <output_file>'
			sys.exit()
		elif opt in ("--fhashes"):
			arg_file_hashes = arg
		elif opt in ("--fdic"):
			arg_dictionary_file = arg
		elif opt in ("--foutpass"):
			arg_output_file = arg
		elif opt in ("--hashes"):
			arg_hash = arg
		elif opt in ("--dictionary"):
			arg_dictionary = arg

	hash_list = []
	dictionary_list = []

	# The hashes
	if arg_file_hashes != "":
		hash_list = createListFromFile(arg_file_hashes)
	if arg_hash != "":
		# Separetes the words by space and join to the other list
		aux = arg_hash.split(' ')
		hash_list = hash_list + aux

	# Case the hash list is empty
	if hash_list == []:
		print "No hash is inserted. Type dictionary_attack.py -h for help."

	# The dictionary
	if arg_dictionary_file != "":
		dictionary_list = createListFromFile(arg_dictionary_file)
	if arg_dictionary != "":
		# Separetes the words by space and join to the other list
		aux = arg_dictionary.split(' ')
		dictionary_list = dictionary_list + aux

	# Case the dictionary list is empty
	if dictionary_list == []:
		print "No dictionary is inserted. Type dictionary_attack.py -h for help."

	known = {}
	words = dictionary_list

	# Do the attack
	for hash in hash_list:
		known, words = dictionaryAttack(known, words, hash)

	if arg_output_file != "":
		output_string = ''
		for i in known:
			if i in hash_list:
				output_string = output_string + i + ':' + known[i] + '\n'
		output_file = open(arg_output_file)


if __name__ == '__main__':
	main(sys.argv[1:])