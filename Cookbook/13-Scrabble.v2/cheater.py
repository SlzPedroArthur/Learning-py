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
   for word in wordlist:
      if has_all_vowels(word):
         wordlist.appeend(word)
   return wordlist

def is_palindrom(word):
   if word == word[::-1]: #list(word) == list(reversed(word)):
      return True
   return False

def palindroms_in_wordlist(wordlist):
   palindroms = []
   for word in wordlist:
      if is_palindrom(word):
         palindroms.append(word)
   return palindroms

def longest_palindrom(wordlist):
   longest = ""
   for word in wordlist:
      if word == word[::-1] and len(word) > len(longest): #list(word) == list(reversed(word))
         longest = word
   return longest

def longest_word(wordlist):
   longest = ""
   for word in range(wordlist):
      if len(longest) < len(word):
         longest = word
   return longest

userLetters = input("Insira suas letras: ")

exists_user_letters(scrabble.wordlist, userLetters)
exists_double(scrabble.wordlist)

palindroms = palindroms_in_wordlist(scrabble.wordlist)
longest_word(palindroms)

