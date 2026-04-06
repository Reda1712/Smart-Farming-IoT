import streamlit as st
import joblib
import pandas as pd
import requests

# 1. Configuration de la page
st.set_page_config(page_title="Smart Farming Dashboard", layout="centered")
st.title(" Smart Farming - INPT")
st.subheader("Supervision Hybride : Capteurs Locaux + Cloud")

st.divider()

# 2. Le Cloud (Pour la pluie et la comparaison)
@st.cache_data(ttl=600)
def recuperer_meteo_live(api_key, ville="Casablanca,MA"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ville}&appid={api_key}&units=metric&lang=fr"
    try:
        reponse = requests.get(url)
        donnees = reponse.json()
        if reponse.status_code == 200:
            temp_api = donnees['main']['temp']
            pluie_mm = donnees.get('rain', {}).get('1h', 0)
            description = donnees['weather'][0]['description']
            return temp_api, pluie_mm, description
        return 25.0, 0.0, "Erreur API"
    except:
        return 25.0, 0.0, "Erreur Connexion"

MA_CLE_API = "VOTRE_CLE_API_ICI"
temp_api, pluie_live, desc_live = recuperer_meteo_live(MA_CLE_API)

st.write("###  Météo Globale (Casablanca - Cloud)")
col_m1, col_m2, col_m3 = st.columns(3)
col_m1.metric("Ciel", desc_live.capitalize())
col_m2.metric("Temp. Ville", f"{temp_api} °C")
col_m3.metric("Pluie (1h)", f"{pluie_live} mm")

st.divider()

# 3. Chargement de l'IA
try:
    modele = joblib.load('cerveau_pompe.pkl')
except FileNotFoundError:
    st.error(" Fichier 'cerveau_pompe.pkl' introuvable.")
    st.stop()

# 4. Simulation du Matériel Local (ESP32)
st.write("###  Capteurs Locaux (Simulation ESP32)")
st.info("Ces curseurs remplacent temporairement le DHT11 et le capteur de sol.")

col1, col2 = st.columns(2)
with col1:
    temp_locale = st.slider(" Température DHT11 (°C)", 10.0, 50.0, 25.0)
    hum_air_locale = st.slider(" Humidité Air DHT11 (%)", 20.0, 90.0, 50.0)
with col2:
    hum_sol = st.slider(" Humidité du Sol (%)", 0.0, 100.0, 30.0)

st.divider()

# 5. Le Moteur de Décision (Le cerveau hybride)
st.write("###  Décision de l'Intelligence Artificielle")

# L'IA prend les données LOCALES du DHT11, l'humidité du sol, ET la pluie du CLOUD !
donnees_actuelles = pd.DataFrame([[temp_locale, hum_air_locale, hum_sol, pluie_live]], 
                                 columns=['Temperature', 'Humidite_Air', 'Humidite_Sol', 'Pluie_mm'])

prediction = modele.predict(donnees_actuelles)[0]

if prediction == 1:
    st.success(" DÉCISION : ALLUMER LA POMPE (ON)")
    st.write("L'IA analyse tes capteurs locaux et la météo cloud : les conditions exigent un arrosage.")
else:
    st.error(" DÉCISION : POMPE ÉTEINTE (OFF)")
    st.write("L'IA bloque l'arrosage pour économiser l'eau (sol humide ou pluie imminente).")