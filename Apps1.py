from formHome import Ui_formHome

from PyQt5 import QtWidgets, QtCore
import runnerDialog as runner


# class AnalisisWindow(QtWidgets.QDialog, Ui_formAnalisisDialog):
#     def __init__(self, parent=None):
#         super(Ui_formAnalisisDialog,self).__init__(parent)
#         self.setupUi(self)
        


class MainWindow(QtWidgets.QWidget, Ui_formHome):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)
        self.initButtonFunction()


    def initButtonFunction(self):
        self.buttonAnalisis.clicked.connect(self.AnalisisClicked)
        self.buttonMaterial.clicked.connect(self.MaterialClicked)
        self.buttonHelp.clicked.connect(self.HelpClicked)
        self.buttonAbout.clicked.connect(self.AboutClicked)
        self.buttonExit.clicked.connect(self.ExitClicked)




    def AnalisisClicked(self):
        print('Analisis clicked')
        rsp = runner.LaunchAnalisis()
        print(rsp)

    def MaterialClicked(self):
        print('Material clicked')
        rsp = runner.LaunchMaterial()
        print(rsp)

    def HelpClicked(self):
        print('Help clicked')
        rsp = runner.LaunchHelp()
        print(rsp)

    def AboutClicked(self):
        print('Help clicked')
        rsp = runner.LaunchHelp()
        print(rsp)

    def ExitClicked(self):
        print('Exit clicked')
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    widget = MainWindow()
    widget.show()
    app.exec_()

