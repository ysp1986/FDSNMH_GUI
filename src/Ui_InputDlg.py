# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/InputDlg.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_InputDlg(object):
    def setupUi(self, InputDlg):
        InputDlg.setObjectName("InputDlg")
        InputDlg.setEnabled(True)
        InputDlg.resize(717, 515)
        InputDlg.setMinimumSize(QtCore.QSize(700, 500))
        InputDlg.setToolTip("")
        InputDlg.setSizeGripEnabled(False)
        InputDlg.setModal(False)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(InputDlg)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_4.setSpacing(9)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_3 = QtWidgets.QGroupBox(InputDlg)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.textMaterialSearch = QtWidgets.QLineEdit(self.groupBox_3)
        self.textMaterialSearch.setObjectName("textMaterialSearch")
        self.horizontalLayout_2.addWidget(self.textMaterialSearch)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        self.listWidgetMaterialLib = QtWidgets.QListWidget(self.groupBox_3)
        self.listWidgetMaterialLib.setObjectName("listWidgetMaterialLib")
        self.verticalLayout_7.addWidget(self.listWidgetMaterialLib)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButtonDeleteMatFromLib = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButtonDeleteMatFromLib.setObjectName("pushButtonDeleteMatFromLib")
        self.horizontalLayout_5.addWidget(self.pushButtonDeleteMatFromLib)
        self.pushButtonUpdateMaterialLib = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButtonUpdateMaterialLib.setObjectName("pushButtonUpdateMaterialLib")
        self.horizontalLayout_5.addWidget(self.pushButtonUpdateMaterialLib)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.verticalLayout_7.addWidget(self.label)
        self.tableWidgetSelectedMatComposition = QTableWidgetMaterial(self.groupBox_3)
        self.tableWidgetSelectedMatComposition.setObjectName("tableWidgetSelectedMatComposition")
        self.tableWidgetSelectedMatComposition.setColumnCount(2)
        self.tableWidgetSelectedMatComposition.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetSelectedMatComposition.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetSelectedMatComposition.setHorizontalHeaderItem(1, item)
        self.tableWidgetSelectedMatComposition.horizontalHeader().setVisible(True)
        self.tableWidgetSelectedMatComposition.horizontalHeader().setDefaultSectionSize(88)
        self.tableWidgetSelectedMatComposition.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetSelectedMatComposition.verticalHeader().setVisible(False)
        self.verticalLayout_7.addWidget(self.tableWidgetSelectedMatComposition)
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.comboBoxSelectSpectra = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxSelectSpectra.setEditable(False)
        self.comboBoxSelectSpectra.setMaxVisibleItems(6)
        self.comboBoxSelectSpectra.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBoxSelectSpectra.setDuplicatesEnabled(True)
        self.comboBoxSelectSpectra.setObjectName("comboBoxSelectSpectra")
        self.verticalLayout_5.addWidget(self.comboBoxSelectSpectra)
        self.verticalLayout_7.addWidget(self.groupBox)
        self.pushButtonShowResult = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButtonShowResult.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButtonShowResult.setObjectName("pushButtonShowResult")
        self.verticalLayout_7.addWidget(self.pushButtonShowResult)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(6, -1, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButtonLoad = QtWidgets.QPushButton(InputDlg)
        self.pushButtonLoad.setObjectName("pushButtonLoad")
        self.verticalLayout_3.addWidget(self.pushButtonLoad)
        self.pushButtonSave = QtWidgets.QPushButton(InputDlg)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.verticalLayout_3.addWidget(self.pushButtonSave)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox_2 = QtWidgets.QGroupBox(InputDlg)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.textMatName = QtWidgets.QLineEdit(self.groupBox_2)
        self.textMatName.setObjectName("textMatName")
        self.horizontalLayout_3.addWidget(self.textMatName)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.tableWidgetMatComposition = QTableWidgetMaterial(self.groupBox_2)
        self.tableWidgetMatComposition.setObjectName("tableWidgetMatComposition")
        self.tableWidgetMatComposition.setColumnCount(2)
        self.tableWidgetMatComposition.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetMatComposition.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetMatComposition.setHorizontalHeaderItem(1, item)
        self.tableWidgetMatComposition.horizontalHeader().setDefaultSectionSize(88)
        self.tableWidgetMatComposition.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetMatComposition.verticalHeader().setVisible(False)
        self.tableWidgetMatComposition.verticalHeader().setMinimumSectionSize(16)
        self.tableWidgetMatComposition.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_6.addWidget(self.tableWidgetMatComposition)
        self.pushButtonClearCurrentMat = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButtonClearCurrentMat.setObjectName("pushButtonClearCurrentMat")
        self.verticalLayout_6.addWidget(self.pushButtonClearCurrentMat)
        self.horizontalLayout_4.addWidget(self.groupBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 8)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 8)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(InputDlg)
        QtCore.QMetaObject.connectSlotsByName(InputDlg)

    def retranslateUi(self, InputDlg):
        _translate = QtCore.QCoreApplication.translate
        InputDlg.setWindowTitle(_translate("InputDlg", "Material Activation Estimator"))
        InputDlg.setWhatsThis(_translate("InputDlg", "<html><head/><body><p>This is the interface program for the Activation Handbook for ITER, developed by the FDS team, named as Material Activation Estimator</p></body></html>"))
        self.groupBox_3.setTitle(_translate("InputDlg", "Material Library"))
        self.label_3.setText(_translate("InputDlg", "Search Material:"))
        self.label_2.setText(_translate("InputDlg", "Material List in Library:"))
        self.listWidgetMaterialLib.setToolTip(_translate("InputDlg", "<html><head/><body><p>This list contains currently cached materials, which can be found in the file in <span style=\" font-weight:600;\">&quot;Data Save/matlist.txt&quot;</span>, in which, each line represent one material\'s components.</p></body></html>"))
        self.pushButtonDeleteMatFromLib.setText(_translate("InputDlg", "Delete Selected Material"))
        self.pushButtonUpdateMaterialLib.setText(_translate("InputDlg", "Update Material Library"))
        self.label.setText(_translate("InputDlg", "Components of Selected Material:"))
        item = self.tableWidgetSelectedMatComposition.horizontalHeaderItem(0)
        item.setText(_translate("InputDlg", "Nuclide"))
        item = self.tableWidgetSelectedMatComposition.horizontalHeaderItem(1)
        item.setText(_translate("InputDlg", "Weight Proportion (%)"))
        self.groupBox.setTitle(_translate("InputDlg", "Choose Spectrum"))
        self.pushButtonShowResult.setText(_translate("InputDlg", "Show Activation Result"))
        self.pushButtonLoad.setText(_translate("InputDlg", ">>>"))
        self.pushButtonSave.setText(_translate("InputDlg", "<<<"))
        self.groupBox_2.setTitle(_translate("InputDlg", "Current Material"))
        self.label_4.setText(_translate("InputDlg", "Edit Material Name:"))
        item = self.tableWidgetMatComposition.horizontalHeaderItem(0)
        item.setText(_translate("InputDlg", "Nuclide"))
        item = self.tableWidgetMatComposition.horizontalHeaderItem(1)
        item.setText(_translate("InputDlg", "Weight Proportion (%)"))
        self.pushButtonClearCurrentMat.setText(_translate("InputDlg", "Clear"))

from qtablewidgetmaterial import QTableWidgetMaterial
