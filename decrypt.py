# Secret Message Ms Course
#-------------------------
# Associate variable town with the value "Contosoville"
town = "Contosoville"
print( "Hello, "+town+"!" )

def callBeetlejuice(phrase):
    for i in range(0,3):
        print(phrase+"!")
        if (i==2):
            print("BOOM!!!!")

def lassoLetter(letter, shiftAmount):
    letterOrd = ord(letter.lower())
    shiftedOrd = letterOrd + shiftAmount
    shiftedLetter = chr(shiftedOrd)
    print('letter %s +%d --> %s' % (letter, shiftAmount, shiftedLetter))
    return shiftedLetter

callBeetlejuice("Beetlejuice")
print('lassoLetter: ' + lassoLetter('A',2))

#test mod
print('*** test mod ***')
three_two = 3 % 2
eleven_four = 11 % 4 
five_ten = 5 % 10

print(three_two)
print(eleven_four)
print(five_ten)

#decrypt function
def decrypt(letter, shiftAmount):
    A_ASCII = ord('a')
    ALPHABET_SIZE = 26
    letterAscii = ord(letter.lower())
    return chr(A_ASCII + (((letterAscii  - A_ASCII) + shiftAmount) % ALPHABET_SIZE))

print('N --> '+ decrypt('N',2))
print('p --> '+ decrypt('p',-2))