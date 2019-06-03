# TRABALHO - CÁLCULO NÚMERICO
## **Marcos Vinicius Freitas Pinto - 476644 - Universidade Federal do Ceará**

- **Descrição do Problema: http://prntscr.com/nvzdeu**

Conhecendo-se o valor de um parâmetro a fornecido, as amplitudes de deslocamentos de vários pêndulos são
dadas pela expressão a*d, onde d1, d2,..., dn são os deslocamentos dos pêndulos. Cada um dos deslocamentos
pode ser calculado através da solução de um sistema linear Cd = v, que pode ser resolvido pela regra de
Cramer, onde cada deslocamento é dado por di = detCi/detC onde detC é o determinante da matriz dos
coeficientes C e detCi é o determinante da matriz obtida trocando-se a coluna i pelo vetor d dos termos
independentes. Desenvolva um sistema para calcular as amplitudes dos deslocamentos de vários pêndulos
com requisitos dados a seguir:

a) Implementar algoritmo para calcular valores de {d} pelo método de Gauss normal.

b) Implementar algoritmo para calcular valores de {d} pelo método de Gauss-Jordan.

c) Calibrar sistema usando como padrão a=1, a matriz [C] e o vetor {v} dados abaixo.

d) Fornecer quadro resposta para cada método, variando os valores de [C] e de {v}.

       10   1    1                 12
       1    10   1  = [C]    e     12  = {v}          
       1    1    10                12


Dados de entrada: n (número de pêndulos), parâmetro a, os termos de [C]nxn e os termos de {v}nx1.

Dados de saída: termos de {d}nx1 que representam os n deslocamentos d1, d2,..., dn e as amplitudes.


