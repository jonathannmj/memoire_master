# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'open_project.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)
from .. icons import logo_rc

class Ui_OpenProject(object):
    def setupUi(self, OpenProject):
        if not OpenProject.objectName():
            OpenProject.setObjectName(u"OpenProject")
        OpenProject.resize(845, 538)
        self.gridLayout = QGridLayout(OpenProject)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_2 = QFrame(OpenProject)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 4, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 2, 1, 1, 5)

        self.closeProjectFormButton = QPushButton(self.frame_2)
        self.closeProjectFormButton.setObjectName(u"closeProjectFormButton")

        self.gridLayout_3.addWidget(self.closeProjectFormButton, 4, 5, 1, 1)

        self.recentProjectsCombo = QComboBox(self.frame_2)
        self.recentProjectsCombo.addItem("")
        self.recentProjectsCombo.setObjectName(u"recentProjectsCombo")

        self.gridLayout_3.addWidget(self.recentProjectsCombo, 4, 4, 1, 1)

        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.projectTitleField = QLineEdit(self.groupBox)
        self.projectTitleField.setObjectName(u"projectTitleField")
        self.projectTitleField.setStyleSheet(u"padding: 5px")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.projectTitleField)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.changeFileDestinationButton = QPushButton(self.groupBox_2)
        self.changeFileDestinationButton.setObjectName(u"changeFileDestinationButton")

        self.gridLayout_2.addWidget(self.changeFileDestinationButton, 0, 1, 1, 1)

        self.projectDestinationCombo = QComboBox(self.groupBox_2)
        self.projectDestinationCombo.addItem("")
        self.projectDestinationCombo.setObjectName(u"projectDestinationCombo")

        self.gridLayout_2.addWidget(self.projectDestinationCombo, 0, 0, 1, 1)


        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.groupBox_2)


        self.gridLayout_3.addWidget(self.groupBox, 3, 1, 1, 5, Qt.AlignmentFlag.AlignVCenter)

        self.createProjectButton = QPushButton(self.frame_2)
        self.createProjectButton.setObjectName(u"createProjectButton")

        self.gridLayout_3.addWidget(self.createProjectButton, 4, 2, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 5, 1, 1, 5)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(20)
        font.setBold(True)
        self.label_3.setFont(font)

        self.gridLayout_3.addWidget(self.label_3, 1, 1, 1, 5)

        self.openAProjectButton = QPushButton(self.frame_2)
        self.openAProjectButton.setObjectName(u"openAProjectButton")

        self.gridLayout_3.addWidget(self.openAProjectButton, 4, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 0, 1, 1, 5)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 6, 1, 1, 5)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u":/mainLogo/Network App Logo.png"))

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 7, 1)


        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)


        self.retranslateUi(OpenProject)

        QMetaObject.connectSlotsByName(OpenProject)
    # setupUi

    def retranslateUi(self, OpenProject):
        OpenProject.setWindowTitle(QCoreApplication.translate("OpenProject", u"Form", None))
        self.closeProjectFormButton.setText(QCoreApplication.translate("OpenProject", u"Fermer", None))
        self.recentProjectsCombo.setItemText(0, QCoreApplication.translate("OpenProject", u"Recent", None))

        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("OpenProject", u"Titre du Projet:", None))
        self.label_2.setText(QCoreApplication.translate("OpenProject", u"Destination:", None))
        self.groupBox_2.setTitle("")
        self.changeFileDestinationButton.setText(QCoreApplication.translate("OpenProject", u"Changer", None))
        self.projectDestinationCombo.setItemText(0, QCoreApplication.translate("OpenProject", u"C:\\NmjNetworkAutomationTool\\Projects", None))

        self.createProjectButton.setText(QCoreApplication.translate("OpenProject", u"Creer", None))
        self.label_3.setText(QCoreApplication.translate("OpenProject", u"Ouvrir un Projet", None))
        self.openAProjectButton.setText(QCoreApplication.translate("OpenProject", u"Ouvrir", None))
        self.label_4.setText("")
    # retranslateUi

