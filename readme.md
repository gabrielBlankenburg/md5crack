# Welcome to the MD5 Crack

**For studying pourposes only!!!**
**Author: Gabriel Gonçalves Blankenburg**

### Requirements 
In order to use the MD5 Crack all you need is [Python 2.7](https://www.python.org/download/releases/2.7/) installed.

### Usage
The usage is very simple. All you need is to have some hashes and a dictionary. They can be inserted both from command line and a txt file.

#### Commands
`-h` Shows the help.
`--fhashes <path of a file containing hashes>` Opens a specified file with hashes separeted by line break.
`--fdic <path of a file containing the wordlist>` Opens a specified file with words that later the script is going to use to try to guess the passwords.
`--foutpass <path to the output file>` Choose a file to save the hashes and passwords found in the pattern `hash:password`. Notice that if the file does not exist it will create one and if the file already exists it will OVERWRITE it. This argument is optional.
`--hashes "<a hash> <another hash>"` Inputs the hashes via command line. The hashes must be between a double quotation marks and separeted by spaces.
`--dictionary "<a word> <another word>"` Input the wordlist via command line. The words must be between a double quotation marks and separeted by spaces. Notice that if the word contain space, please put it inside a .txt file and use the `--fdic` parameter.
`--rmduplicate` This may improve the speed of the script by removing duplicated values in the hashes and words.
`--rmnotfoundmsg` This prevents showing messages when not founding the passwords.
`--rmanymessage` This prevents showing any messages related to found passwords at all.

##### Examples Usage
`./dictionary_attack.py --fhashes hashes.txt --fdic dictionary.txt` It will try to guess the hashes from the file hashes.txt with the words of the dictionary.txt .

`./dictionary_attack.py --fhashes hashes.txt --dic dictionary.txt --hashes "202cb962ac59075b964b07152d234b70" --dic "123 abc" --foutpass output.txt` It does the same of the previous example plus add a inline hash and dic. It also chooses a output file that will write the passwords that contain the hashes.

`./dictionary_attack.py --fhashes hashes.txt --fdic "foo bar baz foo foo" --rmduplicate` It will consider only once the *foo* value. Notice that if the file hashes contains repeated words it will consider once too.

`./dictionary_attack.py --fhashes hashes.txt --fdic dictionary.txt --rmnotfoundmsg` It will not print when it does not find a password.

``./dictionary_attack.py --fhashes hashes.txt --fdic dictionary.txt` --rmanymessage` It will not print any message related to found passwords at all.

#### Hints
If you are using special characteres be aware that they won't be properly written in an output file. In this case you can use the bash command `>` to write the output in a file instead using the `--foutpass` like `./dictionary_attack.py --fhashes hashes.txt --fdic dictionary.txt > output.txt`. Notice that doing so you should not use the parameter `--rmanymessage` once it will not print anything about found passwords.

As you can see in the examples, there is no problem adding both command line and files to hashes and dictionaries.
