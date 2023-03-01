
#%% Bibliotecas utilizadas
import matplotlib.pyplot as plt
import numpy as np
import os
import scipy.optimize as so

# Direcionamento do diretório das imagens
os.chdir(r'E:\Arquivos\TCC 2609\Imagens\Sample 6_\600 mV_7.5 GW-cm²')

#%% Cálculo de intensidade do laser em 20 imagens de SLIM
# Variáveis de manipulação
dtframe = {}
imgs = {}
soma_imgs = np.empty((614, 815))
tags = [1, 2, 3, 5, 6, 7, 8, 9, 11, 13, 15, 16, 17, 18, 20]

# Leitura das imagens e manipulação inicial
for i in range(0, len(tags), 1):
    id = str(tags[i])
    dtframe['pulso{0}'.format(tags[i])] = plt.imread('pulso_#' + id.zfill(3) + '.tif')
    imgs['img{0}'.format(tags[i])] = dtframe['pulso{0}'.format(tags[i])][:, :, 2]
    soma_imgs += imgs['img{0}'.format(tags[i])]

plt.figure(figsize = (6,4), dpi = 1600)
plt.imshow(imgs['img2'])
plt.show()

# Matriz de média das imagens
med_imgs = np.around(soma_imgs/15)
med_imgs_col = np.sum(med_imgs, axis = 0)
med_imgs_row = np.sum(med_imgs, axis = 1)
pixels = np.linspace(1, 815, 815)
pixels_row = np.linspace(1, 614, 614)

plt.figure(figsize = (6,4), dpi = 1600)
plt.imshow(med_imgs)
plt.show()

# Regiões de interesse para seccionamento vertical
MA = 291
MB = MA + 317

# Plot da soma das linhas da média das imagens
plt.figure(figsize = (6,4), dpi = 1600)
plt.scatter(pixels, med_imgs_col, marker = '.')
plt.vlines(x = MA, ymin = 0, ymax = 7500, colors = 'indianred', linestyles = 'dashdot')
plt.vlines(x = MB, ymin = 0, ymax = 7500, colors = 'indianred', linestyles = 'dashdot')
plt.ylim(1000, 6100)
plt.xlim(0, pixels[-1])
plt.legend(('Soma', 'MA: ' + str(MA) + 'px', 'MB: ' + str(MB) + 'px'))
plt.grid('on')

# Plot da soma das linhas da imagem1
plt.figure(figsize = (6,4), dpi = 1600)
plt.scatter(pixels, np.sum(imgs['img1'], axis = 0), marker = '.')
plt.vlines(x = MA, ymin = 0, ymax = 7500, colors = 'indianred', linestyles = 'dashdot')
plt.vlines(x = MB, ymin = 0, ymax = 7500, colors = 'indianred', linestyles = 'dashdot')
plt.ylim(1000, 6100)
plt.xlim(0, pixels[-1])
plt.legend(('Soma', 'MA: ' + str(MA) + 'px', 'MB: ' + str(MB) + 'px'))
plt.grid('on')

# Visualização da região pré corte vertical com demarcações MA e MB
plt.figure(figsize = (6,4), dpi = 1600)
plt.vlines(x = MA, ymin = 0, ymax = 7500, colors = 'indianred', linestyles = 'dashed')
plt.vlines(x = MB, ymin = 0, ymax = 7500, colors = 'indianred', linestyles = 'dashed')
plt.imshow(med_imgs)

# Regiões de interesse para seccionamento horizontal
MC = 106
MD = 212

# Plot da soma das colunas da média das imagens
plt.figure(figsize = (4,4), dpi = 1600)
plt.scatter(np.sum(imgs['img1'][:, 291:608], axis = 1), pixels_row, marker = '.')
plt.hlines(y = MC, xmin = -100, xmax = 18000, colors = 'red', linestyles = 'dashdot')
plt.hlines(y = MD, xmin = -100, xmax = 18000, colors = 'magenta', linestyles = 'dashed')
plt.xlim(0, 18000)
plt.ylim(614, 0)
plt.legend(('Soma', 'MC: ' + str(MC) + 'px', 'MD: ' + str(MD) + 'px'))
plt.grid('on')

# Plot da soma das colunas da média das imagens
plt.figure(figsize = (4,4), dpi = 1600)
plt.scatter(np.sum(med_imgs[:, 291:608], axis = 1), pixels_row, marker = '.')
plt.hlines(y = MC, xmin = -100, xmax = 18000, colors = 'red', linestyles = 'dashdot')
plt.hlines(y = MD, xmin = -100, xmax = 18000, colors = 'magenta', linestyles = 'dashed')
plt.xlim(0, 18000)
plt.ylim(614, 0)
plt.legend(('Soma', 'MC: ' + str(MC) + 'px', 'MD: ' + str(MD) + 'px'))
plt.grid('on')

# Visualização da região pós corte vertical
plt.figure(figsize = (6,4), dpi = 1600)
plt.hlines(y = MC, xmin = -100, xmax = 18000, colors = 'red', linestyles = 'dashdot')
plt.hlines(y = MD, xmin = -100, xmax = 18000, colors = 'magenta', linestyles = 'dashed')
plt.imshow(med_imgs[:,291:608])


# Seccionamento vertical das imagens
vert_imgs = {}
for i in range(0, len(tags), 1):
    id = str(tags[i])
    vert_imgs['vert_img{0}'.format(tags[i])] = imgs['img{0}'.format(tags[i])][:, MA:MB]

# Visualização do seccionamento vertical da Img1
plt.figure(figsize = (6,4), dpi = 1600)
plt.imshow(vert_imgs['vert_img1'])
plt.axis('on')

# Seccionamento horizontal das imagens
vert_hor_imgs = {}
for i in range(0, len(tags), 1):
    id = str(tags[i])
    vert_hor_imgs['vert_hor_img{0}'.format(tags[i])] = vert_imgs['vert_img{0}'.format(tags[i])][0 : MD,:]


# Visualização do seccionamento vertical e horizontal da Img1
plt.figure(figsize = (6,4), dpi = 1600)
plt.imshow(vert_hor_imgs['vert_hor_img1'])
plt.xlabel('z (pixels)')
plt.ylabel('y (pixels)')
plt.axis('on')

# Visualização do seccionamento vertical e horizontal da média das imagens
plt.figure(figsize = (6,4), dpi = 1600)
plt.imshow(med_imgs[0:212, 291:608])
plt.xlabel('z (pixels)')
plt.ylabel('y (pixels)')
plt.axis('on')


# Corte das imagens entre 0 e MD, MA e MB
med_img_secc = med_imgs[0:MD, MA:MB]

# Soma das potências das linhas em função das colunas
med_pot = np.sum(med_img_secc, axis = 0)
linha = np.linspace(1, 317, 317)


# Visualização da soma das potências
plt.figure(figsize = (4,4), dpi = 1600)
plt.grid('on')
plt.xlim(0, 317)
plt.ylim(700, 4500)
plt.ylabel('Potência')
plt.xlabel('z (pixels)')
plt.scatter(linha, med_pot, marker = '.')


# Visualização da soma das potências com destaque para o Calombo
plt.figure(figsize = (4,4), dpi = 1600)
plt.grid('on')
plt.xlim(0, 317) # Região de corte do Calombo
plt.ylim(700, 4500)
plt.vlines(x = 75, ymin = 0, ymax = 6000, colors = 'red', linestyles = 'dashed')
plt.ylabel('Potência')
plt.xlabel('z (pixels)')
plt.scatter(linha, med_pot, marker = '.')

# Corte do gráfico de potência após a região do Calombo e conversão de escala px -> mm
eixo_z_mm = np.linspace(0, 10*(317-75)/317, 317-75)
dados_pot_75 = med_pot[75:]

# Visualização gráfica da remoção do calombo
plt.figure(figsize = (4,4), dpi = 1600)
plt.grid('on')
plt.xlim(0, max(eixo_z_mm))
plt.ylabel('Potência')
plt.xlabel('z (mm)')
plt.scatter(eixo_z_mm, dados_pot_75, color = 'dodgerblue', marker = '.')
plt.show()

# Definição do formato da função de potência
def Pz(z, alfa, P0):
    return P0 * np.exp(-alfa * z)

# Ajuste exponencial da curva e armazenamento das variáveis para visualização
dados_fit = so.curve_fit(Pz, eixo_z_mm, dados_pot_75, full_output = True)
popt = dados_fit[0]
pcov = dados_fit[1]
alfa_fit, P0_fit = popt
dados_pot_75_fit = Pz(eixo_z_mm, alfa_fit, P0_fit)

dados_fit1 = [alfa_fit, P0_fit]

# Visualização gráfica do ajuste exponencial
plt.figure(figsize = (4,4), dpi = 1600)
plt.grid('on')
plt.xlim(0, max(eixo_z_mm))
plt.ylabel('Potência')
plt.xlabel('z (mm)')
plt.scatter(eixo_z_mm, dados_pot_75, color = 'dodgerblue', marker = '.')
plt.scatter(eixo_z_mm, dados_pot_75_fit, color = 'orangered', marker = '.')
plt.legend(('Dados Experimentais', 'Ajuste Exponencial'))
plt.show()

# Ajuste gaussiano da curva para a posição de z = 150 pixels

# CONVERTENDO A ESCALA DE PIXELS PARA MILIMETROS
# Seccionamento da média dos feixes na posição z = 150 pixels
int_z_150 = np.array(med_img_secc[:,150], dtype = float)
y_pos_z_150 = np.linspace(0, 6.84, len(int_z_150))

# Visualização da coluna selecionada
plt.figure(figsize = (6,4), dpi = 1600)
plt.vlines(x = 150, ymin = 0, ymax = 212, colors = 'r', linestyles = 'dashed')
plt.imshow(med_imgs[0:212, 291:608])
plt.xlabel('z (pixels)')
plt.ylabel('y (pixels)')
plt.axis('on')

# Definição do formato da função Gaussiana
def Iy(y, I0, y0, w, b0):
    return I0 * np.exp(-2*((y-y0)**2)/w**2) + b0

dados_fit2 = so.curve_fit(Iy, y_pos_z_150, int_z_150, full_output = True)
popt2 = dados_fit2[0]
pcov2 = dados_fit2[1]

dados_int_150_fit = Iy(y_pos_z_150, *popt2)

plt.figure(figsize = (4,4), dpi = 1600)
plt.grid('on')
plt.xlim(0, max(y_pos_z_150))
plt.ylim(0, 90)
plt.ylabel('Intensidade')
plt.xlabel('y (mm)')
plt.scatter(y_pos_z_150, int_z_150, color = 'dodgerblue', marker = '.')
plt.scatter(y_pos_z_150, dados_int_150_fit, color = 'orangered', marker = '.')
plt.legend(('Dados Experimentais', 'Ajuste Exponencial'))
plt.show()


#%% Generalização da rotina para obtenção da largura do perfil em função do eixo de propagação (w versus z)
def w_versus_z(vet_med_img_secc):
    M, N = np.shape(vet_med_img_secc[:,:])
    y_pos_z_i = np.linspace(0, 6.84, M) # eixo y para a posição z
    eixo_w_pos_z = np.linspace(0, 10.0, N) # 7.63 mm se considerar 317 - 75 = 242 pixels
    w_pos_z = np.linspace(0, 7.63, N)
    for i in range(N):
        int_z_i = np.array(vet_med_img_secc[:,i], dtype = float)
        dados_fit_i = so.curve_fit(Iy, y_pos_z_i, int_z_i, maxfev = 20000)
        w_pos_z[i] = dados_fit_i[0][2]
        print(i)
    return(eixo_w_pos_z, w_pos_z)


y_pos_z_i, w_pos_z = w_versus_z(med_img_secc)

#w_pos_z = w_pos_z*1000


plt.figure(figsize = (4,4), dpi = 1600)
plt.grid('on')
plt.xlim(0, max(y_pos_z_i))
plt.scatter(y_pos_z_i, w_pos_z, marker = '.')
plt.xlabel('Eixo z (mm)')
plt.ylabel('w(z) (mm)')
plt.axvline(x = 10*75/317, color = 'red', linestyle = '--')
plt.axvline(x = 10*150/317, color = 'orange', linestyle = '--')
plt.show()


#%% Análise das amostras de saliva

# Bibliotecas
import matplotlib.pyplot as plt
import numpy as np
import os
import scipy.optimize as so

# Direcionamento do diretório das imagens
os.chdir(r'E:\Arquivos\TCC 2609\Slim\Fabio')

dtframe = {}
array = []
tags = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
soma_imgs = np.empty((1000, 1000))

for i in range(0, len(tags), 1):
    id = str(tags[i])
    string = "salivacomfiltroH00000" + id + ".cma"
    
    try:
        f = open(string)
        lines = f.readlines()
    finally:
        f.close()
    
    for j in range(len(lines)):
        lines[j] = lines[j].split(',')

    array = np.array(lines)
    array = array[:,:1000]
    array = np.array(array, dtype = float)
    
    dtframe['pulso{0}'.format(tags[i])] = array

    soma_imgs += array

med_imgs = np.around(soma_imgs/len(tags), 6)

# Média das 10 imagens
plt.figure(figsize = (4,4), dpi = 1600)
plt.xlabel('z (pixels)')
plt.ylabel('y (pixels)')
plt.imshow(med_imgs, cmap = 'gray')

# Soma dos elementos ao longo de y
med_imgs_lin = np.sum(med_imgs, axis = 1)
eixo_y_mm = np.linspace(0, 999, 1000)

plt.figure(figsize = (5,4), dpi = 1600)
plt.axhline(eixo_y_mm[480], color = 'red', linestyle = '--')
plt.axhline(eixo_y_mm[400], color = 'blue', linestyle = '--')
plt.axhline(eixo_y_mm[560], color = 'blue', linestyle = '--')
plt.ylim(0, 1000)
plt.xlabel('Potência')
plt.ylabel('y (pixels)')
plt.scatter(med_imgs_lin, eixo_y_mm, marker = '.')
plt.xlim(0)
plt.grid('on')

med_imgs_sec_hor = med_imgs[400:560,:]

eixo_y_sec = eixo_y_mm[400:560]
plt.figure(figsize = (4,4), dpi = 1600)
plt.xlabel('z (pixels)')
plt.ylabel('y (pixels)')
plt.imshow(med_imgs[400:560,:], cmap = 'gray')


plt.scatter(eixo_y_sec, med_imgs_sec_hor)
         
plt.imshow(med_imgs_sec_hor, cmap = 'gray')


med_imgs_col = np.sum(med_imgs_sec_hor, axis = 1)
eixo_y_mm = np.linspace(400, 560, 160)

plt.figure(figsize = (4,4), dpi = 1600)
plt.axhline(eixo_y_mm[80], color = 'red', linestyle = '--')
plt.axhline(eixo_y_mm[0], color = 'blue', linestyle = '--')
plt.axhline(eixo_y_mm[159], color = 'blue', linestyle = '--')
plt.scatter(med_imgs_col, eixo_y_mm, marker = '.')
plt.grid('on')

# Soma dos elementos ao longo de Z
med_imgs_lin = np.sum(med_imgs_sec_hor, axis = 0)
eixo_z_mm = np.linspace(1, 1000, 1000)

plt.figure(figsize = (4,4), dpi = 1600)
plt.scatter(eixo_z_mm, med_imgs_lin, marker = '.')
plt.xlim((min(eixo_z_mm), max(eixo_z_mm)))
plt.xlabel('z (pixels)')
plt.ylabel('Potência')
plt.grid('on')


#Ajuste do gráfico de potência
# Definição do formato da função de potência
def Pz(z, alfa, P0):
    return P0 * np.exp(-alfa * z)

med_imgs_lin = med_imgs_lin[:600]
eixo_z_mm = eixo_z_mm[:600]

# Ajuste exponencial da curva e armazenamento das variáveis para visualização
dados_fit = so.curve_fit(Pz, eixo_z_mm, med_imgs_lin, full_output = True)
popt = dados_fit[0]
pcov = dados_fit[1]
alfa_fit, P0_fit = popt
dados_pot_75_fit = Pz(eixo_z_mm, alfa_fit, P0_fit)

dados_fit1 = [alfa_fit, P0_fit]

# Visualização gráfica do ajuste exponencial
plt.figure(figsize = (4,4), dpi = 1600)
plt.grid('on')
plt.xlim(0, max(eixo_z_mm))
plt.ylabel('Potência')
plt.xlabel('z (pixels)')
plt.scatter(eixo_z_mm, med_imgs_lin, color = 'dodgerblue', marker = '.')
plt.scatter(eixo_z_mm, dados_pot_75_fit, color = 'orangered', marker = '.')
plt.legend(('Dados Experimentais', 'Ajuste Exponencial'))
plt.show()

#Teste de remoção de outliers pela média e DP
from preprocess import remoutliers, normaliza, preselec

outlier_dp1 = remoutliers(padroes = med_imgs_lin, p = 1, method = 'desvio')
sinal_dp1 = np.delete(med_imgs_lin, outlier_dp1, axis = 0)

outlier_dp2 = remoutliers(padroes = med_imgs_lin, p = 2, method = 'desvio')
sinal_dp2 = np.delete(med_imgs_lin, outlier_dp2, axis = 0)

plt.figure(figsize = (6,4), dpi = 1600)
plt.scatter(np.linspace(0, len(med_imgs_lin) - 1, len(med_imgs_lin)), med_imgs_lin, marker = '*', s = 8, label = 'Sinal')
plt.scatter(outlier_dp2, med_imgs_lin[outlier_dp2], color = 'orange', s = 100)
plt.scatter(outlier_dp1, med_imgs_lin[outlier_dp1], color = 'red', s = 10)
plt.axhline(y = np.mean(med_imgs_lin) + np.std(med_imgs_lin, ddof = 1), linestyle = '--', color = 'red', alpha = 0.8, label = 'Mean 1 STD')
plt.axhline(y = np.mean(med_imgs_lin) - np.std(med_imgs_lin, ddof = 1), linestyle = '--', color = 'red', alpha = 0.8)
plt.axhline(y = np.mean(med_imgs_lin) + 2*np.std(med_imgs_lin, ddof = 1), linestyle = '-.', color = 'orange', alpha = 0.8, label = 'Mean 2 STD')
plt.axhline(y = np.mean(med_imgs_lin) - 2*np.std(med_imgs_lin, ddof = 1), linestyle = '-.', color = 'orange', alpha = 0.8)
plt.axhline(y = np.mean(med_imgs_lin), color = 'black', alpha = 0.8, linestyle = '-.')
plt.grid('on')
plt.xlim((min(eixo_z_mm), max(eixo_z_mm)))
plt.legend()

#Teste de remoção de outliers pela mediana e quartis
outlier_qt1 = remoutliers(padroes = med_imgs_lin, p = 1, method = 'quartis')
sinal_qt1 = np.delete(med_imgs_lin, outlier_qt1, axis = 0)

outlier_qt2 = remoutliers(padroes = med_imgs_lin, p = 2, method = 'quartis')
sinal_qt2 = np.delete(med_imgs_lin, outlier_qt2, axis = 0)

plt.figure(figsize = (6,4), dpi = 1600)
plt.scatter(np.linspace(0, len(med_imgs_lin) - 1, len(med_imgs_lin)), med_imgs_lin, marker = '*', s = 8, label = 'Sinal')
plt.scatter(outlier_qt2, med_imgs_lin[outlier_qt2], color = 'orange', s = 100)
plt.scatter(outlier_qt1, med_imgs_lin[outlier_qt1], color = 'red', s = 10)
plt.axhline(y = np.percentile(med_imgs_lin, 75) + (np.percentile(med_imgs_lin, 75) - np.percentile(med_imgs_lin, 25)), linestyle = '--', color = 'red', alpha = 0.8, label = 'Median 1 QT')
plt.axhline(y = np.percentile(med_imgs_lin, 25) - (np.percentile(med_imgs_lin, 75) - np.percentile(med_imgs_lin, 25)), linestyle = '--', color = 'red', alpha = 0.8)
plt.axhline(y = np.percentile(med_imgs_lin, 75) + 2*(np.percentile(med_imgs_lin, 75) - np.percentile(med_imgs_lin, 25)), linestyle = '-.', color = 'orange', alpha = 0.8, label = 'Median 2 QT')
plt.axhline(y = np.percentile(med_imgs_lin, 25) - 2*(np.percentile(med_imgs_lin, 75) - np.percentile(med_imgs_lin, 25)), linestyle = '-.', color = 'orange', alpha = 0.8)
plt.axhline(y = np.percentile(med_imgs_lin, 50), color = 'black', alpha = 0.8, linestyle = '-.')
plt.grid('on')
plt.xlim((min(eixo_z_mm), max(eixo_z_mm)))
plt.legend()



#%% RASCUNHO
    
array = lines[0].split(",")

teste = np.array([[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]])


a = f.read()


b = ("salivacomfiltroH000000.cma", "r")


# Variáveis de manipulação
dtframe = {}
imgs = {}
soma_imgs = np.empty((614, 815))
tags = [1, 2, 3, 5, 6, 7, 8, 9, 11, 13, 15, 16, 17, 18, 20]


# Leitura das imagens e manipulação inicial
for i in range(0, len(tags), 1):
    id = str(tags[i])
    dtframe['pulso{0}'.format(tags[i])] = plt.imread('pulso_#' + id.zfill(3) + '.tif')
    imgs['img{0}'.format(tags[i])] = dtframe['pulso{0}'.format(tags[i])][:, :, 2]
    soma_imgs += imgs['img{0}'.format(tags[i])]

