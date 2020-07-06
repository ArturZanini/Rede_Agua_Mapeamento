# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parameter_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewParameterDialog(object):
    def setupUi(self, NewParameterDialog):
        NewParameterDialog.setObjectName("NewParameterDialog")
        NewParameterDialog.resize(839, 828)
        self.gridLayout_3 = QtWidgets.QGridLayout(NewParameterDialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.buttonBox = QtWidgets.QDialogButtonBox(NewParameterDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_3.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.ParametersWidget = QtWidgets.QTabWidget(NewParameterDialog)
        self.ParametersWidget.setAutoFillBackground(False)
        self.ParametersWidget.setMovable(False)
        self.ParametersWidget.setObjectName("ParametersWidget")
        self.parametersLabel = QtWidgets.QWidget()
        self.parametersLabel.setObjectName("parametersLabel")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.parametersLabel)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.qeReferenceMaxLabel = QtWidgets.QLabel(self.parametersLabel)
        self.qeReferenceMaxLabel.setObjectName("qeReferenceMaxLabel")
        self.gridLayout_2.addWidget(self.qeReferenceMaxLabel, 13, 0, 1, 1)
        self.startLabel = QtWidgets.QLabel(self.parametersLabel)
        self.startLabel.setObjectName("startLabel")
        self.gridLayout_2.addWidget(self.startLabel, 0, 1, 1, 1)
        self.qeMaxLabel = QtWidgets.QLabel(self.parametersLabel)
        self.qeMaxLabel.setObjectName("qeMaxLabel")
        self.gridLayout_2.addWidget(self.qeMaxLabel, 12, 1, 1, 1)
        self.unitLabel_8 = QtWidgets.QLabel(self.parametersLabel)
        self.unitLabel_8.setObjectName("unitLabel_8")
        self.gridLayout_2.addWidget(self.unitLabel_8, 10, 4, 1, 1)
        self.populationLabel_3 = QtWidgets.QLabel(self.parametersLabel)
        self.populationLabel_3.setObjectName("populationLabel_3")
        self.gridLayout_2.addWidget(self.populationLabel_3, 3, 4, 1, 1)
        self.beginningPopulationEdit = QtWidgets.QSpinBox(self.parametersLabel)
        self.beginningPopulationEdit.setObjectName("beginningPopulationEdit")
        self.gridLayout_2.addWidget(self.beginningPopulationEdit, 1, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.parametersLabel)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.distributedContributionsLabel_2 = QtWidgets.QLabel(self.groupBox)
        self.distributedContributionsLabel_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.distributedContributionsLabel_2.setWordWrap(False)
        self.distributedContributionsLabel_2.setIndent(7)
        self.distributedContributionsLabel_2.setObjectName("distributedContributionsLabel_2")
        self.gridLayout.addWidget(self.distributedContributionsLabel_2, 3, 1, 1, 1)
        self.image_2 = QtWidgets.QLabel(self.groupBox)
        self.image_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.image_2.setObjectName("image_2")
        self.gridLayout.addWidget(self.image_2, 2, 1, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_2.setAutoRepeat(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 1, 1, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 1, 0, 1, 1)
        self.concentratedContributionsPerBlockLabel = QtWidgets.QLabel(self.groupBox)
        self.concentratedContributionsPerBlockLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.concentratedContributionsPerBlockLabel.setObjectName("concentratedContributionsPerBlockLabel")
        self.gridLayout.addWidget(self.concentratedContributionsPerBlockLabel, 3, 0, 1, 1)
        self.image = QtWidgets.QLabel(self.groupBox)
        self.image.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.image.setObjectName("image")
        self.gridLayout.addWidget(self.image, 2, 0, 1, 1)
        self.distributedContributionsLabel = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.distributedContributionsLabel.setFont(font)
        self.distributedContributionsLabel.setObjectName("distributedContributionsLabel")
        self.gridLayout.addWidget(self.distributedContributionsLabel, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 15, 0, 1, 5)
        self.pointFlowsStartEdit = QtWidgets.QSpinBox(self.parametersLabel)
        self.pointFlowsStartEdit.setReadOnly(True)
        self.pointFlowsStartEdit.setObjectName("pointFlowsStartEdit")
        self.gridLayout_2.addWidget(self.pointFlowsStartEdit, 10, 1, 1, 1)
        self.pointFlowsEndEdit = QtWidgets.QSpinBox(self.parametersLabel)
        self.pointFlowsEndEdit.setReadOnly(True)
        self.pointFlowsEndEdit.setObjectName("pointFlowsEndEdit")
        self.gridLayout_2.addWidget(self.pointFlowsEndEdit, 10, 3, 1, 1)
        self.PopulationLabel = QtWidgets.QLabel(self.parametersLabel)
        self.PopulationLabel.setObjectName("PopulationLabel")
        self.gridLayout_2.addWidget(self.PopulationLabel, 1, 0, 1, 1)
        self.residencesEndEdit = QtWidgets.QSpinBox(self.parametersLabel)
        self.residencesEndEdit.setReadOnly(True)
        self.residencesEndEdit.setObjectName("residencesEndEdit")
        self.gridLayout_2.addWidget(self.residencesEndEdit, 5, 3, 1, 1)
        self.connectionsEndEdit_2 = QtWidgets.QSpinBox(self.parametersLabel)
        self.connectionsEndEdit_2.setObjectName("connectionsEndEdit_2")
        self.gridLayout_2.addWidget(self.connectionsEndEdit_2, 7, 3, 1, 1)
        self.occupancyRateLabel = QtWidgets.QLabel(self.parametersLabel)
        self.occupancyRateLabel.setObjectName("occupancyRateLabel")
        self.gridLayout_2.addWidget(self.occupancyRateLabel, 3, 0, 1, 1)
        self.occupancyRateStartEdit = QtWidgets.QDoubleSpinBox(self.parametersLabel)
        self.occupancyRateStartEdit.setObjectName("occupancyRateStartEdit")
        self.gridLayout_2.addWidget(self.occupancyRateStartEdit, 3, 1, 1, 1)
        self.unitLabel_2 = QtWidgets.QLabel(self.parametersLabel)
        self.unitLabel_2.setObjectName("unitLabel_2")
        self.gridLayout_2.addWidget(self.unitLabel_2, 7, 4, 1, 1)
        self.litersDayLabel = QtWidgets.QLabel(self.parametersLabel)
        self.litersDayLabel.setObjectName("litersDayLabel")
        self.gridLayout_2.addWidget(self.litersDayLabel, 13, 4, 1, 1)
        self.finalPopulationEdit = QtWidgets.QSpinBox(self.parametersLabel)
        self.finalPopulationEdit.setObjectName("finalPopulationEdit")
        self.gridLayout_2.addWidget(self.finalPopulationEdit, 1, 3, 1, 1)
        self.qeMedLabel = QtWidgets.QLabel(self.parametersLabel)
        self.qeMedLabel.setObjectName("qeMedLabel")
        self.gridLayout_2.addWidget(self.qeMedLabel, 12, 3, 1, 1)
        self.connectionsLabel = QtWidgets.QLabel(self.parametersLabel)
        self.connectionsLabel.setObjectName("connectionsLabel")
        self.gridLayout_2.addWidget(self.connectionsLabel, 7, 0, 1, 1)
        self.pointFlowsLabel = QtWidgets.QLabel(self.parametersLabel)
        self.pointFlowsLabel.setObjectName("pointFlowsLabel")
        self.gridLayout_2.addWidget(self.pointFlowsLabel, 10, 0, 1, 1)
        self.residencesStartEdit = QtWidgets.QSpinBox(self.parametersLabel)
        self.residencesStartEdit.setReadOnly(True)
        self.residencesStartEdit.setObjectName("residencesStartEdit")
        self.gridLayout_2.addWidget(self.residencesStartEdit, 5, 1, 1, 1)
        self.connectionsStartEdit = QtWidgets.QSpinBox(self.parametersLabel)
        self.connectionsStartEdit.setObjectName("connectionsStartEdit")
        self.gridLayout_2.addWidget(self.connectionsStartEdit, 7, 1, 1, 1)
        self.populationLabel = QtWidgets.QLabel(self.parametersLabel)
        self.populationLabel.setObjectName("populationLabel")
        self.gridLayout_2.addWidget(self.populationLabel, 1, 4, 1, 1)
        self.sewerContributionRateLabel = QtWidgets.QLabel(self.parametersLabel)
        self.sewerContributionRateLabel.setObjectName("sewerContributionRateLabel")
        self.gridLayout_2.addWidget(self.sewerContributionRateLabel, 17, 0, 1, 1)
        self.qeReferenceMaxEdit = QtWidgets.QDoubleSpinBox(self.parametersLabel)
        self.qeReferenceMaxEdit.setReadOnly(True)
        self.qeReferenceMaxEdit.setObjectName("qeReferenceMaxEdit")
        self.gridLayout_2.addWidget(self.qeReferenceMaxEdit, 13, 3, 1, 1)
        self.qeReferenceMedEdit = QtWidgets.QDoubleSpinBox(self.parametersLabel)
        self.qeReferenceMedEdit.setReadOnly(True)
        self.qeReferenceMedEdit.setObjectName("qeReferenceMedEdit")
        self.gridLayout_2.addWidget(self.qeReferenceMedEdit, 13, 1, 1, 1)
        self.specificContributionsLabel = QtWidgets.QLabel(self.parametersLabel)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.specificContributionsLabel.setFont(font)
        self.specificContributionsLabel.setObjectName("specificContributionsLabel")
        self.gridLayout_2.addWidget(self.specificContributionsLabel, 9, 0, 1, 1)
        self.litersSecondLabel = QtWidgets.QLabel(self.parametersLabel)
        self.litersSecondLabel.setObjectName("litersSecondLabel")
        self.gridLayout_2.addWidget(self.litersSecondLabel, 13, 2, 1, 1)
        self.endLabel = QtWidgets.QLabel(self.parametersLabel)
        self.endLabel.setObjectName("endLabel")
        self.gridLayout_2.addWidget(self.endLabel, 0, 3, 1, 1)
        self.populationConnectionsLabel = QtWidgets.QLabel(self.parametersLabel)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.populationConnectionsLabel.setFont(font)
        self.populationConnectionsLabel.setObjectName("populationConnectionsLabel")
        self.gridLayout_2.addWidget(self.populationConnectionsLabel, 0, 0, 1, 1)
        self.residencesLabel = QtWidgets.QLabel(self.parametersLabel)
        self.residencesLabel.setObjectName("residencesLabel")
        self.gridLayout_2.addWidget(self.residencesLabel, 5, 0, 1, 1)
        self.occupancyRateEndEdit = QtWidgets.QDoubleSpinBox(self.parametersLabel)
        self.occupancyRateEndEdit.setObjectName("occupancyRateEndEdit")
        self.gridLayout_2.addWidget(self.occupancyRateEndEdit, 3, 3, 1, 1)
        self.unitLabel = QtWidgets.QLabel(self.parametersLabel)
        self.unitLabel.setObjectName("unitLabel")
        self.gridLayout_2.addWidget(self.unitLabel, 5, 4, 1, 1)
        self.sewerContributionRateStartEdit = QtWidgets.QDoubleSpinBox(self.parametersLabel)
        self.sewerContributionRateStartEdit.setObjectName("sewerContributionRateStartEdit")
        self.gridLayout_2.addWidget(self.sewerContributionRateStartEdit, 17, 1, 1, 1)
        self.sewerContributionRateEndEdit = QtWidgets.QDoubleSpinBox(self.parametersLabel)
        self.sewerContributionRateEndEdit.setObjectName("sewerContributionRateEndEdit")
        self.gridLayout_2.addWidget(self.sewerContributionRateEndEdit, 17, 3, 1, 1)
        self.litersKilometersLabel = QtWidgets.QLabel(self.parametersLabel)
        self.litersKilometersLabel.setObjectName("litersKilometersLabel")
        self.gridLayout_2.addWidget(self.litersKilometersLabel, 17, 4, 1, 1)
        self.ParametersWidget.addTab(self.parametersLabel, "")
        self.projectCriteriasLabel = QtWidgets.QWidget()
        self.projectCriteriasLabel.setObjectName("projectCriteriasLabel")
        self.formLayout = QtWidgets.QFormLayout(self.projectCriteriasLabel)
        self.formLayout.setObjectName("formLayout")
        self.profileLabel = QtWidgets.QLabel(self.projectCriteriasLabel)
        self.profileLabel.setObjectName("profileLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.profileLabel)
        self.profileComboBox = QtWidgets.QComboBox(self.projectCriteriasLabel)
        self.profileComboBox.setObjectName("profileComboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.profileComboBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.projectCriteriasLabel)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.waterConsumptionPcLabel = QtWidgets.QLabel(self.groupBox_2)
        self.waterConsumptionPcLabel.setObjectName("waterConsumptionPcLabel")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.waterConsumptionPcLabel)
        self.k1DailyLabel = QtWidgets.QLabel(self.groupBox_2)
        self.k1DailyLabel.setObjectName("k1DailyLabel")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.k1DailyLabel)
        self.k2HourlyLabel = QtWidgets.QLabel(self.groupBox_2)
        self.k2HourlyLabel.setObjectName("k2HourlyLabel")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.k2HourlyLabel)
        self.coefficientReturnCLabel = QtWidgets.QLabel(self.groupBox_2)
        self.coefficientReturnCLabel.setObjectName("coefficientReturnCLabel")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.coefficientReturnCLabel)
        self.intakeRateLabel = QtWidgets.QLabel(self.groupBox_2)
        self.intakeRateLabel.setObjectName("intakeRateLabel")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.intakeRateLabel)
        self.avgTractiveForceLabel = QtWidgets.QLabel(self.groupBox_2)
        self.avgTractiveForceLabel.setObjectName("avgTractiveForceLabel")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.avgTractiveForceLabel)
        self.flowMinQminLabel = QtWidgets.QLabel(self.groupBox_2)
        self.flowMinQminLabel.setObjectName("flowMinQminLabel")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.flowMinQminLabel)
        self.waterSurfaceMaxLabel = QtWidgets.QLabel(self.groupBox_2)
        self.waterSurfaceMaxLabel.setObjectName("waterSurfaceMaxLabel")
        self.formLayout_2.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.waterSurfaceMaxLabel)
        self.maxWaterLevelLabel = QtWidgets.QLabel(self.groupBox_2)
        self.maxWaterLevelLabel.setObjectName("maxWaterLevelLabel")
        self.formLayout_2.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.maxWaterLevelLabel)
        self.parametersHydraulicCalculationLabel = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.parametersHydraulicCalculationLabel.setFont(font)
        self.parametersHydraulicCalculationLabel.setObjectName("parametersHydraulicCalculationLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.parametersHydraulicCalculationLabel)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_2)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_3)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_4)
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_5)
        self.doubleSpinBox_6 = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_6)
        self.doubleSpinBox_7 = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_7.setObjectName("doubleSpinBox_7")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_7)
        self.doubleSpinBox_8 = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_8.setObjectName("doubleSpinBox_8")
        self.formLayout_2.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_8)
        self.doubleSpinBox_9 = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_9.setObjectName("doubleSpinBox_9")
        self.formLayout_2.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_9)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.projectCriteriasLabel)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupBox_3)
        self.formLayout_3.setObjectName("formLayout_3")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.formLayout_3.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.gridLayout_5)
        self.diametersLabel = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.diametersLabel.setFont(font)
        self.diametersLabel.setObjectName("diametersLabel")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.diametersLabel)
        self.minDiameterLabel = QtWidgets.QLabel(self.groupBox_3)
        self.minDiameterLabel.setObjectName("minDiameterLabel")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.minDiameterLabel)
        self.minDiameterLineEdit = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.minDiameterLineEdit.setAcceptDrops(True)
        self.minDiameterLineEdit.setObjectName("minDiameterLineEdit")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.minDiameterLineEdit)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.groupBox_3)
        self.newProfileGroupBox = QtWidgets.QGroupBox(self.projectCriteriasLabel)
        self.newProfileGroupBox.setObjectName("newProfileGroupBox")
        self.formLayout_4 = QtWidgets.QFormLayout(self.newProfileGroupBox)
        self.formLayout_4.setObjectName("formLayout_4")
        self.profileName = QtWidgets.QLineEdit(self.newProfileGroupBox)
        self.profileName.setObjectName("profileName")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.profileName)
        self.profileNameLabel = QtWidgets.QLabel(self.newProfileGroupBox)
        self.profileNameLabel.setObjectName("profileNameLabel")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.profileNameLabel)
        self.pushButton = QtWidgets.QPushButton(self.newProfileGroupBox)
        self.pushButton.setObjectName("pushButton")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.pushButton)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.newProfileGroupBox)
        self.ParametersWidget.addTab(self.projectCriteriasLabel, "")
        self.pipesLabel = QtWidgets.QWidget()
        self.pipesLabel.setObjectName("pipesLabel")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.pipesLabel)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pipesWidget = QtWidgets.QTableWidget(self.pipesLabel)
        self.pipesWidget.setObjectName("pipesWidget")
        self.pipesWidget.setColumnCount(4)
        self.pipesWidget.setRowCount(11)
        item = QtWidgets.QTableWidgetItem()
        self.pipesWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.pipesWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.pipesWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.pipesWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.pipesWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.pipesWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.pipesWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.pipesWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.pipesWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.pipesWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.pipesWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.pipesWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.pipesWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.pipesWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.pipesWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.pipesWidget.setItem(0, 1, item)
        self.gridLayout_4.addWidget(self.pipesWidget, 0, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.pipesLabel)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_7.setContentsMargins(9, 12, -1, -1)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_7.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_7.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_4, 0, 1, 1, 1)
        self.ParametersWidget.addTab(self.pipesLabel, "")
        self.inspectionDevicesLabel = QtWidgets.QWidget()
        self.inspectionDevicesLabel.setObjectName("inspectionDevicesLabel")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.inspectionDevicesLabel)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.inspectionDevicesWidget = QtWidgets.QTableWidget(self.inspectionDevicesLabel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inspectionDevicesWidget.sizePolicy().hasHeightForWidth())
        self.inspectionDevicesWidget.setSizePolicy(sizePolicy)
        self.inspectionDevicesWidget.setAutoScrollMargin(16)
        self.inspectionDevicesWidget.setObjectName("inspectionDevicesWidget")
        self.inspectionDevicesWidget.setColumnCount(3)
        self.inspectionDevicesWidget.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.inspectionDevicesWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.inspectionDevicesWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.inspectionDevicesWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.inspectionDevicesWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.inspectionDevicesWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.inspectionDevicesWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.inspectionDevicesWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.inspectionDevicesWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.inspectionDevicesWidget.setHorizontalHeaderItem(2, item)
        self.gridLayout_8.addWidget(self.inspectionDevicesWidget, 0, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.inspectionDevicesLabel)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_9.addWidget(self.pushButton_4, 0, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_9.addWidget(self.pushButton_5, 1, 0, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_5, 0, 1, 1, 1)
        self.ParametersWidget.addTab(self.inspectionDevicesLabel, "")
        self.gridLayout_3.addWidget(self.ParametersWidget, 0, 0, 1, 1)

        self.retranslateUi(NewParameterDialog)
        self.ParametersWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(NewParameterDialog.accept)
        self.buttonBox.rejected.connect(NewParameterDialog.reject)
        self.buttonBox.clicked['QAbstractButton*'].connect(NewParameterDialog.open)
        QtCore.QMetaObject.connectSlotsByName(NewParameterDialog)
        NewParameterDialog.setTabOrder(self.beginningPopulationEdit, self.finalPopulationEdit)
        NewParameterDialog.setTabOrder(self.finalPopulationEdit, self.occupancyRateStartEdit)
        NewParameterDialog.setTabOrder(self.occupancyRateStartEdit, self.occupancyRateEndEdit)
        NewParameterDialog.setTabOrder(self.occupancyRateEndEdit, self.residencesStartEdit)
        NewParameterDialog.setTabOrder(self.residencesStartEdit, self.residencesEndEdit)
        NewParameterDialog.setTabOrder(self.residencesEndEdit, self.connectionsStartEdit)
        NewParameterDialog.setTabOrder(self.connectionsStartEdit, self.connectionsEndEdit_2)
        NewParameterDialog.setTabOrder(self.connectionsEndEdit_2, self.pointFlowsStartEdit)
        NewParameterDialog.setTabOrder(self.pointFlowsStartEdit, self.pointFlowsEndEdit)
        NewParameterDialog.setTabOrder(self.pointFlowsEndEdit, self.qeReferenceMedEdit)
        NewParameterDialog.setTabOrder(self.qeReferenceMedEdit, self.qeReferenceMaxEdit)
        NewParameterDialog.setTabOrder(self.qeReferenceMaxEdit, self.radioButton)
        NewParameterDialog.setTabOrder(self.radioButton, self.radioButton_2)
        NewParameterDialog.setTabOrder(self.radioButton_2, self.sewerContributionRateStartEdit)
        NewParameterDialog.setTabOrder(self.sewerContributionRateStartEdit, self.sewerContributionRateEndEdit)
        NewParameterDialog.setTabOrder(self.sewerContributionRateEndEdit, self.profileComboBox)
        NewParameterDialog.setTabOrder(self.profileComboBox, self.doubleSpinBox)
        NewParameterDialog.setTabOrder(self.doubleSpinBox, self.doubleSpinBox_2)
        NewParameterDialog.setTabOrder(self.doubleSpinBox_2, self.doubleSpinBox_3)
        NewParameterDialog.setTabOrder(self.doubleSpinBox_3, self.doubleSpinBox_4)
        NewParameterDialog.setTabOrder(self.doubleSpinBox_4, self.doubleSpinBox_5)
        NewParameterDialog.setTabOrder(self.doubleSpinBox_5, self.doubleSpinBox_6)
        NewParameterDialog.setTabOrder(self.doubleSpinBox_6, self.doubleSpinBox_7)
        NewParameterDialog.setTabOrder(self.doubleSpinBox_7, self.doubleSpinBox_8)
        NewParameterDialog.setTabOrder(self.doubleSpinBox_8, self.doubleSpinBox_9)
        NewParameterDialog.setTabOrder(self.doubleSpinBox_9, self.minDiameterLineEdit)

    def retranslateUi(self, NewParameterDialog):
        _translate = QtCore.QCoreApplication.translate
        NewParameterDialog.setWindowTitle(_translate("NewParameterDialog", "SANIBIDapp"))
        self.qeReferenceMaxLabel.setText(_translate("NewParameterDialog", "Caudal de referencia del proyecto "))
        self.startLabel.setText(_translate("NewParameterDialog", "Inicial"))
        self.qeMaxLabel.setText(_translate("NewParameterDialog", "QE Max"))
        self.unitLabel_8.setText(_translate("NewParameterDialog", "un"))
        self.populationLabel_3.setText(_translate("NewParameterDialog", "hab/dom"))
        self.distributedContributionsLabel_2.setText(_translate("NewParameterDialog", "Contribuciones distribuidas"))
        self.image_2.setText(_translate("NewParameterDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/prefijoNuevo/contributions.png\" /><img src=\":/distributedContributions/distributedContributions.png\" /><img src=\":/prefijoNuevo/contributions.png\" /></p></body></html>"))
        self.radioButton_2.setText(_translate("NewParameterDialog", "Contribuciones lineales"))
        self.radioButton.setText(_translate("NewParameterDialog", "Contribuciones Puntuales"))
        self.concentratedContributionsPerBlockLabel.setText(_translate("NewParameterDialog", "Contribuciones concentradas por manzana"))
        self.image.setText(_translate("NewParameterDialog", "<html><head/><body><p><img src=\":/prefijoNuevo/contributions.png\"/><img src=\":/concentratedContributions/concentratedContributions.png\"/><img src=\":/prefijoNuevo/contributions.png\"/></p></body></html>"))
        self.distributedContributionsLabel.setText(_translate("NewParameterDialog", "Contribuciones distribuidas"))
        self.PopulationLabel.setText(_translate("NewParameterDialog", "Población"))
        self.occupancyRateLabel.setText(_translate("NewParameterDialog", "Tasa de Ocupación"))
        self.unitLabel_2.setText(_translate("NewParameterDialog", "un"))
        self.litersDayLabel.setText(_translate("NewParameterDialog", "l/dia"))
        self.qeMedLabel.setText(_translate("NewParameterDialog", "QE Max"))
        self.connectionsLabel.setText(_translate("NewParameterDialog", "Cant. conexiones"))
        self.pointFlowsLabel.setText(_translate("NewParameterDialog", "Cantidad (qe)"))
        self.populationLabel.setText(_translate("NewParameterDialog", "hab"))
        self.sewerContributionRateLabel.setText(_translate("NewParameterDialog", "Tasa de contribución lineal de AR"))
        self.specificContributionsLabel.setText(_translate("NewParameterDialog", "Contribuciones Puntuales - Qe"))
        self.litersSecondLabel.setText(_translate("NewParameterDialog", "l/s"))
        self.endLabel.setText(_translate("NewParameterDialog", "Final"))
        self.populationConnectionsLabel.setText(_translate("NewParameterDialog", "Población y Conexiones"))
        self.residencesLabel.setText(_translate("NewParameterDialog", "Cant. viviendas"))
        self.unitLabel.setText(_translate("NewParameterDialog", "un"))
        self.litersKilometersLabel.setText(_translate("NewParameterDialog", "l/s.km"))
        self.ParametersWidget.setTabText(self.ParametersWidget.indexOf(self.parametersLabel), _translate("NewParameterDialog", "Parámetros"))
        self.profileLabel.setText(_translate("NewParameterDialog", "Seleccione Perfil"))
        self.waterConsumptionPcLabel.setText(_translate("NewParameterDialog", "Dotación per capita de Agua"))
        self.k1DailyLabel.setText(_translate("NewParameterDialog", "K1 (coef. día max consumo)"))
        self.k2HourlyLabel.setText(_translate("NewParameterDialog", "K2 (coef. hora max consumo)"))
        self.coefficientReturnCLabel.setText(_translate("NewParameterDialog", "Coef. Retorno C"))
        self.intakeRateLabel.setText(_translate("NewParameterDialog", "Tasa de Infiltracion"))
        self.avgTractiveForceLabel.setText(_translate("NewParameterDialog", "Fuerza tractiva media - min"))
        self.flowMinQminLabel.setText(_translate("NewParameterDialog", "Caudal min. Qmin"))
        self.waterSurfaceMaxLabel.setText(_translate("NewParameterDialog", "Lámina máx. especial (DN < 150mm)"))
        self.maxWaterLevelLabel.setText(_translate("NewParameterDialog", "Lámina máx. regular (DN > 150mm)"))
        self.parametersHydraulicCalculationLabel.setText(_translate("NewParameterDialog", "Parámetros - Cálculo Hidráulico"))
        self.diametersLabel.setText(_translate("NewParameterDialog", "Diámetros"))
        self.minDiameterLabel.setText(_translate("NewParameterDialog", "DN Mínimo"))
        self.newProfileGroupBox.setTitle(_translate("NewParameterDialog", "Nuevo Perfil"))
        self.profileNameLabel.setText(_translate("NewParameterDialog", "Nombre del Perfil"))
        self.pushButton.setText(_translate("NewParameterDialog", "Guardar Perfil"))
        self.ParametersWidget.setTabText(self.ParametersWidget.indexOf(self.projectCriteriasLabel), _translate("NewParameterDialog", "Criterios del Proyecto"))
        item = self.pipesWidget.verticalHeaderItem(0)
        item.setText(_translate("NewParameterDialog", "1"))
        item = self.pipesWidget.verticalHeaderItem(1)
        item.setText(_translate("NewParameterDialog", "2"))
        item = self.pipesWidget.verticalHeaderItem(2)
        item.setText(_translate("NewParameterDialog", "3"))
        item = self.pipesWidget.verticalHeaderItem(3)
        item.setText(_translate("NewParameterDialog", "4"))
        item = self.pipesWidget.verticalHeaderItem(4)
        item.setText(_translate("NewParameterDialog", "5"))
        item = self.pipesWidget.verticalHeaderItem(5)
        item.setText(_translate("NewParameterDialog", "6"))
        item = self.pipesWidget.verticalHeaderItem(6)
        item.setText(_translate("NewParameterDialog", "7"))
        item = self.pipesWidget.verticalHeaderItem(7)
        item.setText(_translate("NewParameterDialog", "8"))
        item = self.pipesWidget.verticalHeaderItem(8)
        item.setText(_translate("NewParameterDialog", "9"))
        item = self.pipesWidget.verticalHeaderItem(9)
        item.setText(_translate("NewParameterDialog", "10"))
        item = self.pipesWidget.verticalHeaderItem(10)
        item.setText(_translate("NewParameterDialog", "12"))
        item = self.pipesWidget.horizontalHeaderItem(0)
        item.setText(_translate("NewParameterDialog", "DN(mm)"))
        item = self.pipesWidget.horizontalHeaderItem(1)
        item.setText(_translate("NewParameterDialog", "Material"))
        item = self.pipesWidget.horizontalHeaderItem(2)
        item.setText(_translate("NewParameterDialog", "C. Manning n sugerido"))
        item = self.pipesWidget.horizontalHeaderItem(3)
        item.setText(_translate("NewParameterDialog", "C. Manning n adoptado"))
        __sortingEnabled = self.pipesWidget.isSortingEnabled()
        self.pipesWidget.setSortingEnabled(False)
        self.pipesWidget.setSortingEnabled(__sortingEnabled)
        self.groupBox_4.setTitle(_translate("NewParameterDialog", "Funciones"))
        self.pushButton_2.setText(_translate("NewParameterDialog", "Agregar"))
        self.pushButton_3.setText(_translate("NewParameterDialog", "Eliminar"))
        self.ParametersWidget.setTabText(self.ParametersWidget.indexOf(self.pipesLabel), _translate("NewParameterDialog", "Tubos"))
        item = self.inspectionDevicesWidget.verticalHeaderItem(0)
        item.setText(_translate("NewParameterDialog", "1"))
        item = self.inspectionDevicesWidget.verticalHeaderItem(1)
        item.setText(_translate("NewParameterDialog", "2"))
        item = self.inspectionDevicesWidget.verticalHeaderItem(2)
        item.setText(_translate("NewParameterDialog", "3"))
        item = self.inspectionDevicesWidget.verticalHeaderItem(3)
        item.setText(_translate("NewParameterDialog", "4"))
        item = self.inspectionDevicesWidget.verticalHeaderItem(4)
        item.setText(_translate("NewParameterDialog", "5"))
        item = self.inspectionDevicesWidget.verticalHeaderItem(5)
        item.setText(_translate("NewParameterDialog", "6"))
        item = self.inspectionDevicesWidget.horizontalHeaderItem(0)
        item.setText(_translate("NewParameterDialog", "Tipo"))
        item = self.inspectionDevicesWidget.horizontalHeaderItem(1)
        item.setText(_translate("NewParameterDialog", "Prof. máxima (m)"))
        item = self.inspectionDevicesWidget.horizontalHeaderItem(2)
        item.setText(_translate("NewParameterDialog", "DN Máximo (mm)"))
        self.groupBox_5.setTitle(_translate("NewParameterDialog", "Funciones"))
        self.pushButton_4.setText(_translate("NewParameterDialog", "Agregar"))
        self.pushButton_5.setText(_translate("NewParameterDialog", "Eliminar"))
        self.ParametersWidget.setTabText(self.ParametersWidget.indexOf(self.inspectionDevicesLabel), _translate("NewParameterDialog", "Dispositivos de Inspección"))
from . import contributions_rc
