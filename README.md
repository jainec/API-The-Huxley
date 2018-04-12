API para o juiz online brasileiro The Huxley. Esta API gera mensagens de erros de sintaxe das linguagens C e Python mais amigáveis e compreensíveis para os programadores iniciantes que utilizam o The Huxley, assim, tais programadores conseguem entender melhor onde e qual erro ele está cometendo, recebendo dicas também de como corrigir tal erro, além de aprender mais sobre a linguagem de programação em questão.

Por exemplo, ao submeter o trecho de código abaixo no juiz online The Huxley:

   **long float t=0,a=0,b=0,c=0,d=0,x=0,y=0;
          ^**
  
o usuário recebe tal mensagem de erro:

**/Matrizes.c: In function ‘main’:
/Matrizes.c:6:8: error: both ‘long’ and ‘float’ in declaration specifiers**

Mas através desta API, o usuário passa a receber a mensagem de erro abaixo:

**Na função 'main':
Erro na linha 6
No trecho de código:
    long float t=0,a=0,b=0,c=0,d=0,x=0,y=0;
         ^
Descrição: Em C não é permitido usar 'long' e 'float' juntos para declarar variáveis. Para corrigir o erro retire o 'float' da declaração e lembre-se de que os tipos primitivos para declarar variáveis em C são: char, unsigned char, int, unsigned int, short int, unsigned short int, long int, unsigned long int, float, double e long double.**

Assim, o usuário tem uma mensagem mais clara do erro que está cometendo e dicas de como resvolver tal errro.
