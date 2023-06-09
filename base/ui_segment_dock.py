# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AutomaticGeometricAttributesDialog
                                 A QGIS plugin
 This plugin fill automaticaly the geometric attributes of a line
                             -------------------
        begin                : 2016-07-20
        git sha              : $Format:%H$
        copyright            : (C) 2016 by Infinisoft
        email                : frogerio@infinisoft.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from __future__ import print_function
from __future__ import absolute_import

from builtins import next
import os

from qgis.PyQt import uic, QtWidgets
from qgis.core import *
from .helper_functions import HelperFunctions

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__),'resources', 'ui_segment_dock.ui'))


class UiSegmentDock(QtWidgets.QDockWidget, FORM_CLASS):
    

    
    def __init__(self, parent=None):
        """Constructor."""
        super().__init__(parent)
        
        self.setupUi(self)


        
        self.btnBefore.clicked.connect(self.navigateBefore)
        self.btnAfter.clicked.connect(self.navigateAfter)

        self.selId = None

    def SetIface(self,iface):
        
        self.h = HelperFunctions(iface)

    def SetSelectedId(self,_id):        
        self.selId = _id

    def GetSelectedId(self):
        return self.selId


    def navigateBefore(self):
        self.navigate(-1)

    def navigateAfter(self):
        self.navigate(1)

    def navigate(self,to):
        if self.selId != None:
            # fix_print_with_import
            print('ue')
            h = self.h

            # iterator = h.GetLayer().getFeatures(QgsFeatureRequest().setFilterFid(self.selId))
            feature = h.GetLayer().getFeature(self.selId)

            beg_line_coord_e = h.readValueFromProject("BEG_LINE_COORD_E")
            beg_line_coord_n = h.readValueFromProject("BEG_LINE_COORD_N")
            fin_line_coord_e = h.readValueFromProject("FIN_LINE_COORD_E")
            fin_line_coord_n = h.readValueFromProject("FIN_LINE_COORD_N")
            seg_name = h.readValueFromProject("SEG_NAME")
            seg_name_c = h.readValueFromProject("SEG_NAME_C")

            lstMinFeatures = []
            for ft in h.GetLayer().getFeatures():
                minFeatureObj = {}
                minFeatureObj["BEG_LINE_COORD_E"] = ft[beg_line_coord_e]
                minFeatureObj["BEG_LINE_COORD_N"] = ft[beg_line_coord_n]
                minFeatureObj["FIN_LINE_COORD_E"] = ft[fin_line_coord_e]
                minFeatureObj["FIN_LINE_COORD_N"] = ft[fin_line_coord_n]
                minFeatureObj["SEG_NAME"] = ft[seg_name]
                minFeatureObj["SEG_NAME_C"] = ft[seg_name_c]
                minFeatureObj["ID"] = ft.id()
                lstMinFeatures.append(minFeatureObj)
        
            fnd = h.Get_Feature_On_Index(lstMinFeatures,feature,to,True,[],True)
            if fnd:
                # fix_print_with_import
                print('aqui')
                self.saveFunction()
                h.GetLayer().selectByIds([fnd["ID"]])
    
    

    
