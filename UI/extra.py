import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QGuiApplication



class HomeWindow(QWidget):

  def __init__(self):
    super().__init__()
    self.initializeUI()

  def initializeUI(self):
    self.setMinimumSize(400, 300)
    screen = QGuiApplication.primaryScreen().geometry()
    self.setMaximumSize(screen.width(), screen.height())
    self.setWindowTitle("Home Window")
    self.homeWindowView()
    self.show()

  def homeWindowView(self):

    image = "images/image.jpeg"

    ### Widgets ####
    ################
    # Search bar for projects

    searchProject = QLineEdit(self)
    searchProject.setPlaceholderText("Project Search")
    searchProject.resize(250, 40)
    searchProject.move(75, 30)

    # Recent project image and name

    # recentProjectBox = QVBoxLayout()
    recentProjectsBox = QHBoxLayout()
    recentProjectsBox.setSizeConstraint

    recentProjectBoxList = ["", "", "", "", ""]

    for i in range(0, 4):
      print(i)
      try:
        with open(image):
          recentProjectImage = QLabel(self)
          pixmap = QPixmap(image)
          recentProjectImage.setPixmap(pixmap)
          recentProjectImage.resize(100, 130)
          recentProjectImage.move(25, 90)

      except FileNotFoundError as error:
        print(f"Image not found.\nError: {error}")

      recentProjectName = QLabel(self)
      recentProjectName.setText("Recent Projects")

      # recentProjectBox = recentProjectBoxList[i]
      recentProjectBoxList[i] = QVBoxLayout()
      recentProjectBox = recentProjectBoxList[i]
      
      recentProjectBox.addWidget(recentProjectImage)
      recentProjectBox.addWidget(recentProjectName)
      recentProjectBoxList.append(recentProjectBox)


    for box in recentProjectBoxList:
      if box:
        recentProjectsBox.addLayout(box)

    # Projects names

    projects = ["Project 1", "Project 2", "Project 3", "Project 4"]


    # Layout des projets

    projectsBox = QVBoxLayout()
    for projectName in projects:
      project = QLabel(self)
      project.setText(projectName)
      projectsBox.addWidget(project)

    # Layout pour la page d'accueil

    homePage = QVBoxLayout()
    homePage.addWidget(searchProject)
    homePage.addLayout(recentProjectsBox)
    homePage.addLayout(projectsBox)
    homePage.setContentsMargins(20, 20, 20, 20)
    homePage.setSpacing(10)
    homePage.setAlignment(searchProject, Qt.AlignmentFlag.AlignHCenter)
    self.setLayout(homePage)

app = QApplication(sys.argv)
window = HomeWindow()
sys.exit(app.exec())