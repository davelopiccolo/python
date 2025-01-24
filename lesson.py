import string
import random 


values = string.digits
letters = string.ascii_letters
available = values + letters

def create_pass():
    while True:
        try:
            pass_len = int(input("Lenght of the Password? Numbers Only: "))
            if pass_len < 8:
                print("It has to be more than 8 characters.")
                pass
            else:
                break
        
        except ValueError:
            print("Only digits.")
            pass
    
    password = "".join(random.choice(available) for _ in range(pass_len))
        
    return password

print(create_pass())
    
    

