import string

sonnets = open('sonnets.txt').readlines()

sonnet_words = set()

def strip_punctuation(word):
   word.replace('=',' ')
   if word.find("'"):
      return word.strip(string.punctuation)
   else:
      return None

for line in sonnets:
      line_words = line.replace('-',' ').strip().split()

      if len(line_words) <= 1:
         continue

      for word in line_words:
         stripped = strip_punctuation(word)
         if stripped and len(stripped) > 1:
            sonnet_words.add(stripped.upper())

sonnet_words = list(sonnet_words)
sonnet_words.sort()
f = open('sonnet_words.txt', 'w')
