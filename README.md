# API pour gestion des projets PI² ESILV

Ce fichier README.md explique comment initialiser et faire tourner l'API sur votre ordinateur et le lier avec github, afin de pouvoir la tester et la développer

Ce projet a été initié en Python 3.10.10

## Prérequis

Créer une base données MongoDB via Mongo ATLAS.

Assurez-vous d'avoir Python installé sur votre machine, ainsi que pip pour pouvoir installer les dépendances.

## Étapes de déploiement

### Cloner le projet depuis GitHub
Définissez un espace sur votre ordinateur dans lequel sera stockée le répertoire racine de l'API
Ici 'path/to/api' mais choisissez un espace mieux défini.
```bash
cd path/to/api
git clone https://github.com/YOUR_USERNAME/API-PI2.git
cd API-PI2
```
### Créer un environnement virtuel

```bash
python -m venv mon_env
```

### Activer l'environnement virtuel
```bash
mon_env\Scripts\activate
```

### Installer les dépendances
```bash
pip install -r requirements.txt
```

### Créer les variables d'environnement
Créez un fichier nommé '.env' à la racine du répertoir de l'API

#### En powershell :
```bash
cd path/to/api
New-Item -Type file .env
```
#### En windows classique :
```bash
cd path/to/api
type nul > .env
```
Ensuite, veuillez définir les variables suivantes dans le fichier .env fraîchement crée.
La syntaxe est la suivante : "NOM_DE_LA_VARIABLE=valeur". Notez que les chaînes de caractères ne prennent pas de guillemets.

>SECRET_KEY,
> 
>REACT_CLIENT_URL, 
> 
> MONGO_USERNAME,
> 
> MONGO_PASSWORD,
> 
> MONGO_CLUSTER_NAME,
> 
> DB_NAME,
> 
> USERS_COLLECTION_NAME,
>
> PROJECTS_COLLECTION_NAME

### Lancer l'API
```bash
flask run
```
L'API devrait être accessible à l'adresse http://localhost:5000/ dans votre navigateur.
Elle est accompagnée de sa documentation générée par Swagger, qui permet également de la tester à cette adresse.
