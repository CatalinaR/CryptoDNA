

from array import array

#sequence = 'CGGCA'
sequence = raw_input('Introduce cipher text:\n')
#xkey = 'TTCCG'
xkey =  raw_input('Introduce a key:\n')

def change(sequence):
    xcode = []
    for letter in sequence:
            if letter =='A':
                xcode.append(0)
            elif letter == 'T':
                xcode.append(1)
            elif letter == 'G':
                xcode.append(2)
            elif letter == 'C':
                xcode.append(3)
    return xcode
    
    
crypto_list = change(sequence)  

trans_key = change(xkey)


def xor(num1, num2, offset):
    offset = offset or 0
    return (4 - (offset + num1 + num2) % 4) % 4
    

zip_all = zip (crypto_list,trans_key)

def apply_xor(zip_all):
    crypto = []
    for (l,k) in zip_all:
        crypto.append(xor(l,k,0))
    return crypto        
            
crypto_numbers = apply_xor(zip_all)

def translate_crypto(crypto_numbers):
    xco = []
    for c in crypto_numbers:
        if c == 0:
            xco.append('A')
        elif c == 1:
            xco.append('T')
        elif c == 2:
            xco.append('G')
        elif c == 3:
            xco.append('C')
    return xco
            
text_final = ''.join(translate_crypto(crypto_numbers))

print ('Your plain text is:\n' + text_final)


