# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_card.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Card_TableWidget(object):
    def setupUi(self, mainWidget,no_rows):
        mainWidget.setObjectName("mainWidget")
        mainWidget.resize(1303, 733)
        mainWidget.setAutoFillBackground(False)
        self.card_table = QtWidgets.QTableWidget(mainWidget)
        self.card_table.setGeometry(QtCore.QRect(310, 30, 531, 251))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.card_table.setFont(font)
        self.card_table.setRowCount(no_rows)
        self.card_table.setColumnCount(4)
        self.card_table.setObjectName("card_table")
        item = QtWidgets.QTableWidgetItem()
        self.card_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.card_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.card_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.card_table.setHorizontalHeaderItem(3, item)
        self.horizontalLayoutWidget = QtWidgets.QWidget(mainWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 320, 1151, 35))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.card_horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.card_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.card_horizontalLayout.setObjectName("card_horizontalLayout")
        self.insert_card_main_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.insert_card_main_button.setFont(font)
        self.insert_card_main_button.setObjectName("insert_card_main_button")
        self.card_horizontalLayout.addWidget(self.insert_card_main_button)
        self.update_card_main_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.update_card_main_button.setFont(font)
        self.update_card_main_button.setObjectName("update_card_main_button")
        self.card_horizontalLayout.addWidget(self.update_card_main_button)
        self.delete_card_main_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.delete_card_main_button.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.delete_card_main_button.setFont(font)
        self.delete_card_main_button.setObjectName("delete_card_main_button")
        self.card_horizontalLayout.addWidget(self.delete_card_main_button)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(mainWidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 370, 1151, 91))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.insert_horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.insert_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.insert_horizontalLayout.setObjectName("insert_horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.id_client_insert_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.id_client_insert_label.setFont(font)
        self.id_client_insert_label.setAlignment(QtCore.Qt.AlignCenter)
        self.id_client_insert_label.setWordWrap(False)
        self.id_client_insert_label.setObjectName("id_client_insert_label")
        self.verticalLayout.addWidget(self.id_client_insert_label)
        self.id_client_insert_combo_box = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.id_client_insert_combo_box.setFont(font)
        self.id_client_insert_combo_box.setObjectName("id_client_insert_combo_box")
        self.verticalLayout.addWidget(self.id_client_insert_combo_box)
        self.insert_horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.data_nastere_client_line = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.data_nastere_client_line.setFont(font)
        self.data_nastere_client_line.setObjectName("data_nastere_client_line")
        self.verticalLayout_4.addWidget(self.data_nastere_client_line)
        self.insert_horizontalLayout.addLayout(self.verticalLayout_4)
        self.add_card_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.add_card_button.setFont(font)
        self.add_card_button.setObjectName("add_card_button")
        self.insert_horizontalLayout.addWidget(self.add_card_button)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(mainWidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 480, 1151, 61))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.update_horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.update_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.update_horizontalLayout.setObjectName("update_horizontalLayout")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_9.addWidget(self.label_6)
        self.id_client_update_card_combo_box = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.id_client_update_card_combo_box.setFont(font)
        self.id_client_update_card_combo_box.setObjectName("id_client_update_card_combo_box")
        self.verticalLayout_9.addWidget(self.id_client_update_card_combo_box)
        self.update_horizontalLayout.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_10.addWidget(self.label_7)
        self.set_card_combo_box = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.set_card_combo_box.setFont(font)
        self.set_card_combo_box.setObjectName("set_card_combo_box")
        self.verticalLayout_10.addWidget(self.set_card_combo_box)
        self.update_horizontalLayout.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_11.addWidget(self.label_8)
        self.new_value_card_line = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.new_value_card_line.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.new_value_card_line.setFont(font)
        self.new_value_card_line.setObjectName("new_value_card_line")
        self.verticalLayout_11.addWidget(self.new_value_card_line)
        self.update_horizontalLayout.addLayout(self.verticalLayout_11)
        self.set_card_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.set_card_button.setFont(font)
        self.set_card_button.setObjectName("set_card_button")
        self.update_horizontalLayout.addWidget(self.set_card_button)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(mainWidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(20, 550, 238, 71))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.delete_driver_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.delete_driver_layout.setContentsMargins(0, 0, 0, 0)
        self.delete_driver_layout.setObjectName("delete_driver_layout")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_13.addWidget(self.label_9)
        self.id_client_delete_card_combo_box = QtWidgets.QComboBox(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.id_client_delete_card_combo_box.setFont(font)
        self.id_client_delete_card_combo_box.setObjectName("id_client_delete_card_combo_box")
        self.verticalLayout_13.addWidget(self.id_client_delete_card_combo_box)
        self.delete_driver_layout.addLayout(self.verticalLayout_13)
        self.delete_card_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.delete_card_button.setFont(font)
        self.delete_card_button.setObjectName("delete_card_button")
        self.delete_driver_layout.addWidget(self.delete_card_button)

        self.retranslateUi(mainWidget)
        QtCore.QMetaObject.connectSlotsByName(mainWidget)

    def retranslateUi(self, mainWidget):
        _translate = QtCore.QCoreApplication.translate
        mainWidget.setWindowTitle(_translate("mainWidget", "main"))
        item = self.card_table.horizontalHeaderItem(0)
        item.setText(_translate("mainWidget", "ID_client"))
        item = self.card_table.horizontalHeaderItem(1)
        item.setText(_translate("mainWidget", "ID_card"))
        item = self.card_table.horizontalHeaderItem(2)
        item.setText(_translate("mainWidget", "Data_nastere_client"))
        item = self.card_table.horizontalHeaderItem(3)
        item.setText(_translate("mainWidget", "Nr_puncte"))
        self.insert_card_main_button.setText(_translate("mainWidget", "Insert"))
        self.update_card_main_button.setText(_translate("mainWidget", "Update"))
        self.delete_card_main_button.setText(_translate("mainWidget", "Delete card"))
        self.id_client_insert_label.setText(_translate("mainWidget", "ID_client"))
        self.label.setText(_translate("mainWidget", "Data_nastere_client"))
        self.add_card_button.setText(_translate("mainWidget", "Add card"))
        self.label_6.setText(_translate("mainWidget", "ID_client"))
        self.label_7.setText(_translate("mainWidget", "Set"))
        self.label_8.setText(_translate("mainWidget", "New value"))
        self.set_card_button.setText(_translate("mainWidget", "Update card"))
        self.label_9.setText(_translate("mainWidget", "ID_client"))
        self.delete_card_button.setText(_translate("mainWidget", "Delete card"))

    def show_table(self):
        self.card_table.show()
        self.show_buttons()

    def get_table(self):
        return self.card_table

    def show_buttons(self):
        self.horizontalLayoutWidget.show()
        self.update_card_main_button.clicked.connect(lambda: self.show_update())
        self.insert_card_main_button.clicked.connect(lambda: self.show_insert())
        self.delete_card_main_button.clicked.connect(lambda: self.show_delete())

        self.horizontalLayoutWidget_2.hide()
        self.horizontalLayoutWidget_3.hide()
        self.horizontalLayoutWidget_4.hide()

    def show_insert(self):
        self.horizontalLayoutWidget_2.show()
        self.horizontalLayoutWidget_3.hide()
        self.horizontalLayoutWidget_4.hide()

    def show_update(self):
        self.horizontalLayoutWidget_2.hide()
        self.horizontalLayoutWidget_4.hide()
        self.horizontalLayoutWidget_3.show()

    def show_delete(self):
        self.horizontalLayoutWidget_2.hide()
        self.horizontalLayoutWidget_3.hide()
        self.horizontalLayoutWidget_4.show()

    def hide_card(self):
        self.card_table.hide()
        self.horizontalLayoutWidget.hide()
        self.horizontalLayoutWidget_2.hide()
        self.horizontalLayoutWidget_3.hide()
        self.horizontalLayoutWidget_4.hide()

    def get_insert_boxes(self):
        return self.insert_card_main_button, self.id_client_insert_combo_box, self.data_nastere_client_line, self.add_card_button

    def get_update_boxes(self):
        return self.update_card_main_button, self.id_client_update_card_combo_box, self.set_card_combo_box,\
               self.new_value_card_line,self.set_card_button

    def get_delete_boxes(self):
        return self.delete_card_main_button, self.id_client_delete_card_combo_box, self.delete_card_button

    def set_no_rows(self,rows):
        self.card_table.setRowCount(rows)


