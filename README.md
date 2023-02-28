## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

#### Déploiement

Configuration requise pour le déploiement

- Aller dans oc_lettings_site/settings.py et assurer vous que  ALLOWED_HOSTS=["*"] et DEBUG=False soit configuré.

Utilisation de Heroku comme hébergeur.

- Créer un compte Heroku à l'adresse suivante https://www.heroku.com/
- Installer le CLI pour Heroku compatible avec votre OS à l'adresse suivante https://devcenter.heroku.com/articles/heroku-cli
- Vérifier que Heroku est bien installé avec la commande `Heroku --version`
- Dans le terminal lancer la commande `Heroku login` afin de se connecter à Heroku
- Entrer vos informations personnels pour vous authentifier
- Dans le terminal lancer la commande `Heroku container:login` afin de se connecter à vos containers
- Dans le terminal lancer la commande `Heroku create` pour créer un repository ou `Heroku create "app name"`, si vous voulez précissez le nom de votre application, sinon un nom sera donné par defaut
- Dans le terminal lancer la commande au niveau de votre dockerfile (vérifier avec la commande `ls`, Dockerfile devrait être présent) `Heroku container:push web --app "app name"` pour déposer votre container sur Heroku
- Dans le terminal lancer la commande `Heroku container:release web --app "app name"` afin de compléter le déploiement et rendre le site accèssible.
- L'application web devrait maintenant être présente à l'url "https://app-name.herokuapp.com/". Remplacez app-name par le nom de votre application.
