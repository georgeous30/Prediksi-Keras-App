# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formAnalisis.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_formAnalisisDialog(object):
    def setupUi(self, formAnalisisDialog):
        formAnalisisDialog.setObjectName("formAnalisisDialog")
        formAnalisisDialog.resize(600, 600)
        formAnalisisDialog.setMinimumSize(QtCore.QSize(600, 600))
        self.verticalLayout = QtWidgets.QVBoxLayout(formAnalisisDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_4 = QtWidgets.QFrame(formAnalisisDialog)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(78, 78))
        self.label_5.setMaximumSize(QtCore.QSize(78, 78))
        self.label_5.setBaseSize(QtCore.QSize(0, 0))
        self.label_5.setStyleSheet("image: url(:/Logo/Artboard 22-75.png);")
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.horizontalLayout_7.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(formAnalisisDialog)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.horizontalLayout_7.addWidget(self.frame_5)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.frame_12 = QtWidgets.QFrame(formAnalisisDialog)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_12)
        self.gridLayout_3.setContentsMargins(0, -1, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 2, 0, 1, 1)
        self.buttonAnalyze = QtWidgets.QPushButton(self.frame_12)
        self.buttonAnalyze.setObjectName("buttonAnalyze")
        self.gridLayout_3.addWidget(self.buttonAnalyze, 2, 1, 1, 1)
        self.comboMaterial = QtWidgets.QComboBox(self.frame_12)
        self.comboMaterial.setObjectName("comboMaterial")
        self.comboMaterial.addItem("")
        self.comboMaterial.addItem("")
        self.comboMaterial.addItem("")
        self.gridLayout_3.addWidget(self.comboMaterial, 1, 0, 1, 2)
        self.label_14 = QtWidgets.QLabel(self.frame_12)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 0, 0, 1, 2)
        self.verticalLayout.addWidget(self.frame_12)
        self.graphicsView = QtWidgets.QGraphicsView(formAnalisisDialog)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.frame_11 = QtWidgets.QFrame(formAnalisisDialog)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_11)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.lineWeek3 = QtWidgets.QLineEdit(self.frame_11)
        self.lineWeek3.setObjectName("lineWeek3")
        self.gridLayout_8.addWidget(self.lineWeek3, 6, 3, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame_11)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_8.addWidget(self.label_12, 4, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.frame_11)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_8.addWidget(self.label_11, 4, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.frame_11)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_8.addWidget(self.label_13, 4, 3, 1, 1)
        self.lineWeek2 = QtWidgets.QLineEdit(self.frame_11)
        self.lineWeek2.setObjectName("lineWeek2")
        self.gridLayout_8.addWidget(self.lineWeek2, 6, 1, 1, 1)
        self.lineWeek1 = QtWidgets.QLineEdit(self.frame_11)
        self.lineWeek1.setObjectName("lineWeek1")
        self.gridLayout_8.addWidget(self.lineWeek1, 6, 0, 1, 1)
        self.lineWeek4 = QtWidgets.QLineEdit(self.frame_11)
        self.lineWeek4.setObjectName("lineWeek4")
        self.gridLayout_8.addWidget(self.lineWeek4, 6, 4, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame_11)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_8.addWidget(self.label_10, 4, 4, 1, 1)
        self.lineMaterial = QtWidgets.QLineEdit(self.frame_11)
        self.lineMaterial.setObjectName("lineMaterial")
        self.gridLayout_8.addWidget(self.lineMaterial, 0, 1, 1, 4)
        self.label_7 = QtWidgets.QLabel(self.frame_11)
        self.label_7.setObjectName("label_7")
        self.gridLayout_8.addWidget(self.label_7, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_11)
        self.frame_2 = QtWidgets.QFrame(formAnalisisDialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineTest = QtWidgets.QLineEdit(self.frame_2)
        self.lineTest.setObjectName("lineTest")
        self.gridLayout_2.addWidget(self.lineTest, 1, 1, 1, 1)
        self.lineTrain = QtWidgets.QLineEdit(self.frame_2)
        self.lineTrain.setObjectName("lineTrain")
        self.gridLayout_2.addWidget(self.lineTrain, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_6 = QtWidgets.QFrame(formAnalisisDialog)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_8 = QtWidgets.QFrame(self.frame_6)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.buttonHome = QtWidgets.QPushButton(self.frame_8)
        self.buttonHome.setObjectName("buttonHome")
        self.gridLayout_5.addWidget(self.buttonHome, 0, 0, 1, 1)
        self.horizontalLayout_5.addWidget(self.frame_8)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.frame_10 = QtWidgets.QFrame(self.frame_6)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.buttonPrint = QtWidgets.QPushButton(self.frame_10)
        self.buttonPrint.setObjectName("buttonPrint")
        self.gridLayout_7.addWidget(self.buttonPrint, 0, 0, 1, 1)
        self.horizontalLayout_5.addWidget(self.frame_10)
        self.verticalLayout.addWidget(self.frame_6)

        self.retranslateUi(formAnalisisDialog)
        QtCore.QMetaObject.connectSlotsByName(formAnalisisDialog)

    def retranslateUi(self, formAnalisisDialog):
        _translate = QtCore.QCoreApplication.translate
        formAnalisisDialog.setWindowTitle(_translate("formAnalisisDialog", "Analisis"))
        self.label_6.setText(_translate("formAnalisisDialog", "My App"))
        self.buttonAnalyze.setText(_translate("formAnalisisDialog", "Analyze!"))
        self.comboMaterial.setItemText(0, _translate("formAnalisisDialog", "HVS 80"))
        self.comboMaterial.setItemText(1, _translate("formAnalisisDialog", "Art Carton"))
        self.comboMaterial.setItemText(2, _translate("formAnalisisDialog", "Art Paper"))
        self.label_14.setText(_translate("formAnalisisDialog", "Material"))
        self.label_12.setText(_translate("formAnalisisDialog", "Next 2 Week"))
        self.label_11.setText(_translate("formAnalisisDialog", "Next Week"))
        self.label_13.setText(_translate("formAnalisisDialog", "Next 3 Week"))
        self.label_10.setText(_translate("formAnalisisDialog", "Next 4 Week"))
        self.label_7.setText(_translate("formAnalisisDialog", "Material"))
        self.label_8.setText(_translate("formAnalisisDialog", "Training"))
        self.label_9.setText(_translate("formAnalisisDialog", "Testing "))
        self.buttonHome.setText(_translate("formAnalisisDialog", "Home"))
        self.buttonPrint.setText(_translate("formAnalisisDialog", "Print"))
import source1_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    formAnalisisDialog = QtWidgets.QDialog()
    ui = Ui_formAnalisisDialog()
    ui.setupUi(formAnalisisDialog)
    formAnalisisDialog.show()
    sys.exit(app.exec_())
