# -*- coding: utf-8 -*-
import hashlib

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
		 


def main():
	# hash_list = open('senhas1.txt', 'r')
	# dictionary = open(u'C:\\Users\\Roberto\\Downloads\\10-million-combos\\wordlist.txt', 'r')
	file_hashes = open('crypted.txt', 'r')
	hash_content = file_hashes.read()
	hash_list = hash_content.splitlines()
	file_hashes.close()

	file_dictionary = open('dic.txt', 'r')
	dictionary_content = file_dictionary.read()
	dictionary_list = dictionary_content.splitlines()
	file_dictionary.close()


	known = {}
	words = list(dictionary_list)
	print dictionary_list
	for i in hash_list:
		known, words = dictionaryAttack(known, words, i)
	print known
	print words
	print dictionary_list

if __name__ == '__main__':
	main()