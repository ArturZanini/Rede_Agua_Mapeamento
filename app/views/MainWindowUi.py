# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1111, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1101, 551))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(13)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1111, 22))
        self.menubar.setObjectName("menubar")
        self.menuParametros = QtWidgets.QMenu(self.menubar)
        self.menuParametros.setObjectName("menuParametros")
        self.menuFunciones = QtWidgets.QMenu(self.menubar)
        self.menuFunciones.setObjectName("menuFunciones")
        self.menuExportaci_n = QtWidgets.QMenu(self.menubar)
        self.menuExportaci_n.setObjectName("menuExportaci_n")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionProject = QtWidgets.QAction(MainWindow)
        self.actionProject.setObjectName("actionProject")
        self.actionParameters = QtWidgets.QAction(MainWindow)
        self.actionParameters.setObjectName("actionParameters")
        self.actionPipes = QtWidgets.QAction(MainWindow)
        self.actionPipes.setObjectName("actionPipes")
        self.actionInspectionDevices = QtWidgets.QAction(MainWindow)
        self.actionInspectionDevices.setObjectName("actionInspectionDevices")
        self.actionMin_Excav = QtWidgets.QAction(MainWindow)
        self.actionMin_Excav.setObjectName("actionMin_Excav")
        self.actionMin_Desnivel = QtWidgets.QAction(MainWindow)
        self.actionMin_Desnivel.setObjectName("actionMin_Desnivel")
        self.actionAjuste_NA = QtWidgets.QAction(MainWindow)
        self.actionAjuste_NA.setObjectName("actionAjuste_NA")
        self.actionCalcular_DN_Creciente = QtWidgets.QAction(MainWindow)
        self.actionCalcular_DN_Creciente.setObjectName("actionCalcular_DN_Creciente")
        self.actionCalculara_DN = QtWidgets.QAction(MainWindow)
        self.actionCalculara_DN.setObjectName("actionCalculara_DN")
        self.actionCrear_Capa_QGIS = QtWidgets.QAction(MainWindow)
        self.actionCrear_Capa_QGIS.setObjectName("actionCrear_Capa_QGIS")
        self.actionGenerar_Hoja_Impresi_n = QtWidgets.QAction(MainWindow)
        self.actionGenerar_Hoja_Impresi_n.setObjectName("actionGenerar_Hoja_Impresi_n")
        self.menuParametros.addAction(self.actionProject)
        self.menuParametros.addAction(self.actionParameters)
        self.menuFunciones.addAction(self.actionMin_Excav)
        self.menuFunciones.addAction(self.actionMin_Desnivel)
        self.menuFunciones.addAction(self.actionAjuste_NA)
        self.menuFunciones.addAction(self.actionCalcular_DN_Creciente)
        self.menuFunciones.addAction(self.actionCalculara_DN)
        self.menuExportaci_n.addAction(self.actionCrear_Capa_QGIS)
        self.menuExportaci_n.addAction(self.actionGenerar_Hoja_Impresi_n)
        self.menubar.addAction(self.menuParametros.menuAction())
        self.menubar.addAction(self.menuFunciones.menuAction())
        self.menubar.addAction(self.menuExportaci_n.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SANIBIDapp"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "col1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "col2"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "col3"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "col4"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "col5"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "col6"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "col7"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "col8"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "col9"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "col10"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "col11"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "col12"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "col13"))
        self.menuParametros.setTitle(_translate("MainWindow", "Configuración"))
        self.menuFunciones.setTitle(_translate("MainWindow", "Funciones"))
        self.menuExportaci_n.setTitle(_translate("MainWindow", "Exportación"))
        self.actionProject.setText(_translate("MainWindow", "Proyecto"))
        self.actionParameters.setText(_translate("MainWindow", "Parámetros"))
        self.actionPipes.setText(_translate("MainWindow", "Tubos"))
        self.actionInspectionDevices.setText(_translate("MainWindow", "Dispositivos de Inspección"))
        self.actionMin_Excav.setText(_translate("MainWindow", "Min. Excav."))
        self.actionMin_Desnivel.setText(_translate("MainWindow", "Min. Desnivel"))
        self.actionAjuste_NA.setText(_translate("MainWindow", "Ajuste NA"))
        self.actionCalcular_DN_Creciente.setText(_translate("MainWindow", "Calcular DN Creciente"))
        self.actionCalculara_DN.setText(_translate("MainWindow", "Calculara DN"))
        self.actionCrear_Capa_QGIS.setText(_translate("MainWindow", "Crear Capa QGIS"))
        self.actionGenerar_Hoja_Impresi_n.setText(_translate("MainWindow", "Generar Hoja Impresión"))
