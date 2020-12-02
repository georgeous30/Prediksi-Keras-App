from PyQt5 import QtWidgets, QtCore
from formAnalisis import Ui_formAnalisisDialog
from formMaterial import Ui_formMaterialDialog
from formEditMaterial import Ui_formEditMaterialDialog
from formAbout import Ui_formAboutDialog
from formHelp import Ui_formHelpDialog


class runnerAnalisisDialog(QtWidgets.QDialog, Ui_formAnalisisDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.initButtonFunction()



    def initButtonFunction(self):
        self.buttonAnalyze.clicked.connect(self.AnalyzeClicked)
        self.buttonHome.clicked.connect(self.HomeClicked)
    
    def HomeClicked(self):
        self.close()

    def AnalyzeClicked(self):
        print("clicked Analyse")



class runnerMaterialDialog(QtWidgets.QDialog, Ui_formMaterialDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.initButtonFunction()


    def initButtonFunction(self):  
        self.buttonEditMaterial.clicked.connect(self.EditMaterialClicked)
        self.buttonHome.clicked.connect(self.HomeClicked)
   
    def HomeClicked(self):
        self.close()
    
    def EditMaterialClicked(self):
        print('EditMaterial clicked')
        rsp = LaunchEditMaterial()
        print(rsp)



class runnerEditMaterialDialog(QtWidgets.QDialog, Ui_formEditMaterialDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.initButtonFunction()


    def initButtonFunction(self):        
        self.buttonCancel.clicked.connect(self.CancelClicked)
    def CancelClicked(self):
        self.close()


class runnerHelpDialog(QtWidgets.QDialog, Ui_formAboutDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.initButtonFunction()


    def initButtonFunction(self):        
        self.buttonHome.clicked.connect(self.HomeClicked)
    def HomeClicked(self):
        self.close()



class runnerAboutDialog(QtWidgets.QDialog, Ui_formHelpDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.initButtonFunction()


    def initButtonFunction(self):        
        self.buttonHome.clicked.connect(self.HomeClicked)
    def HomeClicked(self):
        self.close()
        
        
                      


def LaunchAnalisis():
    return run(runnerAnalisisDialog())
def LaunchMaterial():
    return run(runnerMaterialDialog())
def LaunchEditMaterial():
    return run(runnerEditMaterialDialog())
def LaunchAbout():
    return run(runnerAboutDialog()) 
def LaunchHelp():
    return run(runnerHelpDialog())


def run(DialogQ):
    dialog = DialogQ
    return dialog.exec_()




if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    formAnalisisDialog = QtWidgets.QDialog()
    ui = Ui_formAnalisisDialog()
    ui.setupUi(formAnalisisDialog)
    formAnalisisDialog.show()
    sys.exit(app.exec_())
