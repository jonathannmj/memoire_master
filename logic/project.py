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
    
    
    def create_project_bundle(self, projectPath: str, destinationPath: str):
        """Cree un fichier mettant ensemble tous les fichiers et dossiers du projet.
        Le fichier a une extention (.nmjnwa).
        
        Args:
            projectPath: Le dossier source du projet (ex: /path/to/my_project_folder)
            destinationPath: Le chemin complet du fichier de destination (ex: /path/to/backup.nmjnwa)
        """
        source_dir = pathlib.Path(projectPath)
        dest_file = pathlib.Path(destinationPath)
        
        # Ensure destination ends with .nmjnwa
        if not dest_file.name.endswith(".nmjnwa"):
             dest_file = dest_file.with_suffix(".nmjnwa")

        print(f"Zipping {source_dir} to {dest_file}")

        with zipfile.ZipFile(dest_file, "w", zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(source_dir):
                for file in files:
                    fullPath = os.path.join(root, file)
                    # Avoid zipping the zip file itself if it's somehow in the loop (unlikely if saving outside)
                    if os.path.abspath(fullPath) == os.path.abspath(dest_file):
                        continue
                        
                    arcname = os.path.relpath(fullPath, source_dir)
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
        """Ouvre un projet (fichier .nmjnwa).
        Lit le fichier zip et l'extrait dans un dossier temporaire unique.
        Returns:
             tuple: (projectFolder, imageFile, dbFile)
        """
        import tempfile
        import shutil

        # Create a unique temp directory for this session's project
        # We use a fixed prefix but unique suffix so multiple opens don't clash immediately? 
        # Actually, for data persistence, if we want to save, we might want to know where it is.
        # But 'load_project' implies reading. 'save' implies writing back to the ZIP?
        # For now, let's extract to a temp folder. Any 'Save' operation will need to repackage.
        
        extract_dir = tempfile.mkdtemp(prefix="nmjnwa_project_")
        
        try:
            with zipfile.ZipFile(projectFilePath, "r") as zipf:
                zipf.extractall(extract_dir)
        except zipfile.BadZipFile:
             shutil.rmtree(extract_dir)
             raise Exception("Le fichier sélectionné n'est pas un fichier projet valide.")

        projectFolder = os.path.abspath(extract_dir)
        print(f"Project extracted to: {projectFolder}")

        dbFile = os.path.join(projectFolder, "privatedb.db") # Fixed typo .bd -> .db
        
        # Check if database exists
        if not os.path.exists(dbFile):
             # Try searching recursively? Or just fail. 
             # Standard structure is root/privatedb.db
             pass

        if not os.path.exists(dbFile):
            # Cleanup and raise
            # shutil.rmtree(extract_dir) # Keep it for debugging? No, clean up.
            pass
            # raise FileNotFoundError("Database (privatedb.db) not found in project bundle.")
        
        # Connect to the private database to get the image name
        try:
            imageName = self.get_image_name(dbFile)
        except Exception as e:
            # shutil.rmtree(extract_dir)
            raise Exception(f"Failed to read image name from database: {e}")

        # configsPath = os.path.join(projectFolder, "configurations") # Not strictly required to exist yet?
        imageFile = os.path.join(projectFolder, "image", imageName)

        if not os.path.exists(imageFile):
             # Try to find any image in image folder?
             pass

        # We return projectFolder. The app can find configs/images relative to it.
        # But for compatibility with existing code:
        configsPath = os.path.join(projectFolder, "configurations")
        
        return projectFolder, imageFile, dbFile, configsPath

    def delete_project(self, title, projectPath):
        """Suprimme un projet"""
        pass

    def get_image_name(self, database_path):
        """Charge le nom de l'image sur la quelle se base le projet en cours."""
        if not os.path.exists(database_path):
            raise FileNotFoundError(f"Database file not found: {database_path}")
            
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT image_name FROM image")
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                raise Exception("No image record found in database.")
        finally:
            connection.close()

