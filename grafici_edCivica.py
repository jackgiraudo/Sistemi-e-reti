import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import csv

def main():
    mesi = []
    tmp = []
    giacca = []
    scuola = []
    videogame = []
    
    data_file = open("valori.csv")
    data_reader = csv.reader(data_file, delimiter=',')
    next(data_reader)
    
    for row in data_reader:
        mesi.append(row[0])
        tmp.append(float(row[1]))
        giacca.append(float(row[2]))
        scuola.append(float(row[3]))
        videogame.append(float(row[4]))
    
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1)
    fig.suptitle('temperature medie')

    ax1.plot(mesi, tmp, 'o-r')
    ax1.set_xlabel('Mese')
    ax1.set_ylabel('Media voti')

    ax2.plot(mesi, giacca, 'o-g')
    ax2.set_xlabel('Mese')
    ax2.set_ylabel('Giacca')

    ax3.plot(mesi, scuola, 'o-b')
    ax3.set_xlabel('Mese')
    ax3.set_ylabel('Scuola')

    ax4.plot(mesi, videogame, 'o-y')
    ax4.set_xlabel('Mese')
    ax4.set_ylabel('Videogame')

    plt.show()

if __name__ == "__main__":
    main()