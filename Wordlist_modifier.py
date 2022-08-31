"""
Program: Wordlist_modifier.py
Author: M4773L
Date: 31/08/2022
Description: A simple program to append or prepend a string to all words contained in a wordlist.
"""

from argparse import ArgumentParser
import os.path

# Default values to be used for a default output file
CURRENT_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
DEFAULT_OUTFILE = os.path.join(CURRENT_DIRECTORY, "modified_wordlist.txt")

parser = ArgumentParser()
parser.add_argument("-M", "--mode", required=True, type=str, help="append (A) or prepend (B)")
parser.add_argument("-S", "--string", required=True, type=str, help="String to add to current words")
parser.add_argument("-W", "--wordlist", required=True, type=str, help="Wordlist containing words to modify")
parser.add_argument("-O", "--outfile", default=DEFAULT_OUTFILE, type=str, help="Location to save modified wordlist")
args = parser.parse_args()


def read_current_wordlist(wordlist_file):

    try:
        print(f"Reading wordlist file: {wordlist_file}\n")
        with open(wordlist_file, "r") as in_file:
            wordlist = in_file.read().splitlines()
            in_file.close()

        return wordlist

    except FileNotFoundError as e:
        print(f"\nError: {e}")
        exit()


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

    elif mode == "PREPEND":
        new_words = []
        for word in words:

            new_word = str_to_add + word
            new_words.append(new_word)

        return new_words


def write_wordlist(outfile, wordlist):

    print(f"\nWriting: {len(wordlist)} words to: {outfile}")
    try:
        with open(outfile, "w", encoding="utf-8") as out_file:
            out_file.write("\n".join(wordlist))
            out_file.close()

        print("Modified wordlist written successfully! \n")

    except PermissionError as e:
        print(f"Error: There was an issue writing the modified wordlist to your specified file: {e}")
        exit()


def main():

    print("\n---> Wordlist Modifier - Append or Prepend a string to an existing wordlist <---\n")
    wordlist_file = args.wordlist
    wordlist = read_current_wordlist(wordlist_file)

    # Print 5 Entries in the list as an example
    print("Before:")
    for word in wordlist[:5]:
        print(f"\t{word}")

    if args.mode.lower() == "append" or args.mode.upper() == "A":
        modified_words = modify_words("APPEND", wordlist, args.string)

    elif args.mode.lower() == "prepend" or args.mode.upper() == "P":
        modified_words = modify_words("PREPEND", wordlist, args.string)

    else:
        print(f"Error: Check your mode: {args.mode}")
        exit()

    # Print 5 Entries in the new list as an example
    print("After:")
    for word in modified_words[:5]:
        print(f"\t{word}")

    write_wordlist(args.outfile, modified_words)
    exit()


if __name__ == "__main__":

    try:
        main()

    except Exception as e:
        print(f"Error: {e}")
        exit()
