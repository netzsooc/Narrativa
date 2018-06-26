import pathlib
import json
from collections import defaultdict
import numpy as np

RESULTS_DIR = 'Results/dual'
UTILES_DIR = [str((i + 1) * 10) for i in range(5)]
THETA_FILE = 'final.theta'
FILE_DICT_FILE = 'listado.lista'
N_SENTI = 2

for num_dir in UTILES_DIR:
    work_dir = pathlib.Path(RESULTS_DIR, num_dir)
    theta = pathlib.Path(work_dir, THETA_FILE)
    dict_file = pathlib.Path(work_dir, FILE_DICT_FILE)
    archivos = [mi_linea.strip() for mi_linea in open(dict_file)]
    clusters_file = pathlib.Path(work_dir, 'clusters.clst')
    
    datos = defaultdict(list)
    is_titulo = False
    block_size = N_SENTI + 1
    with  open(theta) as f:
        for i, linea in  enumerate(f):
            linea = linea.strip()
            is_titulo = (i % block_size) == 0
            if is_titulo:
                titulo = int(linea.split()[-1])
                titulo = archivos[titulo]
            else:
                linea = linea.split()
                puntos = [np.float(x) for x in linea]
                datos[titulo].append(puntos)


    datos = dict(datos)
    clusters = defaultdict(list)
    llaves = defaultdict(lambda: len(llaves))
    for k, v in datos.items():
        datos[k] = np.array(v, dtype=float)
        v = datos[k]
        indice = np.unravel_index(v.argmax(), v.shape)
        llave = llaves[indice]
        clusters[llave].append(k)


    print(clusters.keys()) 
    with open(clusters_file, 'w', encoding='utf8') as f:
        json.dump(clusters, f)
        f.write('\n')

