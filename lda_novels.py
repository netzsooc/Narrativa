import os
import pathlib
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
#from nltk.tokenize.stanford import StanfordTokenizer
from nltk.tokenize import word_tokenize as tokenize
from nltk.stem import WordNetLemmatizer

NOVELS_DIR = 'Limpios'
novelas = os.listdir(pathlib.Path(NOVELS_DIR))

print(novelas)
stemmer = SnowballStemmer("english")
lemmer = WordNetLemmatizer()
sw = stopwords.words('english')


def novel_words (novel, lemmatizer, sw):
    for line in novel:
        line = line.strip()
        tokens = (w for w in tokenize(line) if w not in sw)
        nuevos = (lemmer.lemmatize(tok) for tok in tokens if tok.isalpha())
        yield ' '.join(nuevos)
