import scrabble
import string

def exists_user_letters(wordlist, userLetters):
   avalaibleWords = []
   for word in wordlist:
      if userLetters in word:
         avalaibleWords.append(word)
   return avalaibleWords

#All letters that don't appear dooble
def exists_double(wordlist):
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

def has_all_vowels(word):
   vowels = 'aeiou'
   for vowel in vowels:
      if vowel not in word:
         return False
   return True

def words_with_all_vowels(wordlist):
   wordlist = []
   for word in scrabble.wordlist:
      if has_all_vowels(word):
         wordlist.appeend(word)
   return wordlist

def is_palindrom(word):
   for i in range(len(word)):
      if word[i] != word[len(word) - 1 - i]:
         return False
   return True

def palindroms_in_wordlist(wordlist):
   palindroms = []
   for word in scrabble.wordlist:
      if is_palindrom(word):
         palindroms.append(word)
   return palindroms
   
userLetters = input("Insira suas letras: ")

palindroms_in_wordlist(scrabble.wordlist)
exists_user_letters(scrabble.wordlist, userLetters)
exists_double(scrabble.wordlist)



