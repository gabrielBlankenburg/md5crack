#!/usr/bin/python
# -*- coding: utf-8 -*-
import hashlib
import sys
import getopt

def dictionaryAttack(known, words, current_hash, remove_not_found_message, remove_any_message):
	# Tries the list of known hashes
	if current_hash in known:
		if not remove_any_message:
			print current_hash + ':' + known[current_hash].decode('utf8')
		return known, words

	# Go through a copy of words so won't have any problem removing its indexes
	for i in words[:]:
		# Creates a hash of the current word, add to the known and then remove it from the wordlist
		h = hashlib.md5(i)
		attempt = h.hexdigest()
		known[attempt] = i
		words.remove(i)

		# Compares the hash created with the word and the hash to find
		if attempt == current_hash:
			if not remove_any_message:
				print current_hash + ':' + i.decode('utf8')
			return known, words

	if not remove_any_message and not remove_not_found_message:
		print 'Could not crack the hash ' + current_hash + ' . Try another dictionary'
	return known, words

def createListFromFile(file_name):
	file = open(file_name, 'r')
	content = file.read()
	list_content = content.splitlines()
	file.close()
	return list_content

def removeDuplicate(list_elements):
	aux = set(list_elements)
	return list(aux)

def main(argv):
	arg_file_hashes = ""
	arg_dictionary_file = ""
	arg_output_file = ""
	arg_hash = ""
	arg_dictionary = ""
	remove_duplicate = False
	remove_not_found_message = False
	remove_any_message = False
	# Check the arguments
	try:
		opts, args = getopt.getopt(argv,"h",["fhashes=","fdic=","foutpass=", "hashes=", "dictionary=", "rmduplicate", \
									"rmnotfoundmsg", "rmanymsg"])
	except getopt.GetoptError:
		print 'Invalid syntax. Type dictionary_attack.py -h for help'
		sys.exit()

	# Go through the options
	for opt, arg in opts:
		if opt == '-h':
			print '`-h` Shows the help. \n\n' \
					+ '--fhashes <path of a file containing hashes> Opens a specified file with hashes separeted by line break.\n\n' \
					+ '--fdic <path of a file containing the wordlist> Opens a specified file with words that later the script is going to use to try to guess the passwords.\n\n' \
					+ '--foutpass <path to the output file> Choose a file to save the hashes and passwords found in the pattern `hash:password`. Notice that if the file does not exist it will create one and if the file already exists it will OVERWRITE it. This argument is optional.\n\n' \
					+ '--hashes "<a hash> <another hash>" Inputs the hashes via command line. The hashes must be between a double quotation marks and separeted by spaces.\n\n' \
					+ '--dictionary "<a word> <another word>" Input the wordlist via command line. The words must be between a double quotation marks and separeted by spaces. Notice that if the word contain space, please put it inside a .txt file and use the `--fdic` parameter.\n\n' \
					+ '--rmduplicate This may improve the speed of the script by removing duplicated values in the hashes and words.\n\n' \
					+ '--rmnotfoundmsg This prevents showing messages when not founding the passwords.\n\n' \
					+ '--rmanymessage This prevents showing any messages related to found passwords at all.'
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
		elif opt in ("--rmduplicate"):
			remove_duplicate = True
		elif opt in ("--rmnotfoundmsg"):
			remove_not_found_message = True
		elif opt in ("--rmanymsg"):
			remove_any_message = True

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
		exit()

	# Removes de duplicated if passed the argument rmDuplicate
	if remove_duplicate:
		hash_list = removeDuplicate(hash_list)
		dictionary_list = removeDuplicate(dictionary_list)

	known = {}
	words = list(dictionary_list)

	# Do the attack
	for h in hash_list:
		known, words = dictionaryAttack(known, words, h, remove_not_found_message, remove_any_message)

	if arg_output_file != "":
		output_string = ''
		for i in known:
			if i in hash_list:
				output_string = output_string + i + ':' + known[i] + '\n'
		output_file = open(arg_output_file)


if __name__ == '__main__':
	main(sys.argv[1:])