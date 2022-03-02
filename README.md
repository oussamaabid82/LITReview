# Application qui perme de demander des critiques de livres ou d’articles, en créant un ticket et de publier des critiques de livres ou d’articles

* ##### Cette application web permettant à une communauté d'utilisateurs de consulter ou de solliciter une critique de livres à la demande.


* ### Prérequis
	- il faut installer un Shell sur votre ordinateur, sinon vous pouvez utiliser le terminal préinstallé avec votre système d'exploitation:

	- WINDOWS:
		-  touche Windows + R puis tapez 'cmd' puis ENTRER 

	- MAC:
		- Cliquez sur l’icône Launchpad dans le Dock, saisissez Terminal dans le champ de recherche, puis cliquez sur Terminal.
		- Dans le Finder, ouvrez le dossier /Applications/Utilitaires, puis cliquez deux fois sur Terminal.
	 
	- LINUX: 
		- ctrl + alt + t

* ### Démarrage
	- télécharger l'application: https://github.com/oussamaabid82/LITReview.
	- Démarrer votre terminal et diriger vous dans le dossier télécharger (LITReview).
    - Créer un environnement virtuel en tapant dans votre terminal:
        ```bash
        python -m venv venv
        ```
    - Activer l'environnement en tapant dans votre terminal:
        ```bash
        source venv/Scripts/activate
        ```
	- Installez Django et les modules nécessaires pour le bon fonctionnement du programme
		```bash
		pip install -r requirements.txt
		``` 
	- Démarrer le le serveur en tapant dans votre terminal:
		```shell
		python manage.py runserver
		```
    - Ouvrez votre navigateur web et taper http://127.0.0.1:8000/ dans la barre d'adresse pour démarrer le programme
    
* ### Fabriqué avec
	- [VSCode](https://code.visualstudio.com/) 
	- [Cygwin](https://www.cygwin.com/install.html)

* ### Versions
	- Bêta

* ### Auteurs
	- Abid Oussama:
 
	 [oussamaabidd@gmail.com](oussamaabidd@gmail.com)

	- Mr Williams De Souza
