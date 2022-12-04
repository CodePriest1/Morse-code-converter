# dictionary containing alphanumeric data and corresponding morse code
code = {'a': '.-',
        'b': '-...',
        'c': '-.-.',
        'd': '-..',
        'e': '.',
        'f': '..-.',
        'g': '--.',
        'h': '....',
        'i': '..',
        'j': '.---',
        'k': '-.-',
        'l': '.-..',
        'm': '--',
        'n': '-.',
        'o': '---',
        'p': '.--.',
        'q': '--.-',
        'r': '.-.',
        's': '...',
        't': '-',
        'u': '..-',
        'v': '...-',
        'w': '.--',
        'x': '-..-',
        'y': '-.--',
        'z': '--..',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '.': '.-.-.-',
        ',': '--..--',
        ':': '---...',
        '?': '..--..',
        "'": '.----.',
        '-': '-....-',
        '/': '-..-.',
        ')': '-.--.-',
        '(': '-.--.',
        '"': '.-..-.',
        '@': '.--.-.',
        '=': '-...-',
        '+': '.-.-.',
        '!': '-.-.--',
        '&': '.-...',
        }

# function to encrypt text or message
def encrypt():
    cipher = ""
    # loop through each letter input in user
    for item in user:
        # check that each letter is not an empty string
        if item != " ":
            # check the dictionary for the corresponding morse code separating them by a SPACE
            cipher += code[item] + " "
        # check if there is a SPACE between words and separate morse code by |
        if item == " ":
            cipher += "|"
    # print out the encrypted data(Morse code)
    print(f"\nOutput:\n{cipher}")


# function to decrypt morse code
def decrypt():
    decipher = ""
    cipher_text = ""
    result = ""
    # returns a dictionary from code with the values as keys and keys as values (basically the inverse since we are
    # decrypting)
    traverse = {v: k for k, v in code.items()}
    i = 0
    # .--. .-. .. -. -.-. .
    # .--. .-. .. -. -.-. .  .. ...  .... --- -
    # loop through the encrypted data
    for item in user:
        # check that it is not an empty string and iterate them to a variable (decipher)
        if item != " ":
            i = 0
            decipher += item
        else:
            i += 1
            # to check for SPACE (i ==2 means there is double space between encrypted code)
            if i == 2:
                # we need our output to return a space if there is double space between the encrypted morse code
                cipher_text += " "
            result += decipher
            # check if result is in the reverse dictionary (traverse)
            if result in traverse:
                # add decrypted data to a variable "cipher_text"
                cipher_text += traverse[result]
                # initialise decipher and result
                decipher = ""
                result = ""
    # return output as cipher_text
    print(f"\nOutput:\n{cipher_text.upper()}")


print("Morse Code Translator")
user = input("Type your message below. This app allows you to encrypt and decrypt in Morse code. \
Alphabets or Morse code is accepted as input.\nEnter Morse code using '.' or '-', separating words or Morse code by\
 a space after every word, the encrypted code will be separated by |:\n").lower()
if user.startswith(".") or user.startswith("-"):
    decrypt()
else:
    encrypt()


