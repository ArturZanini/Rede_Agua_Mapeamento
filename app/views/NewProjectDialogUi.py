# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_project_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewProjectDialog(object):
    def setupUi(self, NewProjectDialog):
        NewProjectDialog.setObjectName("NewProjectDialog")
        NewProjectDialog.resize(624, 356)
        self.formLayout = QtWidgets.QFormLayout(NewProjectDialog)
        self.formLayout.setObjectName("formLayout")
        self.titleLabel = QtWidgets.QLabel(NewProjectDialog)
        self.titleLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.titleLabel.setObjectName("titleLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.titleLabel)
        self.projectNameLabel_2 = QtWidgets.QLabel(NewProjectDialog)
        self.projectNameLabel_2.setObjectName("projectNameLabel_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.projectNameLabel_2)
        self.projectNameEdit = QtWidgets.QLineEdit(NewProjectDialog)
        self.projectNameEdit.setObjectName("projectNameEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.projectNameEdit)
        self.countryLabel = QtWidgets.QLabel(NewProjectDialog)
        self.countryLabel.setObjectName("countryLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.countryLabel)
        self.countryEdit = QtWidgets.QLineEdit(NewProjectDialog)
        self.countryEdit.setObjectName("countryEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.countryEdit)
        self.cityLabel = QtWidgets.QLabel(NewProjectDialog)
        self.cityLabel.setObjectName("cityLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.cityLabel)
        self.cityEdit = QtWidgets.QLineEdit(NewProjectDialog)
        self.cityEdit.setObjectName("cityEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.cityEdit)
        self.microsystemLabel = QtWidgets.QLabel(NewProjectDialog)
        self.microsystemLabel.setObjectName("microsystemLabel")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.microsystemLabel)
        self.microsystemEdit = QtWidgets.QLineEdit(NewProjectDialog)
        self.microsystemEdit.setObjectName("microsystemEdit")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.microsystemEdit)
        self.authorLabel = QtWidgets.QLabel(NewProjectDialog)
        self.authorLabel.setObjectName("authorLabel")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.authorLabel)
        self.authorEdit = QtWidgets.QLineEdit(NewProjectDialog)
        self.authorEdit.setObjectName("authorEdit")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.authorEdit)
        self.dateLabel = QtWidgets.QLabel(NewProjectDialog)
        self.dateLabel.setObjectName("dateLabel")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.dateLabel)
        self.dateEdit = QtWidgets.QDateEdit(NewProjectDialog)
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewProjectDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.buttonBox)

        self.retranslateUi(NewProjectDialog)
        self.buttonBox.accepted.connect(NewProjectDialog.accept)
        self.buttonBox.rejected.connect(NewProjectDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NewProjectDialog)

    def retranslateUi(self, NewProjectDialog):
        _translate = QtCore.QCoreApplication.translate
        NewProjectDialog.setWindowTitle(_translate("NewProjectDialog", "SANIBIDapp"))
        self.titleLabel.setText(_translate("NewProjectDialog", "Crear Nuevo Proyecto"))
        self.projectNameLabel_2.setText(_translate("NewProjectDialog", "Nombre Proyecto"))
        self.countryLabel.setText(_translate("NewProjectDialog", "País"))
        self.cityLabel.setText(_translate("NewProjectDialog", "Ciudad"))
        self.microsystemLabel.setText(_translate("NewProjectDialog", "Subcuenca"))
        self.authorLabel.setText(_translate("NewProjectDialog", "Autor"))
        self.dateLabel.setText(_translate("NewProjectDialog", "Fecha"))
