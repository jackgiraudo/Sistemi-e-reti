import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import csv

def main():
    anni = []
    tot = []

    anniTemp = []
    temperatura=[]
    
    data_file1 = open("CO2.csv")
    data_reader1 = csv.reader(data_file1, delimiter=',')
    next(data_reader1)

    data_file2 = open("temperatura.csv")
    data_reader2 = csv.reader(data_file2, delimiter=',')
    next(data_reader2)

    
    for row1 in data_reader1:
        anni.append(row1[0])
        tot.append(float(row1[1]))

    for row2 in data_reader2:
        anniTemp.append(row2[0])
        temperatura.append(float(row2[1]))
    
    fig, (ax1, ax2) = plt.subplots(2, 1)
    fig.suptitle('Cambiamento climatico')

    anniSlice = anni[0::2]
    totS = tot[0::2]
    
    ax1.plot(anniSlice, totS, 'o-r')
    ax1.set_xlabel('Anno')
    ax1.set_ylabel('CO2')

    anniS2 = anniTemp[0::2]
    tempS = temperatura[0::2]

    ax2.plot(anniS2, tempS, 'o-r')
    ax2.set_xlabel('Anno')
    ax2.set_ylabel('Temperatura')


    plt.show()

if __name__ == "__main__":
    main()