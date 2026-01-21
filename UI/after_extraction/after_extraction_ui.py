# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'after_extraction.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
from .. icons import logo_rc

class Ui_AfterExtraction(object):
    def setupUi(self, AfterExtraction):
        if not AfterExtraction.objectName():
            AfterExtraction.setObjectName(u"AfterExtraction")
        AfterExtraction.resize(732, 514)
        icon = QIcon()
        icon.addFile(u":/mainLogo/Network App Logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        AfterExtraction.setWindowIcon(icon)
        self.gridLayout = QGridLayout(AfterExtraction)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(AfterExtraction)
        self.widget.setObjectName(u"widget")
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(16)
        self.label.setFont(font)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.widget_2 = QWidget(self.groupBox)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 1, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_2.addWidget(self.pushButton_2, 1, 2, 1, 1)

        self.pushButton_3 = QPushButton(self.widget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_2.addWidget(self.pushButton_3, 1, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)


        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.widget_2)

        self.scrollArea = QScrollArea(self.groupBox)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 668, 210))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_3 = QWidget(self.scrollAreaWidgetContents)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.groupBox_2 = QGroupBox(self.widget_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_3)


        self.verticalLayout_4.addLayout(self.formLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)


        self.verticalLayout_2.addWidget(self.groupBox_2)


        self.verticalLayout.addWidget(self.widget_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.scrollArea)


        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)


        self.retranslateUi(AfterExtraction)

        QMetaObject.connectSlotsByName(AfterExtraction)
    # setupUi

    def retranslateUi(self, AfterExtraction):
        AfterExtraction.setWindowTitle(QCoreApplication.translate("AfterExtraction", u"After Extraction", None))
        self.label.setText(QCoreApplication.translate("AfterExtraction", u"Donnees extraites de l'image", None))
        self.groupBox.setTitle("")
        self.pushButton.setText(QCoreApplication.translate("AfterExtraction", u"Confirmer", None))
        self.pushButton_3.setText(QCoreApplication.translate("AfterExtraction", u"Continuer", None))
        self.label_2.setText(QCoreApplication.translate("AfterExtraction", u"TextLabel", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("AfterExtraction", u"Interface e0", None))
        self.lineEdit.setText(QCoreApplication.translate("AfterExtraction", u"ip address", None))
        self.label_3.setText(QCoreApplication.translate("AfterExtraction", u"ip:", None))
    # retranslateUi

