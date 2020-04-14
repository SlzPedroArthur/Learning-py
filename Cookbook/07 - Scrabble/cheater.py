import sys
import scrabble

if __name__ == "__main__":
   if len(sis.argv) < 2:
      print('Usage:scrabble.py [RACK[]')
      sys.exit(1)

      rack = list(sys.argv[1].lower())
      valid_words = []

      for word in scrabble.wordlist:
         available_letters = rack[:]

         valid = True
         for letter in word.lower():
            if letter not in available_letters:
               valid = False
               break
            available_letters.remove(letter)
         
         if valid:
            score = 0
            for letter in word:
               score = score + scrabble.scores[letter]
               valid_words.append((score,word))

      for play in srted(valid_words):
         print('%d %s' % (play[0], play[1]))