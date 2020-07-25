from PyQt5.QtWidgets import (QAbstractItemView, QDataWidgetMapper, QCompleter, QComboBox,
    QHeaderView, QDialog, QMessageBox, QTableWidget)
from PyQt5.QtGui import QKeySequence
from PyQt5.QtSql import QSqlRelation, QSqlRelationalTableModel, QSqlTableModel, QSqlRelationalDelegate
from PyQt5.QtCore import Qt, pyqtSlot, pyqtSignal, QModelIndex, QDateTime

from ..models.Parameter import Parameter
from ..models.Project import Project
from ..models.Criteria import Criteria
from ..models.Pipe import Pipe
from ..models.InspectionDevice import InspectionDevice
from .ui.ParameterDialogUi import Ui_NewParameterDialog

class ParameterView(QDialog, Ui_NewParameterDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.parameterId = None
        self.profileIsEditable = False
        
        #ParameterModel               
        self.parameterModel = QSqlRelationalTableModel(self.profileComboBox)        
        self.parameterModel.setTable("parameters")
               
        criteria_idx = self.parameterModel.fieldIndex("project_criteria_id")                
        self.parameterModel.setRelation(criteria_idx, QSqlRelation("project_criterias", "id", "name"))         

        if not self.parameterModel.select():
            print(self.parameterModel.lastError().text())

        #Tab1
        self.profileComboBox.setModel(self.parameterModel.relationModel(criteria_idx))
        self.profileComboBox.setModelColumn(self.parameterModel.relationModel(criteria_idx).fieldIndex("name"))

        self.mapper = QDataWidgetMapper(self)
        self.mapper.setModel(self.parameterModel)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.AutoSubmit)
        self.mapper.addMapping(self.beginningPopulationEdit, self.parameterModel.fieldIndex('beginning_population'))
        self.mapper.addMapping(self.finalPopulationEdit, self.parameterModel.fieldIndex('final_population'))
        self.mapper.addMapping(self.occupancyRateStartEdit, self.parameterModel.fieldIndex('occupancy_rate_start'))
        self.mapper.addMapping(self.occupancyRateEndEdit, self.parameterModel.fieldIndex('occupancy_rate_end'))
        self.mapper.addMapping(self.residencesStartEdit, self.parameterModel.fieldIndex('residences_start'))
        self.mapper.addMapping(self.residencesEndEdit, self.parameterModel.fieldIndex('residences_end'))        
        self.mapper.addMapping(self.connectionsStartEdit, self.parameterModel.fieldIndex('connections_start'))
        self.mapper.addMapping(self.connectionsEndEdit, self.parameterModel.fieldIndex('connections_end'))
        self.mapper.addMapping(self.pointFlowsStartEdit, self.parameterModel.fieldIndex('point_flows_start'))
        self.mapper.addMapping(self.pointFlowsEndEdit, self.parameterModel.fieldIndex('point_flows_end'))
        self.mapper.addMapping(self.qeReferenceMedEdit, self.parameterModel.fieldIndex('qe_reference_med'))
        self.mapper.addMapping(self.qeReferenceMaxEdit, self.parameterModel.fieldIndex('qe_reference_max'))               
        self.mapper.addMapping(self.sewerContributionRateStartEdit, self.parameterModel.fieldIndex('sewer_contribution_rate_start'))
        self.mapper.addMapping(self.sewerContributionRateEndEdit, self.parameterModel.fieldIndex('sewer_contribution_rate_end'))        
        self.mapper.addMapping(self.profileComboBox, criteria_idx)
        self.mapper.setItemDelegate(QSqlRelationalDelegate(self.profileComboBox))                 
                
        #Tab2
        #Criterias
        self.currentCriteriaIndex = None
        self.currentCriteriaId = None
        self.mapper_project_criterias = QDataWidgetMapper(self)
        self.criteriaModel = Criteria()
        self.mapper_project_criterias.setModel(self.criteriaModel)
        self.maxWaterLevelSpinBox.setReadOnly(True)
        
        self.mapper_project_criterias.addMapping(self.profileName, self.criteriaModel.fieldIndex('name'))
        self.mapper_project_criterias.addMapping(self.waterConsumptionPcSpinBox, self.criteriaModel.fieldIndex('water_consumption_pc'))
        self.mapper_project_criterias.addMapping(self.k1DailySpinBox, self.criteriaModel.fieldIndex('k1_daily'))
        self.mapper_project_criterias.addMapping(self.k2HourlySpinBox, self.criteriaModel.fieldIndex('k2_hourly'))
        self.mapper_project_criterias.addMapping(self.coefficientReturnCSpinBox, self.criteriaModel.fieldIndex('coefficient_return_c'))
        self.mapper_project_criterias.addMapping(self.intakeRateSpinBox, self.criteriaModel.fieldIndex('intake_rate'))
        self.mapper_project_criterias.addMapping(self.avgTractiveForceSpinBox, self.criteriaModel.fieldIndex('avg_tractive_force_min'))
        self.mapper_project_criterias.addMapping(self.flowMinQminSpinBox, self.criteriaModel.fieldIndex('flow_min_qmin'))
        self.mapper_project_criterias.addMapping(self.waterSurfaceMaxSpinBox, self.criteriaModel.fieldIndex('water_surface_max'))
        self.mapper_project_criterias.addMapping(self.maxWaterLevelSpinBox, self.criteriaModel.fieldIndex('max_water_level'))
        self.mapper_project_criterias.addMapping(self.minDiameterLineEdit, self.criteriaModel.fieldIndex('min_diameter'))
        self.mapper_project_criterias.addMapping(self.diameterUp150SpinBox, self.criteriaModel.fieldIndex('diameter_up_150'))
        self.mapper_project_criterias.addMapping(self.diameterUp200SpinBox, self.criteriaModel.fieldIndex('diameter_up_200'))
        self.mapper_project_criterias.addMapping(self.diameterUp250SpinBox, self.criteriaModel.fieldIndex('from_diameter_250'))
        self.mapper_project_criterias.addMapping(self.coverMinStreetSpinBox, self.criteriaModel.fieldIndex('cover_min_street'))
        self.mapper_project_criterias.addMapping(self.coverMinSidewalksGsSpinBox, self.criteriaModel.fieldIndex('cover_min_sidewalks_gs'))
        self.mapper_project_criterias.addMapping(self.typePreferredHeadColSpinBox, self.criteriaModel.fieldIndex('type_preferred_head_col'))
        self.mapper_project_criterias.addMapping(self.maxDropSpinBox, self.criteriaModel.fieldIndex('max_drop'))
        self.mapper_project_criterias.addMapping(self.bottomIbMhSpinBox, self.criteriaModel.fieldIndex('bottom_ib_mh'))
        
        #Pipes       
        self.pipeModel = Pipe()        
        self.pipesTable.setModel(self.pipeModel)
        self.pipesTable.setItemDelegate(QSqlRelationalDelegate(self.pipesTable))                
        #hide and strech columns
        self.pipesTable.setColumnHidden(self.pipeModel.fieldIndex("id"), True)
        self.pipesTable.setColumnHidden(self.pipeModel.fieldIndex("created_at"), True)
        self.pipesTable.setColumnHidden(self.pipeModel.fieldIndex("updated_at"), True)                       
        self.pipesTable.horizontalHeader().setSectionResizeMode(True)

        #Inspection Devices
        self.deviceModel = InspectionDevice()
        self.devicesTable.setModel(self.deviceModel)
        self.devicesTable.setItemDelegate(QSqlRelationalDelegate(self.devicesTable))
        #hide and strech columns
        self.devicesTable.setColumnHidden(self.deviceModel.fieldIndex("id"), True)
        self.devicesTable.setColumnHidden(self.deviceModel.fieldIndex("type_en"), True)
        self.devicesTable.setColumnHidden(self.deviceModel.fieldIndex("type_pt"), True)
        self.devicesTable.setColumnHidden(self.deviceModel.fieldIndex("created_at"), True)
        self.devicesTable.setColumnHidden(self.deviceModel.fieldIndex("updated_at"), True) 
        self.devicesTable.horizontalHeader().setSectionResizeMode(True)

        #conections
        self.profileComboBox.currentIndexChanged.connect(self.onProfileChange)

        self.finalPopulationEdit.valueChanged.connect(self.calculateResidencesEnd)
        self.occupancyRateEndEdit.valueChanged.connect(self.calculateResidencesEnd)
        self.beginningPopulationEdit.valueChanged.connect(self.calculateResidencesStart)
        self.occupancyRateStartEdit.valueChanged.connect(self.calculateResidencesStart)

        self.waterConsumptionPcSpinBox.valueChanged.connect(self.calculateQeReferenceMaxEdit)
        self.occupancyRateEndEdit.valueChanged.connect(self.calculateQeReferenceMaxEdit)
        self.coefficientReturnCSpinBox.valueChanged.connect(self.calculateQeReferenceMaxEdit)
        self.k1DailySpinBox.valueChanged.connect(self.calculateQeReferenceMaxEdit)
        self.k2HourlySpinBox.valueChanged.connect(self.calculateQeReferenceMaxEdit)
        self.waterConsumptionPcSpinBox.valueChanged.connect(self.calculateQeReferenceMedEdit)
        self.occupancyRateEndEdit.valueChanged.connect(self.calculateQeReferenceMedEdit)
        self.coefficientReturnCSpinBox.valueChanged.connect(self.calculateQeReferenceMedEdit)

        self.addPipeButton.clicked.connect(self.addPipeRecord)
        self.deletePipeButton.clicked.connect(self.deletePipeRecord)
        self.addDeviceButton.clicked.connect(self.addDeviceRecord)
        self.deleteDeviceButton.clicked.connect(self.deleteDeviceRecord)
        self.buttonBox.accepted.connect(self.saveParameters)
        self.newProfileButton.clicked.connect(self.addProfileRecord)
    
    def isCurrentProfileEditable(self):
        projectId = Project.getActiveId()
        if projectId:
            record = self.criteriaModel.record(self.currentCriteriaIndex)
            return projectId == record.value('parent_project_id')
        return False

    def calculateResidencesEnd(self):
        finalPop = self.finalPopulationEdit.value()
        rateEnd = self.occupancyRateEndEdit.value()
        self.residencesEndEdit.setValue(finalPop/rateEnd) if (rateEnd > 0 and rateEnd < finalPop ) else self.residencesEndEdit.setValue(0)

    def calculateQeReferenceMaxEdit(self):
        waterCons = self.waterConsumptionPcSpinBox.value()
        occRate = self.occupancyRateEndEdit.value()
        coeffRetC = self.coefficientReturnCSpinBox.value()
        k1Dly = self.k1DailySpinBox.value()
        k2Hrly = self.k2HourlySpinBox.value()
        self.qeReferenceMaxEdit.setValue((waterCons*occRate*coeffRetC*k1Dly*k2Hrly)/86400)
    
    def calculateQeReferenceMedEdit(self):
        waterCons = self.waterConsumptionPcSpinBox.value()
        occRate = self.occupancyRateEndEdit.value()
        coeffRetC = self.coefficientReturnCSpinBox.value()
        self.qeReferenceMedEdit.setValue(waterCons*occRate*coeffRetC)

    def calculateResidencesStart(self):
        begPop = self.beginningPopulationEdit.value()
        rateStart = self.occupancyRateStartEdit.value()
        self.residencesStartEdit.setValue(begPop/rateStart) if (rateStart > 0 and rateStart < begPop ) else self.residencesStartEdit.setValue(0)

    def onProfileChange(self, i):        
        self.currentCriteriaIndex = i
        self.currentCriteriaId = self.criteriaModel.data(self.criteriaModel.index(self.currentCriteriaIndex, self.criteriaModel.fieldIndex("id")))
        self.profileIsEditable = self.isCurrentProfileEditable()
        self.loadProfile()      

    def loadProfile(self):        
        if self.currentCriteriaIndex is not None:            
            self.mapper_project_criterias.setCurrentIndex(self.currentCriteriaIndex)            
            self.loadPipes(self.currentCriteriaId)
            self.loadDevices(self.currentCriteriaId)
        else:            
            self.mapper_project_criterias.toFirst()
        
        #self.devicesTable.setEditTriggers(QTableWidget.NoEditTriggers)
        self.profileName.setEnabled(self.profileIsEditable)
        self.pipesTable.setEnabled(self.profileIsEditable)
        self.devicesTable.setEnabled(self.profileIsEditable)
        self.addPipeButton.setEnabled(self.profileIsEditable)
        self.deletePipeButton.setEnabled(self.profileIsEditable)
        self.addDeviceButton.setEnabled(self.profileIsEditable)
        self.deleteDeviceButton.setEnabled(self.profileIsEditable)

    def loadPipes(self, criteria_id):
        if criteria_id:
            self.pipeModel.setFilter("criteria_id = {}".format(criteria_id))            
    
    def loadDevices(self, criteria_id):
        if criteria_id:
            self.deviceModel.setFilter("criteria_id = {}".format(criteria_id)) 

    def showEvent(self, event):        
        self.parameterId = Project.getActiveProjectParameter()
        if self.parameterId:
            self.parameterModel.setFilter("parameters.id = {}".format(self.parameterId))            
            self.mapper.toFirst() #IMPORTANT: onProfileChange is triggered by this            
            if self.profileComboBox.currentIndex() == 0:
                self.onProfileChange(0)
        else:
            self.addParameterRecord()
            self.loadProfile()

    def addProfileRecord(self):
        row = self.criteriaModel.rowCount()
        self.mapper_project_criterias.submit()
        self.criteriaModel.insertRow(row)        
        self.criteriaModel.setData(self.criteriaModel.index(row, self.criteriaModel.fieldIndex("name")), "New Profile")
        self.criteriaModel.setData(self.criteriaModel.index(row, self.criteriaModel.fieldIndex("parent_project_id")), Project.getActiveId())
        self.mapper_project_criterias.submit()
        self.criteriaModel.select()
        self.mapper_project_criterias.setCurrentIndex(row)
        self.profileComboBox.model().select()
        self.profileComboBox.setCurrentIndex(row)

    def addParameterRecord(self):
        row = self.parameterModel.rowCount()
        self.mapper.submit()
        self.parameterModel.insertRow(row)
        self.mapper.setCurrentIndex(row)
        self.profileComboBox.setCurrentIndex(0)

    def addPipeRecord(self):  
        row = self.pipeModel.rowCount()        
        self.pipeModel.insertRow(row) 
        self.pipeModel.setData(self.pipeModel.index(row, self.pipeModel.fieldIndex("criteria_id")), self.currentCriteriaId)

    def addDeviceRecord(self):  
        row = self.deviceModel.rowCount()        
        self.deviceModel.insertRow(row) 
        self.deviceModel.setData(self.deviceModel.index(row, self.deviceModel.fieldIndex("criteria_id")), self.currentCriteriaId)


    def deletePipeRecord(self):
        if (QMessageBox.question(self,
                "Delete",
                "Delete selected rows, are you sure?",
                QMessageBox.Yes|QMessageBox.No) ==QMessageBox.No):
            return
        selection = self.pipesTable.selectionModel().selectedRows()
        for index in selection:
            row = index.row()
            self.pipeModel.removeRow(row)
        self.pipeModel.submitAll()
        self.pipeModel.select()            

    def deleteDeviceRecord(self):
        if (QMessageBox.question(self,
                "Delete",
                "Delete selected rows, are you sure?",
                QMessageBox.Yes|QMessageBox.No) ==QMessageBox.No):
            return
        selection = self.devicesTable.selectionModel().selectedRows()
        for index in selection:
            row = index.row()
            self.deviceModel.removeRow(row)
        self.deviceModel.submitAll()
        self.deviceModel.select()

    def saveParameters(self):
        self.mapper.submit()
        self.mapper_project_criterias.submit()
        self.pipeModel.submitAll()
        self.deviceModel.submitAll()
        if not self.parameterId:
            self.parameterId = self.parameterModel.query().lastInsertId()
            Project.setParameterToActive(self.parameterId)