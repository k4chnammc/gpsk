# plik rysujacy wykresy dla x punktow 
import matplotlib.pyplot as plt 
file=R"C:\Users\marta\Desktop\studia\sem5\gpsk\p1\dxdy.txt"
f= open(file, 'r')
lines = f.read().replace('\t', '\n').replace(' ','').replace(',','.').splitlines()

for i in range(0, len(lines)):
    lines[i]=float(lines[i])  #zamiana danych z string na float 


tempx=[]
tempy=[]  
def draw_plot(data,il_pkt,il_ser):   #argumenty: lista wynikow, ilosc punktow, ilosc serii
    for j in range(0,il_pkt):
        for i in range(0,il_ser):
            tempx.append(lines[i*il_pkt*2+j*2])
            tempy.append(lines[i*il_pkt*2+1+j*2])
        
        fig, ax = plt.subplots()
        plt.title("Wykres trajektorii punktu {}".format(j+1), fontsize=15) 
        plt.xlabel("Y [mm]", fontsize=15)
        plt.ylabel("X [mm]", fontsize=15)

        for k in range(0,len(tempx)):
            ax.annotate('S{}'.format(k+1), (tempy[k], tempx[k]),fontsize=10)

        ax.plot(tempy, tempx, color='#808080',linestyle='-', linewidth=1.2)
        ax.plot(tempy, tempx, color='#ff33cc',marker='*', markersize=10,linestyle="none")
        
        plt.grid(axis = 'x',color='#000000',linestyle='dotted',alpha=0.3) ##ACCBFA
        plt.grid(axis = 'y',color='#000000',linestyle='dotted',alpha=0.3)
        plt.gca().set_aspect("equal") ##wyrownanie osi
        
        tempx.clear()
        tempy.clear()


        plt.show()

  
print(draw_plot(lines,4,10))

