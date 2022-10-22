# PythonWorkshopHS
Slot Machine:
1. Quando iniciada pergunta ao utilizador quantos créditos quer depositar;

2. Antes de cada rodada pergunta ao utilizador se quer parar de jogar;

3. Se a decisao for para continuar pergunta quantos créditos vão ser
apostados, se não houver créditos suficientes o jogador é informado e repete-se a pergunta;

4. Uma Rodada consiste em gerar 3 simbolos de um conjunto de 7 símbolos ("#", "$", "%", "&", "@", "£", "€");

5. Os simbolos têm as seguintes probabilidades:
#: 50/156; $: 40/156; %:30/156; &: 20/156; @: 10/156; £: 5/156; €: 1/156;

6. Se os 3 símbolos forem iguais então o utilizador ganha créditos em função da sua aposta e do simbolo que aposta:
#: 5 * aposta; $: 10 * aposta; %: 20 * aposta; &: 70 * aposta; @: 200 * aposta; £: 1000 * aposta; €: 100_000 * aposta;

7. Se o utilizador ficar sem créditos acaba o programa
