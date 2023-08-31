import streamlit as st
import pandas as pd
import numpy  as np

def texte():
    'ecrire le nom de la ville choisie'
    ville = st.text_input('Entrée le nom de votre ville', 'Enter text')
    return ville

def find_town(df ,name):
    "trouver info sur la ville"
    choix = df.loc[df['nom_commune_postal'] == name]
    return choix


st.title("Meteo Ville")

col1, col2= st.columns(2)

with col1:
    # Créer des widgets pour le nom de la ville
    ville = texte()

    # Afficher le nom choisie
    st.write('Nom de votre ville:', ville)

with col2:
    st.write(' ')

    if st.button("Submit"):
        data_ville = ville

df = pd.read_csv("communes-departement-region.csv")
choix = find_town(df, data_ville)
st.map(choix,latitude=df.latitude, longitude=df.longitude)



