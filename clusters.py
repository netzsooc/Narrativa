from pathlib import Path
from collections import defaultdict

DDIR = Path('Results')
NTOPICS = Path('1')
CLASIFICADOS = Path(DDIR, NTOPICS, 'final.pi')

clusters = defaultdict(list)
with open(CLASIFICADOS) as f:
    for line in f:
        line = line.split()
        doc = line[1]
        classes = [float(x) for x in line[2:]]
        k = classes.index(max(classes))
        clusters[k+1].append(doc)

print(clusters.keys())
for i,K in clusters.items():
    print('cluster {} tiene {} docs.'.format(i, len(K)))