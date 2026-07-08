import matplotlib
matplotlib.use('Agg') 
# matplotlib ist im nicht interactiven Modus, um Probleme mit der Anzeige zu vermeiden

############################################
# hier weitere imports:
import numpy as np
############################################


############################################
# hier könnten weitere Funktionen definiert werden, z.B. für die interaktive 
# Abfrage der Dichte
############################################

def initialisierung_proben():
    proben = [
        (101, "Granit_A1", 2.7, 150.5),
        (102, "Kalkstein_B2", 2.4, 80.2),
        (103, "Basalt_C3", 3.0, 200.0),
        (104, "Sandstein_D4", 2.2, 50.0),
        (105, "Schiefer_E5", 2.8, 120.3),
        (106, "Gneis_F6", 2.9, 180.7),
        (107, "Quarzit_G7", 2.6, 90.1),
        (108, "Tonstein_H8", 2.1, 40.5),
        (109, "Marmor_I9", 2.5, 110.0),
        (110, "Konglomerat_J10", 2.3, 70.2),
            ]
    return proben



def berechne_durchschnittliche_dichte(proben):

    listeDichten = []
    for probe in proben:
        listeDichten.append(probe[2])
    durchschnittdichte = np.mean(listeDichten)

    return durchschnittdichte

def bubble_sort(proben):

    n = len(proben)
    

    for i in range(n -1):
        vertauscht = False

        for j in range(n-1 - i):
            #print(proben[j][2], proben[j+1][2])
            if proben[j][2] > proben[j+1][2]:
                proben[j], proben[j+1] = proben[j+1], proben[j]
                vertauscht = True
                #print("Tausch")

                # Wenn nichts vertauscht wurde, ist die Liste bereits sortiert.
        if not vertauscht:
            break
    return proben

def ausgabetabelle(proben):
    print(f"{'ID':<5} | {'Name':<15} | {'Dichte':>10} | {'Gewicht':>8}")
    for probe in proben:
        print(f"{probe[0]:<5} | {probe[1]:<15} | {probe[2]:>10.1f} | {probe[3]:>8.1f}")

    return

def ausgabe(proben):
    namenNachDichte = []

    for probe in proben:
        namenNachDichte.append(probe[1])

    for index, name in enumerate(namenNachDichte):
        print(f"{index}: {name}")
    
    return
    
    





def main():
    print("Willkommen zum Dichteanalyse-Programm!\n" )
    # Schritt 1: Dateninitialisierung
    #initialisierung_proben()

    proben = initialisierung_proben()

    # Schritt 2: Durchschnittliche Dichte berechnen
    print(berechne_durchschnittliche_dichte(proben),"\n")

    # Schritt 3: Bubble Sort anwenden
    #print(bubble_sort(proben))

    # Schritt 4: Sortierte Proben ausgeben
    #print(bubble_sort(proben))
    ausgabetabelle(bubble_sort(proben))
    print()
    ausgabe(bubble_sort(proben))

    # Schritt 5: Visualisierung der Dichteverteilung

    # Schritt 6: Interaktive Abfrage der Dichte

if __name__ == "__main__":
    main()
