import sys
from nltk import word_tokenize, pos_tag, ne_chunk
text = sys.argv[1]
print(ne_chunk(pos_tag(word_tokenize(text))))