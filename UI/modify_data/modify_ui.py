# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modify.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
from .. icons import logo_rc

class Ui_ModifyData(object):
    def setupUi(self, ModifyData):
        if not ModifyData.objectName():
            ModifyData.setObjectName(u"ModifyData")
        ModifyData.resize(671, 520)
        icon = QIcon()
        icon.addFile(u":/mainLogo/Network App Logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        ModifyData.setWindowIcon(icon)
        self.gridLayout = QGridLayout(ModifyData)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(ModifyData)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 651, 446))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.equipmentTable = QTableWidget(self.frame)
        if (self.equipmentTable.columnCount() < 5):
            self.equipmentTable.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.equipmentTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.equipmentTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.equipmentTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.equipmentTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.equipmentTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.equipmentTable.setObjectName(u"equipmentTable")
        self.equipmentTable.setStyleSheet(u"width:fit-content;")

        self.verticalLayout_2.addWidget(self.equipmentTable)


        self.verticalLayout.addWidget(self.frame)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.equipmentTable_3 = QTableWidget(self.frame_3)
        if (self.equipmentTable_3.columnCount() < 5):
            self.equipmentTable_3.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.equipmentTable_3.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.equipmentTable_3.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.equipmentTable_3.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.equipmentTable_3.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.equipmentTable_3.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        self.equipmentTable_3.setObjectName(u"equipmentTable_3")
        self.equipmentTable_3.setStyleSheet(u"width:fit-content;")

        self.verticalLayout_4.addWidget(self.equipmentTable_3)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.equipmentTable_2 = QTableWidget(self.frame_2)
        if (self.equipmentTable_2.columnCount() < 5):
            self.equipmentTable_2.setColumnCount(5)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.equipmentTable_2.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.equipmentTable_2.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.equipmentTable_2.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.equipmentTable_2.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.equipmentTable_2.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        self.equipmentTable_2.setObjectName(u"equipmentTable_2")
        self.equipmentTable_2.setStyleSheet(u"width:fit-content;")

        self.verticalLayout_3.addWidget(self.equipmentTable_2)


        self.verticalLayout.addWidget(self.frame_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 0, 1, 1)

        self.pushButton = QPushButton(ModifyData)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 2, 2, 1, 1)

        self.pushButton_2 = QPushButton(ModifyData)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 1)

        self.label_4 = QLabel(ModifyData)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(True)
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 3)


        self.retranslateUi(ModifyData)

        QMetaObject.connectSlotsByName(ModifyData)
    # setupUi

    def retranslateUi(self, ModifyData):
        ModifyData.setWindowTitle(QCoreApplication.translate("ModifyData", u"Modifier les Informations", None))
        self.label.setText(QCoreApplication.translate("ModifyData", u"Equipement", None))
        ___qtablewidgetitem = self.equipmentTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ModifyData", u"Interface", None));
        ___qtablewidgetitem1 = self.equipmentTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ModifyData", u"IP", None));
        ___qtablewidgetitem2 = self.equipmentTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ModifyData", u"Mode", None));
        ___qtablewidgetitem3 = self.equipmentTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ModifyData", u"Network", None));
        ___qtablewidgetitem4 = self.equipmentTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ModifyData", u"Gateway", None));
        self.label_3.setText(QCoreApplication.translate("ModifyData", u"Equipement", None))
        ___qtablewidgetitem5 = self.equipmentTable_3.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("ModifyData", u"Interface", None));
        ___qtablewidgetitem6 = self.equipmentTable_3.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("ModifyData", u"IP", None));
        ___qtablewidgetitem7 = self.equipmentTable_3.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("ModifyData", u"Mode", None));
        ___qtablewidgetitem8 = self.equipmentTable_3.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("ModifyData", u"Network", None));
        ___qtablewidgetitem9 = self.equipmentTable_3.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("ModifyData", u"Gateway", None));
        self.label_2.setText(QCoreApplication.translate("ModifyData", u"Equipement", None))
        ___qtablewidgetitem10 = self.equipmentTable_2.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("ModifyData", u"Interface", None));
        ___qtablewidgetitem11 = self.equipmentTable_2.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("ModifyData", u"IP", None));
        ___qtablewidgetitem12 = self.equipmentTable_2.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("ModifyData", u"Mode", None));
        ___qtablewidgetitem13 = self.equipmentTable_2.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("ModifyData", u"Network", None));
        ___qtablewidgetitem14 = self.equipmentTable_2.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("ModifyData", u"Gateway", None));
        self.pushButton.setText(QCoreApplication.translate("ModifyData", u"Annuler", None))
        self.pushButton_2.setText(QCoreApplication.translate("ModifyData", u"Modifier", None))
        self.label_4.setText(QCoreApplication.translate("ModifyData", u"Informations Extraites de l'Image, representees par equipement", None))
    # retranslateUi

