# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'processing_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(273, 227)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_processArbData = QtWidgets.QGroupBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_processArbData.sizePolicy().hasHeightForWidth())
        self.groupBox_processArbData.setSizePolicy(sizePolicy)
        self.groupBox_processArbData.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.groupBox_processArbData.setObjectName("groupBox_processArbData")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_processArbData)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox_type_of_data = QtWidgets.QComboBox(self.groupBox_processArbData)
        self.comboBox_type_of_data.setObjectName("comboBox_type_of_data")
        self.comboBox_type_of_data.addItem("")
        self.comboBox_type_of_data.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_type_of_data, 10, 0, 1, 1)
        self.checkBox_isInterpolation = QtWidgets.QCheckBox(self.groupBox_processArbData)
        self.checkBox_isInterpolation.setChecked(True)
        self.checkBox_isInterpolation.setObjectName("checkBox_isInterpolation")
        self.gridLayout_2.addWidget(self.checkBox_isInterpolation, 7, 0, 1, 1)
        self.checkBox_is_remove_background_out_of_contact = QtWidgets.QCheckBox(self.groupBox_processArbData)
        self.checkBox_is_remove_background_out_of_contact.setObjectName("checkBox_is_remove_background_out_of_contact")
        self.gridLayout_2.addWidget(self.checkBox_is_remove_background_out_of_contact, 8, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_processArbData)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.checkBox_isAveraging = QtWidgets.QCheckBox(self.groupBox_processArbData)
        self.checkBox_isAveraging.setObjectName("checkBox_isAveraging")
        self.gridLayout_2.addWidget(self.checkBox_isAveraging, 5, 0, 1, 1)
        self.checkBox_isShifting = QtWidgets.QCheckBox(self.groupBox_processArbData)
        self.checkBox_isShifting.setObjectName("checkBox_isShifting")
        self.gridLayout_2.addWidget(self.checkBox_isShifting, 6, 0, 1, 1)
        self.comboBox_axis_to_plot_along = QtWidgets.QComboBox(self.groupBox_processArbData)
        self.comboBox_axis_to_plot_along.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox_axis_to_plot_along.setObjectName("comboBox_axis_to_plot_along")
        self.comboBox_axis_to_plot_along.addItem("")
        self.comboBox_axis_to_plot_along.addItem("")
        self.comboBox_axis_to_plot_along.addItem("")
        self.comboBox_axis_to_plot_along.addItem("")
        self.comboBox_axis_to_plot_along.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_axis_to_plot_along, 1, 0, 1, 1)
        self.label_folder_to_process_files_3 = QtWidgets.QLabel(self.groupBox_processArbData)
        self.label_folder_to_process_files_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_folder_to_process_files_3.setObjectName("label_folder_to_process_files_3")
        self.gridLayout_2.addWidget(self.label_folder_to_process_files_3, 9, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_processArbData, 1, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 2, 1, 1)

        self.retranslateUi(Dialog)
        self.comboBox_axis_to_plot_along.setCurrentIndex(2)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox_processArbData.setTitle(_translate("Dialog", "Process raw spectra parameters"))
        self.comboBox_type_of_data.setItemText(0, _translate("Dialog", "pkl"))
        self.comboBox_type_of_data.setItemText(1, _translate("Dialog", "txt"))
        self.checkBox_isInterpolation.setText(_translate("Dialog", "Interpolation"))
        self.checkBox_is_remove_background_out_of_contact.setText(_translate("Dialog", "Out _of_contact data"))
        self.label_9.setText(_translate("Dialog", "Plot along axis"))
        self.checkBox_isAveraging.setToolTip(_translate("Dialog", "Straightforward averaging of all spectra at the point"))
        self.checkBox_isAveraging.setText(_translate("Dialog", "Averaging"))
        self.checkBox_isShifting.setToolTip(_translate("Dialog", "Calculate the averaged position of the spectrum (mainly for Apex)"))
        self.checkBox_isShifting.setText(_translate("Dialog", "Shifting"))
        self.comboBox_axis_to_plot_along.setToolTip(_translate("Dialog", "Choose channel to plot"))
        self.comboBox_axis_to_plot_along.setCurrentText(_translate("Dialog", "Z"))
        self.comboBox_axis_to_plot_along.setItemText(0, _translate("Dialog", "X"))
        self.comboBox_axis_to_plot_along.setItemText(1, _translate("Dialog", "Y"))
        self.comboBox_axis_to_plot_along.setItemText(2, _translate("Dialog", "Z"))
        self.comboBox_axis_to_plot_along.setItemText(3, _translate("Dialog", "W"))
        self.comboBox_axis_to_plot_along.setItemText(4, _translate("Dialog", "p"))
        self.label_folder_to_process_files_3.setText(_translate("Dialog", "Type of data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

