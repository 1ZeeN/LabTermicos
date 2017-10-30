import numpy as np
import matplotlib.pyplot as plt

T1=[54,53.9,53.5,53,52.6,52,51.8,51.5,51,50.5,50.2,49.8,49.5,49.2,48.9,48.6,48.3,48,47.7,47.4,47.1,46.8,46.5,46.3,46,45.7,45.4,45.2,44.9,44.8]    #Temperatura do 1º Experimento
T2=[54.2,53.9,53.3,53,52.5,52,51.7,51.3,51,50.6,50.3,50,49.5,49,48.6,48.3,48,47.7,47.4,47.1,46.8,46.5,46.2,45.9,45.7,45.5,45.2,44.9,44.7,44.4]  #Temperatura do 2º Experimento
TM=[]                   #Temperatura Media de T1 e T2
LA=[]
Y=[]
To1=55                  #Temperatura Inicial do 1ºExperimento
To2=55                  #Temperatura Inicial do 2ºExperimento
x=[0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15]         #Tempo
Ta=27                   #Temperatura Inicial

n=len(x)
ToM= (To1+To2)/2
for i in range(len(T1)):
    media= (T1[i] + T2[i]) / 2
    TM.append(media)
    T= (TM[i] - Ta) / (ToM - Ta)
    y=(np.log(T))             #Calculo do Lambida (coeficiente angular)
    Y.append(y)

for i in range(len(T1)):
    La= -Y[i] * x[i]
    LA.append(La)

from LabTermicos import cal

cal()
plt.plot(x, Y)
plt.show()
print (a,b)

