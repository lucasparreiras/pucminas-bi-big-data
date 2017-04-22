# Curso BI - Big Data - MapReduce

## Exercicio 2

Neste caso vamos implementar um junção e agrupamento de duas tabelas que estão representadas por dois arquivos:
I. Vendas;
II. Filiais.

Neste caso o que se deseja é fazer um junção dos dois arquivos para que seja apresentado um resultado que seria: Código da filial ( arquivo Filial - campo1), descrição da filial ( arquivo Filial - campo2) e total de itens pedidos ( arquivo Filial – campo6);
Na verdade seria um SQL com join e um group by:

Select cod_filial, des_filial, sum(qtd_item) as total
from vendas inner join filial on(filial.cod_filial = vendas.cod_filial)
group by cod_filial, des_filial
