#this code outputs international morse code(ITU) out of a given word

import re
word='hello world'
word=word.lower()
word=re.sub('_','-',word)

def encode(x):
    if x == 'a':return ".-"
    elif x == 'b':return "-..."
    elif x == 'c':return "-.-."
    elif x == 'd':return "-.."
    elif x == 'e':return "."
    elif x == 'f':return "..-."
    elif x == 'g':return "--."
    elif x == 'h':return "...."
    elif x == 'i':return ".."
    elif x == 'j':return ".---"
    elif x == 'k':return "-.-"
    elif x == 'l':return ".-.."
    elif x == 'm':return "--"
    elif x == 'n':return "-."
    elif x == 'o':return "---"
    elif x == 'p':return ".--."
    elif x == 'q':return "--.-"
    elif x == 'r':return ".-."
    elif x == 's':return "..."
    elif x == 't':return "-"
    elif x == 'u':return "..-"
    elif x == 'v':return "...-"
    elif x == 'w':return ".--"
    elif x == 'x':return "-..-"
    elif x == 'y':return "-.--"
    elif x == 'z':return "--.."
    elif x == '1':return ".----"
    elif x == '2':return "..---"
    elif x == '3':return "...--"
    elif x == '4':return "....-"
    elif x == '5':return "....."
    elif x == '6':return "-...."
    elif x == '7':return "--..."
    elif x == '8':return "---.."
    elif x == '9':return "----."
    elif x == '0':return "-----"
    return '/'
output=''
for x in word:
    output+=encode(x)+' '
output=re.sub(' / ','/',output)[:-1]
print(output)
