from decrypt import decrypt

def caesarcipherDecrypt(word, shift):
    decryptedWord = ''
    for letter in word:
        decryptedWord += decrypt(letter, shift)
    return decryptedWord


print('Ncevy 13 --> '+ caesarcipherDecrypt('Ncevy',13))
print('gpvsui 25 --> '+ caesarcipherDecrypt('gpvsui',25))
print('ugflgkg -18 --> '+ caesarcipherDecrypt('ugflgkg',-18))
print('wjmmf -1 --> '+ caesarcipherDecrypt('wjmmf',-1))