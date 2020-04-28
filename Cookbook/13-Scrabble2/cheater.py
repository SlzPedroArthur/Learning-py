import scrabble
import string

def existsUserLetters(wordlist, userLetters):
   avalaibleWords = []
   for word in wordlist:
      if userLetters in word:
         avalaibleWords.append(word)
   return avalaibleWords

#All letters that don't appear dooble
def existsDouble(wordlist):
   notExists = []
   for letter in string.ascii_lowercase:
      exists = False
      for word in wordlist:
         if letter * 2 in word:
            exists = True 
            break
      if not exists: notExists.append(letter)
   #print(notExists)
   return notExists

def had_all_vowels(word):
   vowels = 'aeiou'
   for vowel in vowels:
      if vowel not in word:
         return False
   return True



userLetters = input("Insira suas letras: ")

existsUserLetters(scrabble.wordlist, userLetters)
existsDouble(scrabble.wordlist)