import pandas as pd
import random

donnees = []

# On simule 1000 scénarios différents
for _ in range(1000):
    temp = round(random.uniform(10.0, 45.0), 1)       # Température de 10 à 45°C
    hum_air = round(random.uniform(20.0, 90.0), 1)    # Humidité air de 20 à 90%
    hum_sol = round(random.uniform(10.0, 90.0), 1)    # Humidité sol de 10 à 90%
    pluie_mm = round(random.uniform(0.0, 20.0), 1)    # Pluie prévue de 0 à 20mm

    # --- LA LOGIQUE EXPERTE (C'est ce que l'IA va devoir deviner) ---
    pompe_allumee = 0 # Par défaut, la pompe est éteinte

    if hum_sol < 40: # Le sol est sec
        if pluie_mm > 5.0:
            pompe_allumee = 0 # Il va pleuvoir, on économise l'eau !
        else:
            pompe_allumee = 1 # Pas de pluie, il faut arroser.
            
    elif hum_sol >= 40 and hum_sol < 60: # Sol moyennement humide
        if temp > 35.0 and pluie_mm < 2.0:
            pompe_allumee = 1 # Il fait très chaud et pas de pluie, un petit coup d'eau
            
    # Si le sol est > 60%, la pompe reste éteinte (pompe_allumee = 0)

    # On ajoute ce scénario à notre liste
    donnees.append([temp, hum_air, hum_sol, pluie_mm, pompe_allumee])

# On sauvegarde tout dans un fichier Excel/CSV
df = pd.DataFrame(donnees, columns=['Temperature', 'Humidite_Air', 'Humidite_Sol', 'Pluie_mm', 'Pompe_ON'])
df.to_csv('dataset_irrigation.csv', index=False)

print("Dataset généré avec succès ! Le fichier 'dataset_irrigation.csv' a été créé.")