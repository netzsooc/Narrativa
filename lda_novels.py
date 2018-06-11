import os
import pathlib
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
#from nltk.tokenize.stanford import StanfordTokenizer
from nltk.tokenize import word_tokenize as tokenize
from nltk.stem import WordNetLemmatizer

def main():
    NOVELS_DIR = 'Limpios'
    novelas = os.listdir(pathlib.Path(NOVELS_DIR))

    stemmer = SnowballStemmer("english")
    lemmer = WordNetLemmatizer()
    sw = stopwords.words('english')
    corpus = open('corpus_total.txt', 'w', encoding='utf8')
    improcesables = []
    for novela in novelas:
        print('procesando {}'.format(novela))
        novela_path = pathlib.Path(NOVELS_DIR, novela)

        try:
            titulo = novela_path.stem
            with open(novela_path) as f:
                libro = f.read()
                libro = libro.lower()
                libro = libro.strip().split()
                libro = ' '.join(libro)
                tokens = (w for w in tokenize(libro) if w not in sw)
                lemas = (lemmer.lemmatize(tok).lower() for tok in tokens
                         if tok.isalpha())
                tokenizada = ' '.join(lemma for lemma in lemas).strip()
#                tokenizada = ' '.join(x for x in novel_words(f, lemmer, sw))

            corpus.write('{} {}\n'.format(titulo, tokenizada))
        except UnicodeDecodeError:
            improcesables.append(novela)
    corpus.close()
    # print(tokenizada)
    # print(improcesables)

def novel_words (novel, lemmer, sw):
    for line in novel:
        line = ' '.join(line.split()).strip()
        tokens = (w for w in tokenize(line) if w not in sw)
        nuevos = (lemmer.lemmatize(tok).lower() for tok in tokens
                  if tok.isalpha())
        yield ' '.join(nuevos)


if __name__ == '__main__':
    main()
