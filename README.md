
  

# Scrap Mechanic Multiplayer Bot

  

Ce bot discord permet de jouer à plusieurs à Scrap Mechanic sans créer de serveur dédié, en facilitant le partage de la map du jeu entre les joueurs. Il est conçu pour simplifier l'expérience multijoueur en automatisant le processus de partage de la map du jeu.

**Ce projet a été testé uniquement sur Windows et fonctionne avec Python 3.11.**

### Fonctionnalités

-   **Envoi de map** : Envoyer facilement une map de jeu à un canal désigné.
    
-   **Téléchargement de map** : Télécharger automatiquement une map et la déplace vers le dossier de jeu approprié.
    
-   **Gestion des fichiers** : Vérifier l'existence des fichiers pour éviter les erreurs et les messages inutiles.

## Installation

1. Clonez le dépôt :

```bash
git clone https://github.com/DotoroIII/ScrapMapSender.git
cd ScrapMapSender

```

2. Installez les dépendances requises :

```bash
pip install -r requirements.txt

```

## Configuration

Avant d'utiliser le bot, vous devez éditer le fichier de configuration `config.ini` situé dans le répertoire racine du projet. Voici les étapes :

1. Ouvrez le fichier `config.ini` dans un éditeur de texte.

2. Remplacez les valeurs suivantes par les vôtres :

   ```ini
   [BOT]
   Token = VOTRE_TOKEN
   ID_channel = L'ID_du_canal
   Message_for_using = J'utilise
   
   [FOLDER]
   Scrap_Mechanic_map_folder = Chemin_vers_le_dossier_de_map_de_Scrap_Mechanic
   ```


## Utilisation

### Arguments
-  `-f`, `--file` : Le nom de la map.

-  `send` : Envoie la map.

-  `move` : Télécharge et la déplace la map dans le dossier de map configuré.

### Exemples de commandes

#### Envoyer une map

Pour envoyer une map, utilisez la commande suivante :

```bash

python main.py --file nom_de_la_map send
```

#### Télécharger une map

Pour télécharger une map, utilisez la commande suivante :

```bash

python main.py --file nom_de_la_map download
```