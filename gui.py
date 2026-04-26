from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(360, 320)
        Form.setMaximumSize(QtCore.QSize(360, 320))

        self.labelTitle = QtWidgets.QLabel(parent=Form)
        self.labelTitle.setGeometry(QtCore.QRect(80, 20, 201, 31))
        self.labelTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")

        self.labelId = QtWidgets.QLabel(parent=Form)
        self.labelId.setGeometry(QtCore.QRect(70, 70, 21, 31))
        self.labelId.setObjectName("labelId")

        self.lineEditId = QtWidgets.QLineEdit(parent=Form)
        self.lineEditId.setGeometry(QtCore.QRect(110, 70, 141, 31))
        self.lineEditId.setObjectName("lineEditId")

        self.labelCandidates = QtWidgets.QLabel(parent=Form)
        self.labelCandidates.setGeometry(QtCore.QRect(110, 120, 141, 31))
        self.labelCandidates.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelCandidates.setObjectName("labelCandidates")

        self.radioJane = QtWidgets.QRadioButton(parent=Form)
        self.radioJane.setGeometry(QtCore.QRect(135, 160, 95, 20))
        self.radioJane.setObjectName("radioTopuria")

        self.radioJohn = QtWidgets.QRadioButton(parent=Form)
        self.radioJohn.setGeometry(QtCore.QRect(135, 190, 95, 20))
        self.radioJohn.setObjectName("radioGaethje")

        self.pushButtonSubmit = QtWidgets.QPushButton(parent=Form)
        self.pushButtonSubmit.setGeometry(QtCore.QRect(80, 230, 201, 41))
        self.pushButtonSubmit.setObjectName("pushButtonSubmit")

        self.labelMessage = QtWidgets.QLabel(parent=Form)
        self.labelMessage.setGeometry(QtCore.QRect(70, 280, 221, 31))
        self.labelMessage.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelMessage.setObjectName("labelMessage")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Voting Application"))
        self.labelTitle.setText(_translate("Form", "VOTING APPLICATION"))
        self.labelId.setText(_translate("Form", "ID"))
        self.labelCandidates.setText(_translate("Form", "CANDIDATES"))
        self.radioJane.setText(_translate("Form", "Topuria"))
        self.radioJohn.setText(_translate("Form", "Gaethje"))
        self.pushButtonSubmit.setText(_translate("Form", "SUBMIT VOTE"))
        self.labelMessage.setText(_translate("Form", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())