# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save_dialog_view.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SaveDialog(object):
    def setupUi(self, SaveDialog):
        SaveDialog.setObjectName("SaveDialog")
        SaveDialog.resize(368, 165)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SaveDialog.sizePolicy().hasHeightForWidth())
        SaveDialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(SaveDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(SaveDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(SaveDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_4 = QtWidgets.QLabel(SaveDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.label_3 = QtWidgets.QLabel(SaveDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_5 = QtWidgets.QLabel(SaveDialog)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_5)
        self.lineEdit = QtWidgets.QLineEdit(SaveDialog)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(SaveDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SaveDialog)
        self.buttonBox.accepted.connect(SaveDialog.accept)
        self.buttonBox.rejected.connect(SaveDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SaveDialog)

    def retranslateUi(self, SaveDialog):
        _translate = QtCore.QCoreApplication.translate
        SaveDialog.setWindowTitle(_translate("SaveDialog", "Dialog"))
        self.label.setText(_translate("SaveDialog", "Name:"))
        self.label_2.setText(_translate("SaveDialog", "Score (sec):"))
        self.label_4.setText(_translate("SaveDialog", "123"))
        self.label_3.setText(_translate("SaveDialog", "Date:"))
        self.label_5.setText(_translate("SaveDialog", "datetime"))

