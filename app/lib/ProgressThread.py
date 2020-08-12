from PyQt5.QtCore import QThread
from qgis.core import Qgis
from qgis.utils import QgsMessageLog

class ProgressThread(QThread):

    def __init__(self, mainView, controller, run):
        super().__init__(mainView)
                
        self.bar = mainView.progressBar
        self.msg = mainView.progressMsg        
        self.iface = mainView.iface
        self.refreshTables = mainView.refreshTables

        #show progress bar
        self.bar.show()
        self.msg.show() 
        
        #attach worker
        worker = controller
        self.started.connect(run)        
        worker.moveToThread(self)        
        worker.finished.connect(self.threadFinished)        
        worker.error.connect(self.threadError)
        worker.progress.connect(self.bar.setValue)
        worker.info.connect(self.msg.setText)
        self.worker = worker
        self.start()


    def threadFinished(self, success):        
        # clean up the worker and thread
        self.worker.deleteLater()
        self.quit()
        self.wait()
        self.deleteLater()        
        self.bar.hide()
        self.msg.hide()       
        if success:
            self.refreshTables()            
            self.iface.messageBar().pushMessage('the process ended successfully!')
        else:
            # notify the user that something went wrong
            self.iface.messageBar().pushMessage('Something went wrong! See the message log for more information.', level=Qgis.Critical, duration=3)

    def threadError(self, e, trace):        
        QgsMessageLog.logMessage('ProgressBar thread raised an exception:\n {}'.format(trace), level=Qgis.Critical)         