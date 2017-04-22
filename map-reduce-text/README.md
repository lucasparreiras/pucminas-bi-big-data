# Curso BI - Big Data - MapReduce

## Exercicio 1

Um conjunto de comentários sobre os produtos da sua empresa foi disponibilizado (textos em inglês). Todos eles são comentários positivos sobres os produtos. O seu gerente solicitou quevocê prepare uma solução que possa atender os seguinte requisitos:

I. Armazenar os textos e extrair 15 palavras chaves que são mais citadas pelos clientes;
II. Sua companhia possui 4 milhões de clientes e há uma interação com estes clientes pelo menos uma vez por mês;
III. Para cada mês deve haver uma atualização nas palavras ;
IV. Em média um cliente interage com a companhia 1 vez por mês; Cada interação gera um arquivo texto a partir do sistema fonte de informação que armazena este dado;
V. Algumas palavras deve ser descartadas: 'by', 'above', 'all', 'none', 'nobody'......

Sua missão é fazer uma prova de conceito para o seu gerente. Ele ouviu falar de processamento paralelo e leu um artigo na 'Computer magazine' falando sobre o movimento NoSQL: quer entender no cenário da empresa como isto poderia funcionar. Ele já solicitou um extração de 1000 arquivos sobre os comentário dos clientes. Em uma reunião foi definido que você deve entregar um exemplo funcionando amanhã.
Você deve então:

a- Usar uma implementação simples e rápida;
b- Permitir que isto seja executada em 50 máquinas na empresa;
c- No final gerar um arquivo com a contagem das palavras;