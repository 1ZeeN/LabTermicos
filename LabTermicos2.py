import easygui as ei

x=[]
y=[]
yerr=[]
xerr=[]
aux=[]
Sx=Sy=Sx2=Sy2=Sxy=Mx=Mx2=My=Spxy=Sqx=Sqy=Sxx=Syy=r=r2=0

title="Grafico"
choices=("X","Erro em X", "Y", "Erro em Y")
msg="Informe os valores do Experimento"
dados=ei.multenterbox(msg,title,choices)





print (x)