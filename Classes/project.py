import pathlib
import os
import zipfile
import sqlite3

from data import privatedb

class Project:
    """Gestionnaire des projets"""
    def __init__(self):
        self.projects = []
        self.principalDB = "./principalDB.db"

    def create_project(self, title: str, destination: str):
        """Cree tous les dossiers et fichiers relatifs au projet:
            - Un dossier principal dans lequel sont les dossiers:
                - ansible_files: Qui contiendra les fichiers necessaires a la generation des commandes de configuration des equipements reseau;
                - configurations: Dossier dans lequel seront sauvegardes les configurations generees grace a Ansible;
                - image: Dossier contenant l'image de laquelle seront extaites les donnees de la topologie"""
        
        projectPath = pathlib.Path(destination) / title
        if not projectPath.exists():
            # Creation du dossier du projet
            projectPath.mkdir(parents=True, exist_ok=True)

            # Creation des dossiers Ansible_files, configurations et image
            ansibleFiles = pathlib.Path(projectPath) / "ansible_files"
            configsDirectory = pathlib.Path(projectPath) / "configurations"
            imageDirectory = pathlib.Path(projectPath) / "image"
            ansibleFiles.mkdir(parents=True, exist_ok=True)
            configsDirectory.mkdir(parents=True, exist_ok=True)
            imageDirectory.mkdir(parents=True, exist_ok=True)

            # Creation du fichier de la base de donnees privee
            dbFile = os.path.join(projectPath, "privatedb.db")
            dbAbsolutePath = os.path.abspath(dbFile)

            # Creation des tables de la base de donnees
            privatedb.create_db(dbAbsolutePath)

            # TODO: Add the project to the database
        return projectPath
    
    def create_project_bundle(self, projectPath: str, projectName: str):
        """Cree un fichier mettant ensemble tous les fichiers et dossiers du projet.
        Le fichier a une extention (.nmjnwa), qui est l'extention des projets
        crees par ce logiciel
        
        Usage:
                create_project_bundle(projectPath, projectName)
                
                - projectPath: L'adresse du dissier cree pour le projet en cours.
                - projectName: Le nom a donner au fichier qui sera cree"""

        if ".nmjnwa" in projectName:
            zipPath = pathlib.Path(projectPath) / projectName
            # zipPath = f"{projectPath}{projectName}"
            print(zipPath)
        else:
            zipPath = pathlib.Path(projectPath) / f"{projectName}.nmjnwa"
            # zipPath = f"{projectPath}{projectName}.nmjnwa"
            print(zipPath)

        with zipfile.ZipFile(zipPath, "w") as zipf:
            for root, dirs, files in os.walk(projectPath):
                for file in files:
                    fullPath = os.path.join(root, file)
                    arcname = os.path.relpath(fullPath, projectPath)
                    zipf.write(fullPath, arcname)

    def save_destination_path_to_db(self, destinationPath: str):
        """Sauvegarde dans la base de donnees principale les adresses dans les quelles les projets pouront etre sauvegardees"""
        connection = sqlite3.connect(self.principalDB)
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO destination_paths (destination_path) VALUES(?)", (destinationPath,))
            connection.commit()
        except sqlite3.IntegrityError:
            pass
        finally:
            connection.close()

    def get_all_destination_paths(self):
        """Recolte/charge toutes les destinations deja utilisees pour la sauvegarde de nos projets"""

        connection = sqlite3.connect(self.principalDB)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM destination_paths")
        destinationPaths = cursor.fetchall()
        connection.close()
        return destinationPaths

    def load_project(self, projectFilePath):
        """Ouvre un projet.
        
        Il prend comme variable, un fichier avec l'extention (.nmjnwa)"""

        extractTo = "Project_folder"
        with zipfile.ZipFile(projectFilePath, "r") as zipf:
            zipf.extractall(extractTo)
        projectFolder = os.path.abspath(extractTo)
        print(projectFolder)

        dbFile = os.path.join(projectFolder, "privatedb.bd")
        if not os.path.exists(dbFile):
            raise FileNotFoundError("Database not found.")
        
        # Connect to the private database to get the image name
        imageName = self.get_image_name()

        configsPath = os.path.join(projectFolder, "configurations")
        imageFile = os.path.join(projectFolder, "image", imageName)

        if not os.path.isdir(configsPath):
            raise FileNotFoundError("Config folder missing.")
        if not os.path.exists(imageFile):
            raise FileNotFoundError("Image file not found missing.")
        
        # Si tout a ete charge avec succes, Return l'adresse du dossier du projet, l'image, la base de donnees et le dossier des configurations
        return projectFolder, imageFile, dbFile, configsPath

    def delete_project(self, title, projectPath):
        """Suprimme un projet"""
        pass

    def get_image_name(self, database):
        """Charge le nom de l'image sur la quelle se base le projet en cours.
        
        Elle prend comme variable, la base de donnees privee du projet"""

        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute("SELECT image_name FROM image")
        imageName = cursor.fetchone()
        connection.close()
        return imageName[0]

