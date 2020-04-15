
import re

text_to_search = '''
absdflkhasdflkjasdhfkjahsdfksaj
ABCAKJSDHFKJSHDFKJSDFSKJDHFKJSD
1234567890

Ha HaHa

Anna
Pedro

+ - 
'''

sentence = 'Start a sentence and the bring it to an end'

#Raw strings
print(r'\tTab')

pattern = re.compile(r'abc')