# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'data_extracting.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QProgressBar, QSizePolicy, QWidget)

class Ui_DataExtraction(object):
    def setupUi(self, DataExtraction):
        if not DataExtraction.objectName():
            DataExtraction.setObjectName(u"DataExtraction")
        DataExtraction.setWindowModality(Qt.WindowModality.ApplicationModal)
        DataExtraction.resize(434, 87)
        self.gridLayout = QGridLayout(DataExtraction)
        self.gridLayout.setObjectName(u"gridLayout")
        self.progressBar = QProgressBar(DataExtraction)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 0))
        self.progressBar.setMaximum(0)
        self.progressBar.setValue(-1)

        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 1)

        self.label = QLabel(DataExtraction)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(16)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.retranslateUi(DataExtraction)

        QMetaObject.connectSlotsByName(DataExtraction)
    # setupUi

    def retranslateUi(self, DataExtraction):
        DataExtraction.setWindowTitle(QCoreApplication.translate("DataExtraction", u"DataExtraction", None))
        self.label.setText(QCoreApplication.translate("DataExtraction", u"Extraction des donnees en cours", None))
    # retranslateUi

