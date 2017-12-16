#!/usr/bin/python
# -*- coding: utf-8 -*-
import hashlib
import sys
import getopt

def dictionaryAttack(known, words, hash):
	# Tries the list of known hashes
	for i in known:
		if i == hash:
			print hash + ' = ' + known[i]
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
			print hash + ' = ' + i
			return known, words

	print 'Could not crack this hash. Try another dictionary file'
	return known, words



# {hash : senha}
		 


def main(argv):
	arg_file_hashes = ""
	arg_dictionary_file = ""
	arg_output_file = ""
	# Check the arguments
	try:
		opts, args = getopt.getopt(argv,"h",["fhashes=","fdic=","fout="])
	except getopt.GetoptError:
		print 'test.py --fhashes <file_with_hashes> --fdic <dictionary_file> --fout <output_file>'
		sys.exit()

	# Go through the options
	for opt, arg in opts:
		if opt == '-h':
			'test.py --fhashes <file_with_hashes> --fdic <dictionary_file> --fout <output_file>'
			sys.exit()
		elif opt in ("--fhashes"):
			arg_file_hashes = arg
		elif opt in ("--fdic"):
			arg_dictionary_file = arg
		elif opt in ("--fout"):
			arg_output_file = arg

	file_hashes = open(arg_file_hashes, 'r')
	hash_content = file_hashes.read()
	hash_list = hash_content.splitlines()
	file_hashes.close()

	file_dictionary = open(arg_dictionary_file, 'r')
	dictionary_content = file_dictionary.read()
	dictionary_list = dictionary_content.splitlines()
	file_dictionary.close()


	known = {}
	words = list(dictionary_list)

	for hash in hash_list:
		known, words = dictionaryAttack(known, words, hash)

if __name__ == '__main__':
	main(sys.argv[1:])