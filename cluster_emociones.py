import pathlib
#import numpy as np

RESULTS_DIR = 'Results/dual'
PI_FILE = 'final.pi'
TOPICS = ['1', '10', '20', '30', '40', '50']
NSENT = 2
OUT_DIR = pathlib.Path(RESULTS_DIR, 'Clusterado')

DATA_FILES = [pathlib.Path(RESULTS_DIR, topic, PI_FILE) for topic in TOPICS]

def main():
    for numero, archivo in enumerate(DATA_FILES):
        out_file = pathlib.Path(OUT_DIR, '{}.txt'.format(numero))
        print(archivo)
        with open(archivo) as f:
            clusters = clusteriza(f)
        
        with open(out_file, 'w', encoding='utf8') as f:
            for i in range(NSENT):
                print("En el cluster {} quedaron agrupados ".format(i)\
                    + "los siguientes títulos: ", file=f)
                for titulo in clusters[i]:
                    print(titulo, file=f)
                print('\n\n\n', file=f)

def clusteriza(archivo):
    clusters = {}

    for linea in archivo:
        linea = linea.split()
        _, doc_title, sents = linea[0], linea[1], linea[2:]
        sents = [float(x) for x in sents]
        llave = sents.index(max(sents))
        clusters.setdefault(llave, [])
        clusters[llave].append(doc_title)

    return clusters

if __name__ == '__main__':
    main()
