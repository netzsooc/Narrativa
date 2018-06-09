from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize.stanford import StanfordTokenizer

stemmer = SnowballStemmer("english")
tokenizer = StanfordTokenizer()
sw = stopwords.words('english')
with open("Novelas_en_formato_txt/farenheit_prepro.txt") as f:
    for line in f:
        tokens = tokenizer.tokenize(line.strip())
        nuevos = [stemmer.stem(token) for token in tokens if token not in sw]
        print(' '.join(nuevos))