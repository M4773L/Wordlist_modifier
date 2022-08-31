# Modify Wordlist
Recently whilst enumerating a box on a popular CTF platform, I was required to prepend a string to the words contained within an 
existing wordlist hence why I wrote this program. It is a simple program with 2 modes of operation; Append (Add to end of word) and Prepend 
(Add to start of word). The program will read all of the words from the supplied wordlist file into a list, then iterates through each item
appending or prepending the user supplied string and then adding each modified word into a new list. The items in this new list are then 
written to an output file with utf-8 encoding.


## Usage
```
┌──(m477㉿kali)-[~/Python]
└─$ python3 Wordlist_modifier.py -h
usage: Wordlist_modifier.py [-h] -M MODE -S STRING -W WORDLIST [-O OUTFILE]

options:
  -h, --help            show this help message and exit
  -M MODE, --mode MODE  append (A) or prepend (B)
  -S STRING, --string STRING
                        String to add to current words
  -W WORDLIST, --wordlist WORDLIST
                        Wordlist containing words to modify
  -O OUTFILE, --outfile OUTFILE
                        Location to save modified wordlist
```

* Mode: Append or 'A' for Appending to words | Prepend or 'P' for Prepending to words.
* String: The string to append or prepend.
* Wordlist: The wordlist file.
* Outfile: Location to save modified words <-- Will default to modified_wordlist.txt in the scripts directory if none supplied.


```
┌──(m477㉿kali)-[~/Python]
└─$ python3 Wordlist_modifier.py -M P -S "preprod-" -W /usr/share/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -O preprod_subdomains.txt

---> Wordlist Modifier - Append or Prepend a string to existing wordlist items <---

Reading wordlist file: /usr/share/SecLists/Discovery/DNS/subdomains-top1million-5000.txt

Before:
        www
        mail
        ftp
        localhost
        webmail

Modifying words in mode: PREPEND

After:
        preprod-www
        preprod-mail
        preprod-ftp
        preprod-localhost
        preprod-webmail

Writing: 4989 words to: preprod_subdomains.txt
Modified wordlist written successfully!
```
Simple execution in prepend mode with the string 'preprod-', the program will read the a subdomain wordlist from Seclists and write the 
modified words to an outfile named 'preprod_subdomains.txt'. You can see that the program will print the first 5 items from each list to 
provide the user a preview of the modified words.

## Known Issues
When appending to a word you are unable to begin the string with a hyphen '-'; 

```
┌──(m477㉿kali)-[~/Python]
└─$ python3 Wordlist_modifier.py -M A -S "-prep" -W /usr/share/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -O preprod_subdomains.txt
usage: Wordlist_modifier.py [-h] -M MODE -S STRING -W WORDLIST [-O OUTFILE]
Wordlist_modifier.py: error: argument -S/--string: expected one argument
```

Workaround
```
def modify_words(mode, words, str_to_add):

    print(f"\nModifying words in mode: {mode}\n")

    if mode == "APPEND":
        new_words = []
        for word in words:

            # If you require a '-' hyphen between the original word and the string you wish to add, uncomment below.
            new_word = word + str_to_add
            # new_word = word + "-" + str_to_add  # <--- Uncomment this line
            new_words.append(new_word)

        return new_words
```
Navigate to the modify_words function and simply uncomment the line where it is shown. 
You may like to comment out the line above 'new_word = word + str_to_add' however, if not the script will run just fine as the variable will
simply be reassigned.