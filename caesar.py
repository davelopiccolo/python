import string

symbols = string.ascii_lowercase

def main():
    while True:
        choice = input("Do you want to cypher or decypher? C // D , press 0 to Exit ").capitalize()
        if choice == "D":
            decypher()
        elif choice == "C":
            cypher()
        elif choice == "0":
            print("Ok, hope we were useful")
            return
        else:
            print("please print c d or 0")
    
    
        
        
def cypher():
    message = input("What do you want to encrypt? ").lower()
    translated = []
    for letter in message:
        if letter == " ":
            translated.append(letter)
        elif letter not in symbols:
            translated.append(letter)
        else:
            for corrispondence in range(len(symbols)):
                if letter == symbols[corrispondence]:
                    cyphered = corrispondence + 3 % len(symbols)
                    translated.append(symbols[cyphered])
                
        
        
    print(''.join(translated))

def decypher():
    message = input("What do you want to decrypt? ").lower()
    translated = []
    for letter in message:
        if letter == " ":
            translated.append(letter)
        elif letter not in symbols:
            translated.append(letter)
        else:
            for corrispondence in range(len(symbols)):
                if letter == symbols[corrispondence]:
                    cyphered = corrispondence - 3 % len(symbols)
                    translated.append(symbols[cyphered])
                
        
        
    print(''.join(translated))
    

main()