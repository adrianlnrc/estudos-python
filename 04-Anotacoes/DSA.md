# Big O notation
"Quão bem meu algoritmo **escala** em proporção ao input"

**O(1)** Se eu possuo um algoritmo que se receber 100 requisições consegue processar em 10 segundos e com 10000 requisições processar em 10 segundos também ele possui complexidade O(1), demorando sempre 10 segundos independente do input
**O(n)** Se eu possuo um algoritmo que para inputs pequenos é rápido e aumenta o tempo de acordo com a quantidade de input que recebe, possuindo O(n)
**O(n2)** Se eu possuo um algoritmo que escala Exponencialmente com o input, eu possuo O(n2), tendo loop dentro de loop em um input de [1,2] com loop for i in arr \ for j in arr o resultado seria 4 combinacoes 1,1 1,2 2,1 2,2
**O(Log n)** Se eu possuo um algoritmo que descarta metade de um input a cada interação, como uma busca binária, eu possuo o(log n)
**O(n log n)** Se eu possuo um algoritmo de ordenação que percorre um numero n de elementos, escalando em complexidade temporal linear

