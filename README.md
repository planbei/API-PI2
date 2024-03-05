# Déploiement d'un projet Flask

Ce fichier README.md explique comment déployer un projet Flask.

## Prérequis

Assurez-vous d'avoir Python installé sur votre machine.

## Étapes de déploiement

### 1. Cloner le projet depuis GitHub

```bash
git clone https://github.com/votre_utilisateur/votre_projet.git
cd votre_projet
```
### 2. Créer un environnement virtuel

```bash
python -m venv mon_env
```

### 3. Activer l'environnement virtuel
```bash
mon_env\Scripts\activate
```

### 4. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 5. Installer les dépendances
```bash
flask run
```
L'application devrait être accessible à l'adresse http://localhost:5000/ dans votre navigateur.
