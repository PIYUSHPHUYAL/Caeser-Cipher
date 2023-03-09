"""Name:Piyush Phuyal
   Student ID:2330536
   Class Group:L4CG2(2022/23)
   College ID:np03cs4a220258@heraldcollege.edu.np"""


def welcome():
    print("Warm Welcome to Piyush's Caesar Cipher!!!")
    print("Basically, This program encrypts and decrypts text with the Caesar Cipher")


def enter_message():
    while True:
        choose = input(
            "What do you want to do? Encrypt (en) or decrypt (de)? ").upper()
        '''.uppper() method is used to convert all the characters into uppercase'''
        if choose == "EN" or choose == "DE":
            break
        else:
            print('''Incorrect Input!
Please enter "en" or "de"!''')

    while True:
        msg = input("What text do you want to "+choose+"CRYPT? ").upper()

        if msg.isalpha():
            '''Here msg.is alpha() is used to check whether the message to be encrypted or decrypted is a character or not'''
            shift = int(input("Enter the shift number from 0-25 "))
            '''The user have to provided the number to be shifted that means by how many characters to be shifted '''
            break
        print('''Opps! You gave wrong input
Please input your message in characters''')

    return (choose, msg, shift)


def encrypt(msg, shift):
    encrypted_msg = ""  # initialize empty string
    for char in msg:  # to iterate through each characters in the messasge
        if char.isalpha():  # calling isalpha method
            '''isalpha() method is used here to check if the input message provided by
            user is letter or not '''
            shifted_char = chr((ord(char) + shift - 65) % 26 +
                               65)   # using ord() function to calculate the ASCII value of the letter
            # chr()function is used to to convert ASCII value back to character
            encrypted_msg += shifted_char
        # To handle overflow modulo operatiion that is % 26 is used above
        else:
            encrypted_msg += char
    return encrypted_msg


def decrypt(msg, shift):
    decrypted_msg = ""
    for char in msg:
        if char.isalpha():
            shifted_char = chr((ord(char) - shift - 65) % 26 + 65)
            '''ord() is used to calculate ASCIII value of the provided letters whereas 
            chr() function is used to convert that ASCII value back to characters after shifting 
            modulus is used here just to handle the overflow while operation is executed'''
            decrypted_msg += shifted_char
        else:
            decrypted_msg += char
    return decrypted_msg


welcome()  # calling welcome function
while True:
    choose, msg, shift = enter_message()
    if choose == "EN":
        result = encrypt(msg, shift)
    else:
        result = decrypt(msg, shift)
    print(choose+"CRYPTED MESSAGE after " + str(shift) + " shift is " + result)
    while True:
        again = input(
            "Would you like to encrypt/decrypt message again? (y/n) ").lower()
        '''.lower() is a method used here to convert the characters into lower case
        which means that if user enter Y it converts to y'''
        if again == "y" or again == "n":
            break
        else:
            print('''Incorrect input!
please type 'y' or 'n' ''')
    if again == "n":
        print('''Thank you for using Caesar Cipher!
Have a Great Day!''')
        break
