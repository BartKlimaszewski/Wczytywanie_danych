import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Wczytywanie pliku csv
df = pd.read_csv('test_data.csv')

#Odczytuje ilości wierszy i kolumn
print(f"Wiersze i kolumny: {df.shape}")

#Sprawdzam jakie mam kolumny
print(f"Kolumny: {df.columns}")

#Identyfikacja typów danych
print(f"Typy danych w kolumnach:\n{df.dtypes}")

#Sprawdzam ewentualne braki w danych - True oznacza braki
print(df.isnull())

#Statystyki
print(f"Statystyki:\n{df.describe()}")

#Średnia pensja we wszystkich działach
print(df.groupby("Department")["Salary"].mean())

#Ilość pracowników w poszczególnych krajach
print(df.groupby("Country").count())

#Średnia pensja dla osób > 30lat
print(f"Ludzie powyżej 30 roku życia zarabiają średnio: {df[df["Age"] > 30]["Salary"].mean()}")    

#Wykres Wiek do Pensji
def pokaz_wykres():
    x = df["Age"]
    y = df["Salary"]
    a, b = np.polyfit(x, y, 1) #Wyliczanie współczynników linii
    plt.plot(x, a*x+b, color="red", label="Linia regresji") #Dodawanie linii regresji na wykres
    plt.scatter(x, y, color="orange", edgecolors="black")
    plt.legend()
    plt.title("Wykres Wiek do Pensji")
    plt.xlabel("Wiek")
    plt.ylabel("Pensja (PLN)")
    plt.grid(True)
    plt.style.use('seaborn-v0_8-pastel')
    if input("Zapisz wykres do pliku PNG? (T/N): ").strip().upper() == "T": #Opcja zapisywania wykresu w postaci pliku PNG, usuwam spacje z początku i końca, zwiększam litere
        filename = input("Wprowadź nazwe dla wykresu: ").strip().lower() #Nazwa dla wykresu, usuwamy spacje z początku i końca, zmniejszamy litery żeby uniknąć błędów
        if not filename.endswith(".png"): #Chcemy mieć plik PNG, dlatego sprawdzamy czy na końcu jest .png, jeżeli nie ma, to automatycznie dodajemy
            filename += ".png"
        plt.savefig(filename)
    plt.show()
        
#pokaz_wykres() Tymczasowo wyłączone, aby nie tworzyć niepotrzebnych plików png z wykresami


#Przykładowy raport danych z data_large.csv odpowiadający na pytania: Chcę wiedzieć, który dział płaci najlepiej, czy wiek wpływa na pensję i ilu mamy pracowników z Polski.
def raport():
    srednie_place = df.groupby("Department")["Salary"].mean() #Segreguję działy w zależności od płacy
    najlepszy_dzial = srednie_place.idxmax() #Wybieram najbardziej dochodowy dział
    najlepsza_pensja = srednie_place.max()  #Średnia płaca najbardziej dochodowego działu
    print(f"Najlepiej płaci dział: {najlepszy_dzial}, ze średnią pensją: {najlepsza_pensja:.2f}PLN.")
    
    a = df["Age"].corr(df["Salary"]) #Liczę współczynnik korelacji Pearsona
    if a > 0:
        print("Wraz z wiekiem pensja rośnie")
    elif a < 0:
        print("Wraz z wiekiem pensja maleje")
    else:
        print("Wiek nie wpływa na pensję")
        
    pracownicy = df["Country"].value_counts()
    polacy = pracownicy["Poland"]
    print(f"Liczba pracowników z Polski wynosi: {polacy}.")
    
raport()
