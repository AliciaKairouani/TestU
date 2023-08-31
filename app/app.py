import streamlit as st
import pandas as pd
import numpy  as np
import requete

def texte(value = "Paris"):
    'ecrire le nom de la ville choisie'
    ville = st.text_input('Entrée le nom de votre ville', value = value)
    return ville



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

lon,lat = requete.get_latitude_longitude(ville)

st.map(latitude= lat, longitude= lon)



