import mincemeat
import glob
import csv
from os import path
from operator import itemgetter

CURR_PATH = path.dirname(path.realpath(__file__))

#text_files = glob.glob(CURR_PATH+'\\files\\x0003')
text_files = glob.glob(CURR_PATH+'\\files\\*')

def file_contents(file_name):
    f = open(file_name)
    try:
        return f.read()
    finally:
        f.close()

source = dict((file_name, file_contents(file_name)) for file_name in text_files)


# implementacao do metodo map
def mapfn(k, v):
    print('map ' + k)
    from stopwords import allStopWords
    for line in v.splitlines():
        for author in (line.split(':::')[1]).split('::'):
            for word in line.split(':::')[2].split():
                if author in ['Philip S. Yu','Grzegorz Rozenberg']:
                    if (((word.lower()).replace(',','')).replace('.','') not in allStopWords):
                        yield author + ':' + ((word.lower()).replace(',','')).replace('.','') , 1


# implementacao do metodo reduce
def reducefn(k, v):
    #print('reduce ' + k)
    return sum(v)


# utilizacao do mincemeat este vai simular o papel do DFS e do 'name mode'
s = mincemeat.Server()

# a fonte de dados pode ser qq objeto do tipo  dicionario
s.datasource = source
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password='changeme')

i = 0
g = csv.writer(open(CURR_PATH+'\\Grzegorz.csv', 'w'))
for k, v in sorted(results.items(), key=itemgetter(1), reverse=True):
    if k.split(':')[0] == 'Grzegorz Rozenberg' and i < 2:
        g.writerow([k.split(':')[0],k.split(':')[1], v])
        i += 1

i = 0
g = csv.writer(open(CURR_PATH+'\\Philip.csv', 'w'))
for k, v in sorted(results.items(), key=itemgetter(1), reverse=True):
    if k.split(':')[0] == 'Philip S. Yu' and i < 2:
        g.writerow([k.split(':')[0],k.split(':')[1], v])
        i += 1
