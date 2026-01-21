# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'image_import.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLayout, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
from .. icons import logo_rc

class Ui_ImportImage(object):
    def setupUi(self, ImportImage):
        if not ImportImage.objectName():
            ImportImage.setObjectName(u"ImportImage")
        ImportImage.resize(841, 604)
        icon = QIcon()
        icon.addFile(u":/mainLogo/Network App Logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        ImportImage.setWindowIcon(icon)
        ImportImage.setLocale(QLocale(QLocale.French, QLocale.France))
        self.gridLayout = QGridLayout(ImportImage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(ImportImage)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.importImageButton = QPushButton(self.widget)
        self.importImageButton.setObjectName(u"importImageButton")
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift"])
        font1.setPointSize(12)
        self.importImageButton.setFont(font1)
        self.importImageButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.importImageButton.setStyleSheet(u"padding:15px 30px;\n"
"background-color:rgb(85, 0, 127);\n"
"color: white;\n"
"border-radius: 20px;")
        self.importImageButton.setIconSize(QSize(18, 18))

        self.horizontalLayout.addWidget(self.importImageButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.widget)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)


        self.retranslateUi(ImportImage)

        QMetaObject.connectSlotsByName(ImportImage)
    # setupUi

    def retranslateUi(self, ImportImage):
        ImportImage.setWindowTitle(QCoreApplication.translate("ImportImage", u"Importer une Image de l'Architecture", None))
        self.groupBox.setTitle(QCoreApplication.translate("ImportImage", u"Importer une Image", None))
        self.label.setText(QCoreApplication.translate("ImportImage", u"Importer une Image", None))
        self.label_2.setText(QCoreApplication.translate("ImportImage", u"representant l'architecture du reseau", None))
        self.importImageButton.setText(QCoreApplication.translate("ImportImage", u"Importer", None))
    # retranslateUi

