import sys
from nltk import word_tokenize, pos_tag, ne_chunk
text = sys.argv[1]
print('== POS Tagged: ')
print(pos_tag(word_tokenize(text)))
print('== ... and Chunked: ')
print(ne_chunk(pos_tag(word_tokenize(text))))