import requests

def recuperer_meteo(api_key, ville="casablanca,MA"):
    # L'URL de l'API OpenWeatherMap avec les paramètres : ville, clé API, unités en Celsius, et langue en français
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ville}&appid={api_key}&units=metric&lang=fr"

    try:
        # On envoie la requête GET au serveur
        reponse = requests.get(url)
        # On transforme la réponse textuelle en dictionnaire Python (JSON)
        donnees = reponse.json()

        # Code 200 = Succès de la requête HTTP
        if reponse.status_code == 200:
            # Extraction des données utiles en naviguant dans le JSON
            temperature = donnees['main']['temp']
            humidite = donnees['main']['humidity']
            description = donnees['weather'][0]['description']
            
            # Astuce : OpenWeatherMap n'envoie la clé 'rain' que s'il pleut vraiment.
            # On utilise .get() pour éviter une erreur si le ciel est dégagé (renvoie 0 par défaut).
            pluie_mm = donnees.get('rain', {}).get('1h', 0)

            print(f"--- Météo en direct pour {ville.split(',')[0]} ---")
            print(f"Température : {temperature} °C")
            print(f"Humidité : {humidite} %")
            print(f"Conditions : {description.capitalize()}")
            print(f"Volume de pluie (1h) : {pluie_mm} mm")
            print("-" * 35)

            return temperature, humidite, pluie_mm
        
        else:
            print(f"Erreur de l'API : {donnees.get('message', 'Inconnue')}")
            return None, None, None

    except requests.exceptions.RequestException as e:
        print(f"Erreur de connexion internet : {e}")
        return None, None, None

# ==========================================
# TEST DU SCRIPT
# ==========================================

# ⚠️ Remplace cette chaîne par la vraie clé API (suite de lettres et chiffres) 
# que tu as obtenue sur ton compte OpenWeatherMap lors de l'étape 3.1
MA_CLE_API = "61a0fb13c4c3efed8d5d31aeb500d149"

# Exécution de la fonction
temp_actuelle, hum_actuelle, pluie_actuelle = recuperer_meteo(MA_CLE_API)