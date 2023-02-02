# Scattered Light Imaging Method
Explicação dos códigos e imagens geradas sobre o Scattered Light Imaging Method (SLIM) em amostras de saliva artificial.    
    
Neste repositório você encontrará os códigos e imagens utilizadas durante o meu TCC 1 (rotina de teste) e TCC 2 (rotina em amostras salivares).  
    
Para mais informações sobre o trabalho, acesse: https://repositorio.unifesp.br/handle/11600/66726;jsessionid=81E168715F6E5A88D8842C58705A0632   
Para mais informações sobre a apostila (em construção), acesse: https://docs.google.com/document/d/1PwrZZGMXbI_3OzM1R5Hn5g0BxqBqZNsVeMty8_Og4BA/edit?usp=sharing    

## Scattered Light Imaging Method (SLIM)
O SLIM é um método de imageamento que se baseia no espalhamento da luz, para isto, utilizamos um laser de Nd-YAG de 532 nm de comprimento de onda em amostras de saliva artificial. No caso, a amostra de saliva é o meio espalhador da figura e as imagens obtidas pela câmera CCD (Charge-Coupled-Device) foram analisadas.
<p align="center">
<img src = "https://user-images.githubusercontent.com/86500603/216165731-ea7f8e60-277b-4f55-9fab-3862d22495e1.png" height = 250>
</p>
Para mais informações sobre o SLIM, acesse: https://www.somos.unifesp.br/professor/kelly-cristina-jorge-sakamoto    

## Seccionamentos Vertical e Horizontal
O seccionamento da imagem é de grande interesse para focalizarmos a propagação do feixe de luz apenas na região dentro da cubeta, onde a amostra foi inserida.
À esquerda, temos uma imagem do SLIM sem processamento algum. Enquanto que, à direita, temos uma imagem do SLIM exemplificando a região de seccionamento de interesse.    
<p align="center">
<img src = "https://user-images.githubusercontent.com/86500603/216170955-3fe1988f-4233-4ca4-95b8-b7f872b5d9c6.png" height = 250>
<img src = "https://user-images.githubusercontent.com/86500603/216170980-a322ea2b-2887-486e-8d45-ac29ec2ebf3b.png" height = 250>
</p>

Para plotar a imagem à esquerda, o seguinte código foi utilizado:
<p align="center">
<img src = "https://user-images.githubusercontent.com/86500603/216171739-ec1196b5-0ba0-4843-ba69-2e2a627338ef.png" width = 300>
</p>
Na linha 25, são definidos os parâmetros de figsize e dpi, responsáveis pelas dimensões e resolução da imagem. Estes parâmetros são importantes para definir o tamanho e qualidade das imagens geradas. O parâmetro cmap foi mantido como default ('viridis', no caso), resultando em uma imagem com tons de roxo. Para mais informações de mapas de cores, acesse: https://matplotlib.org/stable/tutorials/colors/colormaps.html

## Média das imagens
Antes de entrar nas rotinas de seccionamento, foi realizada uma média das imagens do SLIM. O uso da média faz com que a distribuição de energia se torne mais uniforme ao longo do eixo de propagação e também faz com que o ruído presente na imagem seja atenuado.
    
À esquerda, temos uma imagem do SLIM sem processamento algum. Enquanto que, à direita, temos uma imagem da média de 15 imagens de SLIM.
<p align="center">
<img src = "https://user-images.githubusercontent.com/86500603/216173149-4f711d71-3247-4de7-99a8-c1d554b4beb3.png" height = 250>
<img src = "https://user-images.githubusercontent.com/86500603/216173172-17b6345f-3761-4862-9191-d5099ad7cd66.png" height = 250>
</p>

Para plotar a imagem à direita, o seguinte código foi utilizado:
<p align="center">
<img src = "https://user-images.githubusercontent.com/86500603/216173760-7597de21-b348-4916-8c45-35f313fed6ee.png" width = 600>
</p>
Este trecho é interessante para a leitura de múltiplas imagens, onde cada imagem lida é armazenada dentro de um dicionário com chaves do tipo "img1", "img2", etc. O vetor de tags, definido na linha 16, permite a iteração da leitura seguindo o formato do nome das imagens. Este vetor é importante para o caso em que algumas imagens são descartadas ou não utilizadas na análise, no nosso caso as imagens 4, 10, 12, 14 e 19 não foram utilizadas, então um laço for comum não seria capaz de realizar esta iteração de leitura.    
<br><br>
A média das imagens foi calculada através da soma acumulada das imagens dentro da matriz vazia soma_imgs, sendo esta dividida pelo número de elementos (15), arredondada e posteriormente armazenada na matriz med_imgs (linha 30). Nas linhas 31 e 32 são criados dois vetores linhas com a soma dos elementos nos respectivos eixos, alterando o parâmetro axis que define o sentido da soma da matriz. Nas linhas 33 e 34 são criados dois vetores linhas para realizarmos os plots com a função scatter (dispersão) da biblioteca matplotlib.
<br><br>

## Seccionamento Vertical
À esquerda, temos uma soma das colunas de uma imagem de SLIM. Enquanto que, à direita, temos a soma das colunas da média de 15 imagens de SLIM.
<p align="center">
<img src = "https://user-images.githubusercontent.com/86500603/216178273-64b6b098-0292-458b-a475-0fe3550ac7b9.png" height = 300>
<img src = "https://user-images.githubusercontent.com/86500603/216178519-f12f455b-7415-46f3-a43b-a042e7e128c3.png" height = 300>
</p>
Comparando as imagens, podemos observar que a distribuição da energia é muito mais espalhada na imagem à esquerda, enquanto que à direita os pontos estão mais concentrados e mais bem distribuídos. Os pequenos picos presentes nas áreas fora da demarcação pontilhada são causados pela reflexão da luz, causadas pelas paredes da cubeta.
<br><br>
As demarcações MA e MB foram escolhidas após inspeção visual, assim delimitando as posições em que o Seccionamento Vertical limitaria o feixe para uma região dentro da cubeta. À esquerda, podemos observar a soma das colunas da média de 15 imagens de SLIM. Enquanto que, à direita, podemos observar a região de corte na imagem média das 15 imagens de SLIM.<br><br>
<p align="center">
<img src = "https://user-images.githubusercontent.com/86500603/216178519-f12f455b-7415-46f3-a43b-a042e7e128c3.png" height = 300>
<img src = "https://user-images.githubusercontent.com/86500603/216183185-fcf4c212-21c4-4a52-9b07-f15337b8aae9.png" height = 300>
</p>
<br>
Ao final do procedimento de , obtivemos a seguinte imagem:
<br><br>
<p align="center">
<img src = "https://user-images.githubusercontent.com/86500603/216200654-0cf875f3-977c-4c17-a7d8-e6f836bd5f86.png" height = 300>
</p>

## Seccionamento Horizontal
Dando sequência ao Seccionamento Vertical, temos o Seccionamento Horizontal. Para isto, a lógica é similar ao seccionamento realizado anteriormente, apenas realizando a inversão do eixo de soma (antes somamos os elementos fixando as colunas, agora somaremos os elementos fixando as linhas).<br><br>
À esquerda, temos o Seccionamento Vertical da média das imagens. Enquanto que, à direita, temos a soma das linhas da média das imagens.
<p align="center">
<img src = "https://user-images.githubusercontent.com/86500603/216213263-87008492-23e5-4fe0-8410-649c8709ece7.png" height = 300>
<img src = "https://user-images.githubusercontent.com/86500603/216213639-fd242340-2273-4b73-be62-57daeb1a6d3e.png" height = 300>
</p>
<br>
Com isso, é possível visualizarmos o centro do feixe de laser, indicado com o pontilhado em rosa. Além disso, podemos também determinar a região de Seccionamento Horizontal, MD, que neste caso foi também determinada após inspeção visual.
<br>

## Seccionamento Vertical e Horizontal
Com isso, temos bem definidos os nossos marcadores MA, MB e MD, obtidos através da média das imagens. Agora, precisamos aplicar os cortes em nossas imagens, seguindo a seguinte rotina:
<p align="center">
<img src = "https://user-images.githubusercontent.com/86500603/216229361-93c3bf83-7576-426a-9d87-67c6126072dd.png" height = 250>
</p>
<br>
Nas linhas 102 a 105, temos o Seccionamento na Vertical, armazenando os dados no dicionário vert_imgs. Em seguida, nas linhas 113 a 116, temos o Seccionamento na Horizontal, aplicando o Seccionamento Horizontal após o Seccionamento Vertical, armazenando os dados no dicionário vert_hor_imgs.
<br><br>
Por fim, podemos visualizar os efeitos dos Seccionamentos nas imagens individuais, à esquerda, e na imagem das médias, à direita, abaixo:
<br>
<p align="center">
<img src = "https://user-images.githubusercontent.com/86500603/216230791-6dbf5308-69e4-439a-88ab-337c61438597.png" height = 300>
<img src = "https://user-images.githubusercontent.com/86500603/216230851-bcdbab14-1dae-4991-a341-602d3459157e.png" height = 300>
</p>

## Determinação da potência em função da distância de propagação dentro da amostra
Agora que temos as imagens seccionadas, podemos determinar a função de potência em função da distância de propagação dentro da amostra. Para isto, iremos realizar uma soma dos elementos em função das colunas, de forma similar à etapa em que realizamos o Seccionamento na Vertical.
<br><br>
À esquerda, temos a soma dos elementos em função das colunas. Podemos observar a presença de um pico de intensidade próximo dos 75 pixels no eixo das abscissas. O pico de intensidade, denotado como "calombo", ocorre devido a presença de outros fenômenos ópticos somados ao espalhamento da luz. Como esta rotina inicial se trata da análise exclusiva do espalhamento, foi realizado um Seccionamento na Vertical na demarcação em vermelho, observada na figura à direita.
<p align="center">
<img src = "https://user-images.githubusercontent.com/86500603/216240301-7ef94db5-448b-4b53-965d-f81c691bc78d.png" height = 300>
<img src = "https://user-images.githubusercontent.com/86500603/216240332-984bc0da-1006-4d40-9e4a-cd65b0a55c0d.png" height = 300>
</p>
<br>
Em seguida, foi realizada uma conversão da escala de pixels para mm do eixo das abscissas. Com esta conversão, foi realizado um ajuste exponencial dos dados experimentais, utilizando a função curve_fit() da biblioteca scipy.optimize, disponível em: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html
<br><br>
À esquerda, temos o gráfico com remoção do "calombo". À direita, temos o gráfico com os dados experimentais e os dados ajustados com uma única exponencial.
<br>
<p align="center">
<img src = "https://user-images.githubusercontent.com/86500603/216241734-c9bc74f6-b884-4272-a66d-9159a7ffe9b0.png" height = 300>
<img src = "https://user-images.githubusercontent.com/86500603/216241767-e61478ca-0f53-4b51-a4bc-82d8850fbcb6.png" height = 300>
</p>
<br>
Este ajuste tem como objetivo descrever o decaimento da potência em função da propagação do feixe de laser, ou seja, conforme o laser se propaga na amostra, parte de sua potência é dispersada, gerando um coeficiente de dispersão/extinção, alfa. Além disso, podemos observar que o ajuste da função não é exato aos dados experimentais, configurando um subajuste da curva. Este subajuste poderia ser corrigido de duas formas: ajustando o seccionamento vertical para atenuar as intensas variações nos extremos ou ajustando a função de ajuste, potencialmente adicionando uma soma de exponenciais para melhor descrever os dados experimentais como uma decomposição de duas exponenciais.
<br><br>

No código abaixo, podemos ver os valores que melhor otimizam a função input (linhas 176 e 177) aos dados experimentais. A função input é comparada iterativamente aos dados experimentais através de um chute inicial ("initial guess") dos valores da função de ajuste, visando minimizar o erro a cada iteração. Na linha 181, obtemos os parâmetros que melhor moldam a função aos dados experimentais. Na linha 182 obtemos a matriz de covariância destes parâmetros que minimizam o erro. Com os parâmetros, é possivel estimar o valor da potência em função do eixo das abscissas, assim gerando a curva de ajuste destacada em vermelho.
<br>
<p align="center">
<img src = "https://user-images.githubusercontent.com/86500603/216242650-fba13559-b201-4cb2-993e-6a70f4aedc7e.png" height = 300>
</p>



