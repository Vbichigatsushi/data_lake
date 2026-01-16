# 🌊 DATA_LAKE | Spark Infrastructure 🚀

---

## 📋 Présentation du Projet
Bienvenue dans le dépôt **DATA_LAKE**. Ce projet est une implémentation moderne d'un pipeline de données utilisant **PySpark** et géré par l'outil de performance **uv**. 

L'objectif est de fournir une structure robuste pour le traitement de données à grande échelle avec une séparation claire des couches de données (Medallion Architecture).

---

## 🏗️ Architecture du Répertoire
L'organisation des fichiers suit les standards industriels de l'ingénierie de données :

* 📂 **`.venv/`** : Environnement virtuel isolé géré par `uv`. 🛠️
* 📂 **`config/`** : Centralisation des paramètres Spark et variables d'environnement. ⚙️
* 📂 **`data/`** : Stockage local simulant le Data Lake :
    * 📥 `raw/` : Données brutes non transformées.
    * 🛠️ `staging/` : Zone de transit pour le nettoyage.
    * ✨ `curated/` : Données finales prêtes pour l'analyse.
* 📂 **`notebooks/`** : Expérimentation interactive et visualisation de données. 📊
* 📂 **`src/`** : Code source modulaire pour la production. 🐍
* 📄 **`pyproject.toml`** : Manifeste de configuration et dépendances ultra-rapides. ⚡
* 📄 **`uv.lock`** : Verrouillage déterministe des versions pour la reproductibilité. 🔒

---

## 🛠️ Stack Technique
* 🤖 **Générateur** : Intelligence Artificielle (Modèle Gemini, ChatGPT, Claude)
* 🐍 **Langage** : Python 3.12+
* 🔥 **Framework** : PySpark
* 📦 **Gestionnaire** : [uv](https://github.com/astral-sh/uv)

---

## 🚀 Guide de Démarrage Rapide

1.  **Synchronisation de l'environnement** :
    ```bash
    uv sync
    ```

2.  **Exécution du pipeline principal** :
    ```bash
    uv run python main.py
    ```

3.  **Lancement des notebooks** :
    ```bash
    uv run jupyter lab
    ```

---

### 🧐 Audit du Cours
* **Manque d'accompagnement** : Utiliser ChatGPT pour générer un support de cours sans apporter d'accompagnement concrèt ne constitue pas un acte d'enseignement.
* **Problème Technique** : Nous n'avons pas réussi a faire fonctionner le code. Et quand nous remontions les problèmes vous ne faisiez que nous envoyer sur une IA ou nous dire de supprimer l'appel de la méthode.
* **Investissement** : L'attitude passive de l'intervenant nuit gravement à la progression des apprenants.

---
