import sys
import time

from PyQt5 import QtCore,QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget

import Bon
import Card
import Cars
import Clients
import Com_pizza
import Command
import Drivers
import Pizza
import gui_drivers
from Oracle import *

class basic_page(QtWidgets.QMainWindow):
    def __init__(self,db):
        self.database=db
        self.drivers = Drivers.Driver(self,db)
        self.clients=Clients.Client(self,db)
        self.cars=Cars.Car(self, db)
        self.pizza=Pizza.Pizza(self,db)
        self.card=Card.Card(self,db)
        self.command=Command.Command(self,db)
        self.bon = Bon.Bon(self, db)
        self.comenzi_explicite=Com_pizza.Com_pizza(self, db,self.bon)


        super(basic_page, self).__init__(parent=None)
        #self.setStyleSheet("background-color: ciel")
        self.setWindowTitle("Delivery pizza")
        self.resize(900,350)
        self.center()
        self.initUI()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def initUI(self):
        #layout=QtWidgets.QHBoxLayout()
        menu_bar=self.menuBar()
        #self.menuBar().setStyleSheet("background-color : green")

        clienti=menu_bar.addMenu("Clienti")
        show_all_clients=QtWidgets.QAction("Toti clientii",self)
        show_all_clients.triggered.connect(self.print_client)
        clienti.addAction(show_all_clients)
        #clienti.addAction("Clasament clienti")

        carduri = menu_bar.addMenu("Card fidelitate")
        show_cards = QtWidgets.QAction("Carduri fidelitate", self)
        show_cards.triggered.connect(self.print_card)
        carduri.addAction(show_cards)

        soferi=menu_bar.addMenu("Soferi")
        show_drivers=QtWidgets.QAction("Soferi disponibili",self)
        try:
            show_drivers.triggered.connect(self.print_driver)
        except Exception as err:
            print(err)
        soferi.addAction(show_drivers)

        masini=menu_bar.addMenu("Masini")
        show_cars = QtWidgets.QAction("Toate masinile", self)
        show_cars.triggered.connect(self.print_cars)
        masini.addAction(show_cars)

        meniu=menu_bar.addMenu("Meniu")
        show_meniu = QtWidgets.QAction("Tipuri pizza", self)
        show_meniu.triggered.connect(self.print_meniu)
        meniu.addAction(show_meniu)

        comenzi = menu_bar.addMenu("Comenzi")
        show_commands = QtWidgets.QAction("Toate comenzile", self)
        show_commands.triggered.connect(self.print_command)
        comenzi.addAction(show_commands)

        comenzi_exp = menu_bar.addMenu("Comenzi detaliate")
        show_com_pizza = QtWidgets.QAction("Continut comenzi", self)
        show_com_pizza.triggered.connect(self.print_com_pizza)
        comenzi_exp.addAction(show_com_pizza)

        bonuri = menu_bar.addMenu("Bonuri")
        show_bonuri = QtWidgets.QAction("Un fel de bon", self)
        show_bonuri.triggered.connect(self.print_bonuri)
        bonuri.addAction(show_bonuri)

        save = menu_bar.addMenu("Save")
        salveaza = QtWidgets.QAction("Save changes", self)
        salveaza.triggered.connect(self.save_changes)
        save.addAction(salveaza)

        #self.setLayout(layout)

    def print_driver(self):
        try:
            self.bon.hide()
        except Exception as err:
            print(err)

        try:
            self.clients.hide()
        except Exception as err:
            print(err)

        try:
            self.cars.hide()
        except Exception as err:
            print(err)

        try:
            self.pizza.hide()
        except Exception as err:
            print(err)

        try:
            self.card.hide()
        except Exception as err:
            print(err)

        try:
            self.command.hide()
        except Exception as err:
            print(err)

        try:
            self.comenzi_explicite.hide()
        except Exception as err:
            print(err)

        self.drivers.print_soferi()

    def print_client(self):
        try:
            self.bon.hide()
        except Exception as err:
            print(err)

        try:
            self.drivers.hide()
        except Exception as err:
            print(err)

        try:
            self.cars.hide()
        except Exception as err:
            print(err)

        try:
            self.pizza.hide()
        except Exception as err:
            print(err)

        try:
            self.card.hide()
        except Exception as err:
            print(err)

        try:
            self.command.hide()
        except Exception as err:
            print(err)

        try:
            self.comenzi_explicite.hide()
        except Exception as err:
            print(err)

        self.clients.print_clients()

    def print_cars(self):
        try:
            self.bon.hide()
        except Exception as err:
            print(err)

        try:
            self.drivers.hide()
        except Exception as err:
            print(err)

        try:
            self.clients.hide()
        except Exception as err:
            print(err)

        try:
            self.pizza.hide()
        except Exception as err:
            print(err)

        try:
            self.card.hide()
        except Exception as err:
            print(err)

        try:
            self.command.hide()
        except Exception as err:
            print(err)

        try:
            self.comenzi_explicite.hide()
        except Exception as err:
            print(err)

        self.cars.print_cars()

    def print_meniu(self):
        try:
            self.bon.hide()
        except Exception as err:
            print(err)

        try:
            self.drivers.hide()
        except Exception as err:
            print(err)

        try:
            self.clients.hide()
        except Exception as err:
            print(err)

        try:
            self.cars.hide()
        except Exception as err:
            print(err)

        try:
            self.card.hide()
        except Exception as err:
            print(err)

        try:
            self.command.hide()
        except Exception as err:
            print(err)

        try:
            self.comenzi_explicite.hide()
        except Exception as err:
            print(err)

        try:
            self.pizza.print_pizza()
        except Exception as err:
            print(err)

    def print_card(self):
        try:
            self.bon.hide()
        except Exception as err:
            print(err)

        try:
            self.drivers.hide()
        except Exception as err:
            print(err)

        try:
            self.clients.hide()
        except Exception as err:
            print(err)

        try:
            self.cars.hide()
        except Exception as err:
            print(err)

        try:
            self.pizza.hide()
        except Exception as err:
            print(err)

        try:
            self.command.hide()
        except Exception as err:
            print(err)

        try:
            self.comenzi_explicite.hide()
        except Exception as err:
            print(err)

        try:
            self.card.print_cards()
        except Exception as err:
            print(err)

    def print_command(self):
        try:
            self.bon.hide()
        except Exception as err:
            print(err)

        try:
            self.drivers.hide()
        except Exception as err:
            print(err)

        try:
            self.clients.hide()
        except Exception as err:
            print(err)

        try:
            self.cars.hide()
        except Exception as err:
            print(err)

        try:
            self.pizza.hide()
        except Exception as err:
            print(err)

        try:
            self.card.hide()
        except Exception as err:
            print(err)

        try:
            self.comenzi_explicite.hide()
        except Exception as err:
            print(err)

        try:
            self.command.print_commands()
        except Exception as err:
            print(err)

    def print_com_pizza(self):
        try:
            self.drivers.hide()
        except Exception as err:
            print(err)

        try:
            self.clients.hide()
        except Exception as err:
            print(err)

        try:
            self.cars.hide()
        except Exception as err:
            print(err)

        try:
            self.pizza.hide()
        except Exception as err:
            print(err)

        try:
            self.card.hide()
        except Exception as err:
            print(err)

        try:
            self.command.hide()
        except Exception as err:
            print(err)

        try:
            self.bon.hide()
        except Exception as err:
            print(err)

        try:
            self.comenzi_explicite.print_comenzi_explicite()
        except Exception as err:
            print(err)

    def print_bonuri(self):
        try:
            self.drivers.hide()
        except Exception as err:
            print(err)

        try:
            self.clients.hide()
        except Exception as err:
            print(err)

        try:
            self.cars.hide()
        except Exception as err:
            print(err)

        try:
            self.pizza.hide()
        except Exception as err:
            print(err)

        try:
            self.card.hide()
        except Exception as err:
            print(err)

        try:
            self.command.hide()
        except Exception as err:
            print(err)

        try:
            self.comenzi_explicite.hide()
        except Exception as err:
            print(err)

        try:
            self.bon.print_bonuri()
        except Exception as err:
            print(err)

    def save_changes(self):
        query = "commit"
        print(query)
        try:
            self.database.execute_query(query)
        except Exception as err:
            print(err)


def display_gui(db):
    app=QtWidgets.QApplication(sys.argv)
    menu=basic_page(db)
    menu.show()
    sys.exit(app.exec_())

