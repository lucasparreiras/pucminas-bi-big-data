import mincemeat
import glob
import csv

text_files = glob.glob('D:\\Git-repositorios\\pucminas-bi-big-data\\map-reduce-join\\*')

def file_contents(file_name):
    f = open(file_name)
    try:
        return f.read()
    finally:
        f.close()

source = dict((file_name, file_contents(file_name))for file_name in text_files)


# implementacao do metodo map
def mapfn(k, v):
    print 'map' + k
    for line in v.splitlines():
        if k == 'D:\\Git-repositorios\\pucminas-bi-big-data\\map-reduce-join\\2.2-vendas.csv':
            yield line.split(';')[0], 'Vendas' + ':' + line.split(';')[5]
        if k == 'D:\\Git-repositorios\\pucminas-bi-big-data\\map-reduce-join\\2.2-filiais.csv':
            yield line.split(';')[0], 'Filial' + ':' + line.split(';')[1]


# implementacao do metodo reduce

def reducefn_(k, v):
    print 'reduce' + k
    return v


# implementacao final do metodo reduce
def reducefn(k, v):
	print 'reduce' + k
	total = 0
	for index, item in enumerate(v):
		if item.split(":")[0]== 'Vendas':
			total = int(item.split(":")[1]) + total
		if item.split(":")[0] == 'Filial':
			NomeFilial = item.split(":")[1]
	L = list()
	L.append(NomeFilial + " , " + str(total))
	return L




# utilizacao do mincemeat este vai simular o papel do DFS e do 'name mode'

s = mincemeat.Server()

# a fonte de dados pode ser qq objeto do tipo  dicionario
s.datasource = source
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

w = csv.writer(open("D:\\Git-repositorios\\pucminas-bi-big-data\\map-reduce-join\\result2.csv", "w"))
for k, v in results.items():
    w.writerow([k, str(v).replace("[","").replace("]","").replace(" ","").replace(' ','')])
