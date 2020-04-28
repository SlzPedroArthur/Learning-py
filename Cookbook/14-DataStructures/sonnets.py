import time

my_words = [elem.strip().lower() for elem in open('sonnets_words.txt', 'r').readlines()]

wordlist = [elem.strip().lower() for elem in open('wordsindex.txt', 'r').readlines()]

wordset = set(wordlist)

counter = 0

start = time.time()

for word in my_words:
   if word not in wordset:
      print(word)
      counter += 1

stop = time.time()

print('Total new words %d' % counter)
print('Time elapsed: %.1f seconds' % (stop - start))

