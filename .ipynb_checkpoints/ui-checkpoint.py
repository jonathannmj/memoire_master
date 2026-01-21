import os
import sys
from PySide6.QtCore import QTime, QUrl, Qt, QThread, Signal, QObject
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QMessageBox, QStackedWidget, QGridLayout, QFileDialog, QVBoxLayout, QPushButton

from UI.main_window.main_window_ui import Ui_MainWindow
from UI.open_project.open_project_ui import Ui_OpenProject
from UI.image_import.image_import_ui import Ui_ImportImage
from UI.after_extraction.after_extraction_ui import Ui_AfterExtraction
from UI.modify_data.modify_ui import Ui_ModifyData
from UI.configs_old_project.configs_old_project_ui import Ui_OldProjectConfigsPage
from UI.configs_old_project.configuration_ui import Ui_Configuration
from UI.data_extracting.data_extracting_ui import Ui_DataExtraction

from software import Project, TopologyData, Node0, Configurations


# Global variables
imagePath = None

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.appData = AppData()

        self.new_project_window = OpenProject(self)

        self.stacked = self.stackedWidget

        # Pages to be shown in the stacked widget
        self.after_extraction_page = AfterExtraction(self)
        self.modify_data_page = ModifyData(self)
        self.project_open_page = OpenProject(self, appData=self.appData)

        # Ajout des pages au stacked widget
        self.stacked.addWidget(self.project_open_page)
        self.stacked.addWidget(self.after_extraction_page)
        self.stacked.addWidget(self.modify_data_page)

        # Affichage de la page de selection/creation d'un projet
        self.stacked.setCurrentWidget(self.project_open_page)
        # selectedPath, self.projectTitle = self.open_a_project()
        # self.currentProjectPath = Project().create_project(self.projectTitle, selectedPath)

        self.project_open_page.appInfosFilled.connect(self.create_new_project)

        # Page d'importation de l'image dans un projet
        # self.image_import_page_in_a_project = ImageImport(self, currentProjectPath=self.currentProjectPath, appData=self.appData)
        # self.stacked.addWidget(self.image_import_page_in_a_project)

        # self.stacked.setCurrentWidget(self.image_import_page_in_a_project)

        # Actions from the File menu
        self.actionNew.triggered.connect(self.create_new_project)
        self.actionOpen.triggered.connect(self.open_a_project)
        self.actionFermer.triggered.connect(self.close)
        self.actionSave.triggered.connect(self.save)
        self.actionSave_As.triggered.connect(self.save_as)

    def create_new_project(self):
        # Affichage de la page de selection/creation d'un projet
        self.currentProjectPath = str(self.appData.selectedDirectory)
        print(self.currentProjectPath)
        self.projectTitle = str(self.appData.projectTitle)
        print(self.projectTitle)
        self.appData.currentProjectPath = self.currentProjectPath

        self.import_image()
    
    def import_image(self):
        self.image_import_page_in_a_project = ImageImport(self, currentProjectPath=self.currentProjectPath, appData=self.appData)
        self.stacked.addWidget(self.image_import_page_in_a_project)
        self.stacked.setCurrentWidget(self.image_import_page_in_a_project)

        self.image_import_page_in_a_project.imageUploaded.connect(self.data_extraction)

    def open_a_project(self):
        dialog = OpenProject(self)
        dialog.exec()  # Show the dialog to select a project
        
        project_path = dialog.projectDestinationCombo.currentText()
        projectName = dialog.projectTitleField.text()

        return project_path, projectName
        
    def open_existing_project(self, projectFile):
        """Ouverture d'un projet existant"""

        self.old_project_configs = OldProjectConfigs(self, projectFile=projectFile)
        self.stacked.setCurrentWidget(self.old_project_configs)

    def data_extraction(self):
        
        # The progress bar
        self.progressBar = DataExtraction(self).progressBar
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(0)
        DataExtraction(self).show()

        self.worker = Worker(self, self.appData)
        self.thread = QThread()
        self.worker.moveToThread(self.thread)
        self.worker.finished.connect(self.thread.quit)
        self.thread.started.connect(self.worker.run)
        self.thread.start()

        self.stacked.setCurrentWidget(self.after_extraction_page)

    def save(self):
        Project().create_project_bundle(self.currentProjectPath, self.projectName)
        
    def save_as(self):
        # TODO: Finir le save as
        fileDestination = QFileDialog.getSaveFileName("Nom du projet", ".nmjnwa")
        Project().create_project_bundle(projectPath=self.currentProjectPath, projectName=fileDestination)

    def after_extraction(self):
        self.stacked.setCurrentWidget(self.after_extraction_page)

    def closeEvent(self, event):
        # Demander de sauvegarder avant de fermer
        confirmation = QMessageBox.question(self, "Confirmation", "Voulez-vous Sauvegarder avant de Fermer l'Application ?", QMessageBox.Yes | QMessageBox.No)

        if confirmation == QMessageBox.Yes:
            self.save(self.currentProjectPath, self.projectName)
            event.accept()
        else:
            event.accept()


class OpenProject(QDialog, Ui_OpenProject):
    appInfosFilled = Signal()
    def __init__(self, parent=None, projectPath=None, appData=None):
        super().__init__(parent)
        self.setupUi(self)
        self.appData = appData
        self.projectPath = projectPath

        self.destination_paths_combo()

        self.createProject = self.createProjectButton
        self.createProject.pressed.connect(self.create_new_project)
        self.changeFileDestinationButton.pressed.connect(self.select_project_destination)
        self.closeProjectFormButton.pressed.connect(self.close)
        self.openAProjectButton.pressed.connect(self.select_project)

    def destination_paths_combo(self):
        project = Project()
        destinationPaths = project.get_all_destination_paths()
        if (destinationPaths):
            self.projectDestinationCombo.addItems([path[1] for path in destinationPaths])
            self.projectDestinationCombo.setCurrentText(destinationPaths[-1][1])

    def create_new_project(self):
        projectTitle = self.projectTitleField.text()
        projectDestination = self.projectDestinationCombo.currentText()

        if projectTitle and projectDestination:
            projectDirectory = Project().create_project(projectTitle, projectDestination)
            self.close()
            self.appData.projectTitle = projectTitle
            self.appData.selectedDirectory = projectDirectory
            self.appInfosFilled.emit()

    def select_project_destination(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Project Destination")
        if directory:
            Project().save_destination_path_to_db(directory)
            self.projectDestinationCombo.clear()
            self.destination_paths_combo()
            self.projectDestinationCombo.setCurrentText(directory)

    def select_project(self):
        self.projectFile = QFileDialog.getOpenFileName(self, "Select a project file", "*.nmjnwa")
        if self.projectFile:
            self.close()
            MainWindow().open_existing_project(self.projectFile)


class ImageImport(QWidget, Ui_ImportImage):
    imageUploaded = Signal()
    def __init__(self, parent=None, currentProjectPath=None, appData=None):
        super().__init__(parent)
        self.setupUi(self)
        self.appData = appData
        self.currentProjectPath = currentProjectPath

        self.importImageButton.pressed.connect(self.import_image)


    def import_image(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Select an image", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)")
        if filePath:
            self.appData.imagePath = filePath
            self.imageUploaded.emit()
         

class AfterExtraction(QWidget, Ui_AfterExtraction):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class ModifyData(QWidget, Ui_ModifyData):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class OldProjectConfigs(QWidget, Ui_OldProjectConfigsPage):
    def __init__(self, parent=None, projectFile=None):
        super().__init__(parent)
        self.projectFile = projectFile
        self.setupUi(self)

        self.open_project()
        self.show_equipments()

    def open_project(self):
        self.projectFolder, self.imageFile, self.dbFile, self.configsFolder = Project().load_project(self.projectFile)

        # return self.projectFolder, self.imageFile, self.dbFile, self.configsFolder

    def get_equipments(self):
        equipments = TopologyData().get_all_equipments(self.dbFile)
        return equipments

    def show_equipments(self):
        
        # Aquisition des equipements presents dans l'architecture
        equipments = self.get_equipments()

        # Create a widget to hold the list
        content_widget = QWidget()
        layout = QVBoxLayout(content_widget)

        # Loop through your list and add widgets
        if equipments:
            for equipment in equipments:
                btn = QPushButton(equipment)
                layout.addWidget(btn)
                btn.clicked.connect(lambda checked, name=equipment: self.show_configs(name))

            # Set the content widget as the scroll area's widget
            self.equipmentsScrollArea.setWidget(content_widget)
            self.equipmentsScrollArea.setWidgetResizable(True)

    def show_configs(self, equipmentName):
        configsFile = Configurations().get_equipment_config_file(equipmentName, self.projectFolder)
        self.configurationPage = ConfigurationPage(configsFile)
        

class ConfigurationPage(QWidget, Ui_Configuration):
    def __init__(self, parent=None, configsFile=None):
        super().__init__(parent)
        self.configsFile = configsFile
        self.setupUi(self)

    def show_configs_file_content(self):
        if self.configsFile and os.path.exists(self.configsFile):
            with open(self.configsFile, "r", encoding="utf-8") as configsText:
                commands = configsText.read()
            self.textBrowser.setPlainText(commands)
        else:
            self.textBrowser.setPlainText("No configuration file found.")


class DataExtraction(QDialog, Ui_DataExtraction):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class Worker(QObject):
    def __init__(self, parent=None, appData=None):
        super().__init__(parent)
        self.appData = appData
        self.imagePath = self.appData.imagePath
        self.currentProjectPath = self.appData.currentProjectPath

    progress = Signal(int)
    finished = Signal()

    def run(self):
        TopologyData().process(self.imagePath, self.currentProjectPath)
        self.finished.emit()


class AppData:
    def __init__(self):
        self.imagePath = None
        self.selectedDirectory = None
        self.projectTitle = None
        self.currentProjectPath = None


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())