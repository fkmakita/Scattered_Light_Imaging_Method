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
<img src = "https://user-images.githubusercontent.com/86500603/216178273-64b6b098-0292-458b-a475-0fe3550ac7b9.png" width = 350>
<img src = "https://user-images.githubusercontent.com/86500603/216178519-f12f455b-7415-46f3-a43b-a042e7e128c3.png" width = 350>
</p>
Comparando as imagens, podemos observar que a distribuição da energia é muito mais espalhada na imagem à esquerda, enquanto que à direita os pontos estão mais concentrados e mais bem distribuídos. Os pequenos picos presentes nas áreas fora da demarcação pontilhada são causados pela reflexão da luz, causadas pelas paredes da cubeta.
<br><br>
As demarcações MA e MB foram escolhidas de forma visual, assim delimitando as posições em que o Seccionamento Vertical seria realizado.



