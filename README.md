# TRABALHO - CÁLCULO NÚMERICO
## **Marcos Vinicius Freitas Pinto
## Curso: Bacharelado em Estatística - Universidade Federal do Ceará**
******************************************************

**Pré-requisitos:**

* Windows e Linux: Python 3.6 ou superior
******************************************************

**Execução do Programa via Terminal**

1. Windows:

   - Entre via comandos de terminal na pasta em que encontra-se os arquivos do programa. Por exemplo:
     - `cd Downloads\CalcNum_Trab_2-master`
   - Já na pasta do programa digite `py main.py`.
   - Faça os procedimentos fundamentais que é pedido no programa
   
2. Linux:
   - Entre via comandos de terminal na pasta em que encontra-se os arquivos do programa. Por exemplo:
     - `cd Downloads/CalcNum_Trab_2-master`
   - Já na pasta do programa digite `python main.py`.
   - Faça os procedimentos fundamentais que é pedido no programa
 
******************************************************

**Arquivos Necessários para Execução:**

1. No mesmo diretório da execução:
   - Arquivo nomeado como `Termos_dpd.txt` contendo os valores dos termos dependentes do sistema de equação.    Por exemplo:
   
          10x +  y  +  z   = 12                 10;1;1 
          x   + 10y +  z   = 12 --------------> 1;10;1 ------> sendo essa matriz salva no arquivo desta maneira
          x   +  y  +  10z = 12                 1;1;10  

   
   - Arquivo nomeado como `Termos_idpd.txt` contendo os valores dos termos independentes do sistema de equação. Por exemplo:
      
          10x +  y  +  z   = 12
          x   + 10y +  z   = 12 --------------> 12;12;12 ----> sendo esse vetor salva no arquivo desta maneira
          x   +  y  +  10z = 12   
          
******************************************************
**Descrição do Problema: http://prntscr.com/nvzdeu**

Conhecendo-se o valor de um `parâmetro a` fornecido, as amplitudes de deslocamentos de vários pêndulos são
dadas pela expressão `a*d`, onde `d1, d2,..., dn` são os deslocamentos dos pêndulos. Cada um dos deslocamentos
pode ser calculado através da solução de um sistema linear `Cd = v`, que pode ser resolvido pela regra de
Cramer, onde cada deslocamento é dado por `di = detC_{i}/detC` onde `detC` é o determinante da matriz dos
coeficientes `C` e `detC_{i}` é o determinante da matriz obtida trocando-se a coluna `i` pelo vetor d dos termos
independentes. Desenvolva um sistema para calcular as amplitudes dos deslocamentos de vários pêndulos
com requisitos dados a seguir:

a) Implementar algoritmo para calcular valores de `{d}` pelo método de Gauss normal.

b) Implementar algoritmo para calcular valores de `{d}` pelo método de Gauss-Jordan.

c) Calibrar sistema usando como padrão a=1, a matriz `[C]` e o vetor `{v}` dados abaixo.

d) Fornecer quadro resposta para cada método, variando os valores de `[C]` e de `{v}`.

       10   1    1                 12
       1    10   1  = [C]    e     12  = {v}          
       1    1    10                12


- Dados de entrada: `n(número de pêndulos)`, `parâmetro a`, os termos de `[C]_{nxn}` e os termos de `[v]_{nx1}.

- Dados de saída: termos de `[d]_{nx1}` que representam os `n` deslocamentos `d1, d2,..., dn` e as amplitudes.


