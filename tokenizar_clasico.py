import os
import pathlib
from collections import Counter
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

NOVELS_DIR = 'Limpios'
novelas = os.listdir(pathlib.Path(NOVELS_DIR))

sw = stopwords.words('english') + ['would', 'could', 'might', 'have', 'is',
                                   'be', 'are', 'be', 'was', 'am', 'will', 
                                   'do']
wnl = WordNetLemmatizer()
sw = set(sw)

f = open('nuevo_corpus_total.txt', 'w', encoding='utf8')

for novela in novelas:
    novela_path = pathlib.Path(NOVELS_DIR, novela)

    try:
        with open(novela_path, encoding='utf-8') as libro:
            texto = libro.read()
    except UnicodeError:
        continue

    texto = texto.replace('\n', ' ')
    while '  ' in texto:
        texto = texto.replace('  ', ' ')
    texto = texto.lower()
    nuevo_txt = ''
    palabra = ''
    for letra in texto:
    
        if letra.isalpha():
            palabra += letra
        else:
            if palabra:
                if (len(palabra) > 2) and (palabra not in sw):
                    palabra = wnl.lemmatize(palabra)
                    nuevo_txt += palabra + ' '
            palabra = ''
    nuevo_txt = nuevo_txt.strip()
    pals = nuevo_txt.split()
    conteo = Counter(pals)
    singletones = set(pal for pal in conteo if conteo[pal] == 1)
    nuevo_txt = ' '.join([pal for pal in pals if (pal not in singletones) 
                          and (len(pal) > 2)])
    f.write('{} {}\n'.format(novela, nuevo_txt))
f.close()
