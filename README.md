#  Smart-Farming-IoT : Système d'Irrigation Intelligent & Prédictif

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![C++](https://img.shields.io/badge/C++-Arduino-00979D.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B.svg)
![Machine Learning](https://img.shields.io/badge/AI-Scikit_Learn-orange.svg)
![IoT](https://img.shields.io/badge/IoT-ESP32-yellow.svg)

##  Présentation du Projet
Ce projet est une architecture End-to-End d'agriculture intelligente (Smart Farming). Il démontre la synergie entre l'acquisition de données physiques (Edge Computing) et la prise de décision cloud via l'Intelligence Artificielle.

Contrairement à un système d'arrosage classique qui se contente de réagir à un sol sec, ce système est **prédictif**. Il croise l'état physique actuel du sol avec les prévisions météorologiques locales (API Cloud) via un modèle de Machine Learning pour optimiser la consommation d'eau et d'énergie (Green IT).

##  Architecture Technique

Le système est découpé en 4 couches :

### 1. Couche Matérielle (Hardware / Edge)
* **Microcontrôleur :** ESP32 DevKit (programmé en C++).
* **Capteurs :** * Capteur d'humidité du sol Capacitif v1.2 (anti-corrosion).
  * Capteur de température et d'humidité ambiante DHT11.
* **Actionneur & Puissance :**
  * Module Relais Électromécanique (1 Canal - 5V) commandé par l'ESP32.
  * Mini-pompe à eau submersible (DC 3V-5V).
  * Circuit d'alimentation de puissance isolé (Boîtier de piles externe) pour protéger le microcontrôleur.

### 2. Couche Communication
* Transmission asynchrone des données capteurs via le port Série/USB (115200 bauds).

### 3. Couche Logique & Intelligence Artificielle (Cloud)
* **Serveur Python :** Récupération et nettoyage des données séries en temps réel.
* **API REST :** Interrogation d'OpenWeatherMap pour récupérer les prévisions de pluie imminente.
* **Machine Learning :** Un modèle d'Arbre de Décision (`.pkl` via *Scikit-learn*) évalue la nécessité d'arroser. *Exemple de logique : Si le sol est sec mais qu'une forte pluie est prévue dans l'heure par l'API, la pompe ne s'active pas.*

### 4. Couche Supervision (IHM)
* Dashboard interactif développé avec **Streamlit**, permettant de visualiser les métriques physiques et le statut de l'arrosage en temps réel.

##  Installation et Déploiement

### 1. Configuration Matérielle (ESP32)
1. Câbler les capteurs et le module relais à l'ESP32. (La pompe doit être connectée sur le circuit de puissance du relais).
2. Ouvrir le code source dans l'**Arduino IDE**.
3. Installer la bibliothèque `DHT sensor library` (Adafruit).
4. Téléverser le code sur l'ESP32 (Vérifier le port COM et le pilote CP2102).

### 2. Configuration Logicielle (Python)
1. Cloner ce dépôt :
   ```bash
   git clone [https://github.com/Reda1712/Smart-Farming-IoT.git](https://github.com/Reda1712/Smart-Farming-IoT.git)
   cd Smart-Farming-IoT
