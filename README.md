# Narrativa
Este repositorio es con el que hago los experimentos de narrativa y JST

De momento tokenicé todos los textos y los tengo en un texto por línea en el documento corpus\_total.txt

Por alguna razón desconocida, sólo se están procesando los primeros 42 documentos del corpus. Se debe revisar en corpus\_total.txt qué ocurre con los archivos subsecuentes que estorban el proceso. Se puede intentar eliminar del corpus los archivos que no puedan procesarse y buscar si existe algún problema en su codificación.

Se creó el nuevo\_corpus\_total.txt intentando mejorar la estrategia de tokenizado. Esa se encuentra en el archivo `tokenizar_clasico.py`.

## Tiempos de procesamiento de resultados
Para 6S\_50T
real    2107m35.985s
user    2104m48.213s
sys     0m3.878s

Para 6s\_40T
real    1692m26.112s
user    1690m10.326s
sys     0m5.284s

Para 6s\_30T
real    1211m6.107s
user    1209m32.557s
sys     0m2.151s

Para 6s\_20T
real    781m12.254s
user    780m4.034s
sys     0m1.781s

Para 6s\_10T
real    467m19.298s
user    466m46.718s
sys     0m0.706s

Para 6s\_1T
real    31m22.422s
user    31m20.083s
sys     0m0.296s

## Estructura diccionario de emociones
'PALABRA', 'FEAR', 'SADNESS', 'ANGER', 'SURPRISE', 'DISGUST', 'JOY'