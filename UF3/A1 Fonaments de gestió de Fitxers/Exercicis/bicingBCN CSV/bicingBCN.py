'''
Pol Cerrillo
25/04/2024
ASIXc1C M03 UF3
Descripció: Fer un programa en Python que llegint el fitxer CSV del Bicing  de Barcelona ens doni la següent informació:
Obtenir la "capacity" de l'estació amb més bicicletes i la que en te menys     estació: 2533 amb 54 i 78 amb 0
Obtenir la "capacity" total de la ciutat de barcelona
Font:  Open Data BCN  Inici >  Ciutat i serveis >  Transport >  Informació de les ...> 2023_03_Marc_BicingNou_INFO ...
Arxiu a processar: 2023_03_Marc_BicingNou_INFORMACIO.csv.7z
quantitat de línies: 4.291.777
Pista:  Que macos són els PANDAS !!
'''
import pandas as pd
def llegir_cdv():
    df = pd.read_csv('2023_03_Marc_BicingNou_INFORMACIO.csv').drop_duplicates()
    return df
def calcular_capacitat(df):
    capacitat_maxima = df.loc[df['capacity'].idxmax()]
    capacitat_minima = df.loc[df['capacity'].idxmin()]
    df = df.drop_duplicates(subset=["station_id"])
    capacitat_total = df['capacity'].sum()
    return capacitat_maxima, capacitat_minima, capacitat_total
def main():
    df = llegir_cdv()
    capacitat_maxima, capacitat_minima, capacitat_total = calcular_capacitat(df)
    print(f"Estació amb més bicicletes: {capacitat_maxima['station_id']} amb {capacitat_maxima['capacity']} bicicletes")
    print(f"Estació amb menys bicicletes: {capacitat_minima['station_id']} amb {capacitat_minima['capacity']} bicicletes")
    print(f"Capacitat total de la ciutat de Barcelona: {capacitat_total} bicicletes")

