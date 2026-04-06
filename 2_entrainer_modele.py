import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib

# 1. Charger les données
print("Chargement des données...")
df = pd.read_csv('dataset_irrigation.csv')

# Séparer les "Questions" (Capteurs/Météo) de la "Réponse" (Pompe)
X = df[['Temperature', 'Humidite_Air', 'Humidite_Sol', 'Pluie_mm']]
y = df['Pompe_ON']

# Garder 20% des données pour vérifier si l'IA a bien appris (sans tricher)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Créer et Entraîner le cerveau (L'Arbre de Décision)
print("Entraînement de l'Intelligence Artificielle...")
modele = DecisionTreeClassifier(max_depth=4, random_state=42)
modele.fit(X_train, y_train)

# 3. Évaluer l'IA
predictions = modele.predict(X_test)
precision = accuracy_score(y_test, predictions) * 100
print(f"Précision du modèle : {precision:.2f} %")

# 4. Sauvegarder le cerveau dans un fichier pour l'utiliser plus tard
joblib.dump(modele, 'cerveau_pompe.pkl')
print("Le modèle est sauvegardé sous le nom 'cerveau_pompe.pkl'")