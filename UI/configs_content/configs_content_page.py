# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configs_old_project.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QGridLayout, QLabel, QListWidget, QTextEdit,
    QVBoxLayout, QHBoxLayout, QFrame, QSizePolicy, QWidget)

class Ui_ConfigsContentPage(object):
    def setupUi(self, ConfigsContentPage):
        if not ConfigsContentPage.objectName():
            ConfigsContentPage.setObjectName(u"ConfigsContentPage")
        ConfigsContentPage.resize(1152, 668)
        
        # Main Layout
        self.gridLayout = QGridLayout(ConfigsContentPage)
        self.gridLayout.setObjectName(u"gridLayout")
        
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        
        # Header
        self.headerLabel = QLabel(ConfigsContentPage)
        self.headerLabel.setObjectName(u"headerLabel")
        font_header = QFont()
        font_header.setBold(True)
        font_header.setItalic(True)
        font_header.setPointSize(16)
        self.headerLabel.setFont(font_header)
        self.headerLabel.setAlignment(Qt.AlignCenter)
        self.mainLayout.addWidget(self.headerLabel)
        
        # Content Body
        self.contentLayout = QHBoxLayout()
        self.contentLayout.setObjectName(u"contentLayout")
        
        # Left Panel (Equipements)
        self.leftPanel = QVBoxLayout()
        self.leftPanel.setObjectName(u"leftPanel")
        
        self.equipmentsLabel = QLabel(ConfigsContentPage)
        self.equipmentsLabel.setObjectName(u"equipmentsLabel")
        font_subheader = QFont()
        font_subheader.setBold(True)
        font_subheader.setItalic(True)
        font_subheader.setPointSize(12)
        self.equipmentsLabel.setFont(font_subheader)
        self.equipmentsLabel.setAlignment(Qt.AlignCenter)
        self.leftPanel.addWidget(self.equipmentsLabel)
        
        self.equipmentList = QListWidget(ConfigsContentPage)
        self.equipmentList.setObjectName(u"equipmentList")
        self.leftPanel.addWidget(self.equipmentList)
        
        # Set stretch for left panel components
        self.contentLayout.addLayout(self.leftPanel, 1) # Stretch factor 1
        
        # Right Panel (Configurations)
        self.rightPanel = QVBoxLayout()
        self.rightPanel.setObjectName(u"rightPanel")
        
        self.configsLabel = QLabel(ConfigsContentPage)
        self.configsLabel.setObjectName(u"configsLabel")
        self.configsLabel.setFont(font_subheader) # Reusing subheader font
        self.configsLabel.setAlignment(Qt.AlignCenter)
        self.rightPanel.addWidget(self.configsLabel)
        
        self.configTextEdit = QTextEdit(ConfigsContentPage)
        self.configTextEdit.setObjectName(u"configTextEdit")
        self.configTextEdit.setReadOnly(True)
        self.rightPanel.addWidget(self.configTextEdit)
        
        # Set stretch for right panel components
        self.contentLayout.addLayout(self.rightPanel, 3) # Stretch factor 3 (wider than list)
        
        self.mainLayout.addLayout(self.contentLayout)
        self.gridLayout.addLayout(self.mainLayout, 0, 0, 1, 1)

        self.retranslateUi(ConfigsContentPage)

        QMetaObject.connectSlotsByName(ConfigsContentPage)

    def retranslateUi(self, ConfigsContentPage):
        ConfigsContentPage.setWindowTitle(QCoreApplication.translate("ConfigsContentPage", u"Form", None))
        self.headerLabel.setText(QCoreApplication.translate("ConfigsContentPage", u"Configurations generees", None))
        self.equipmentsLabel.setText(QCoreApplication.translate("ConfigsContentPage", u"Equipements", None))

        # self.configsLabel.setText(QCoreApplication.translate("ConfigsContentPage", u"Configurations", None))

