from PyQt5 import QtWidgets

import gui_cars


class Car:
    def __init__(self,window,db):
        self.main_window=window
        self.database=db
        self.no_rows=8

    def print_cars(self):
        self.cars=gui_cars.Cars_TableWidget()
        self.cars.setupUi(self.main_window,self.no_rows)

        self.cars_tables = self.cars.get_table()
        self.populate_cars()
        self.cars.show_table()

        # insert
        self.insert_car_main_button, self.numar_masina_line, self.an_masina_line, self.add_car_button = self.cars.get_insert_boxes()

        self.numar_masina = ''
        self.an_masina = ''
        self.model_masina = 'UP 1'
        self.marca='VW'

        self.insert_car_main_button.clicked.connect(self.insert)
        self.add_car_button.clicked.connect(self.add_new_car)

        #update
        self.update_car_main_button, self.id_car_update_combo_box, self.set_car_combo_box, \
        self.new_value_car_line, self.set_car_button=self.cars.get_update_boxes()

        self.update_car_main_button.clicked.connect(self.update_car)
        self.set_car_button.clicked.connect(self.update)

        self.optiune_selectata = ''

        #delete
        self.delete_car_main_button, self.id_car_delete_combo_box, self.delete_car_button=self.cars.get_delete_boxes()

        self.delete_car_main_button.clicked.connect(self.delete)
        self.delete_car_button.clicked.connect(self.delete_car)

    def populate_cars(self):
        query = "select * from masina order by numar_masina"
        self.rez = ""
        try:
            self.rez = self.database.execute_query(query)
        except Exception as err:
            print(err)

        # add data
        table_data = []
        for masina in self.rez:
            table_data.append(list(masina))
        # print(table_data)

        row = 0
        for r in table_data:
            col = 0
            for item in r:
                cell = QtWidgets.QTableWidgetItem(str(item))
                self.cars_tables.setItem(row, col, cell)
                col += 1
            row += 1

    def hide(self):
        self.cars.hide_cars()

    def get_numar_masina(self):
        self.numar_masina = self.numar_masina_line.text()

    def get_an_masina(self):
        self.an_masina=self.an_masina_line.text()

    def insert(self):
        self.numar_masina_line.returnPressed.connect(lambda: self.get_numar_masina())
        self.an_masina_line.returnPressed.connect(lambda: self.get_an_masina())

    def add_new_car(self):
        try:
            query = "insert into masina (numar_masina, marca, model, an_fabricatie) " \
                    "values ('{}','{}','{}',{})"\
                .format(self.numar_masina, self.marca,self.model_masina,int(self.an_masina))
            print(query)
        except Exception as err:
            print(err)

        ok = 1
        try:
            self.database.execute_query(query)
        except Exception as err:
            print(err)
            ok = 0
        if ok:
            self.no_rows += 1
            self.cars.set_no_rows(self.no_rows)
        self.populate_cars()

    def selectionchange_id(self,i):
        #print(i)
        self.id_selectat=self.id_car_update_combo_box.currentText()
        #print(self.id_selectat)

    def selectionchange_optiune(self,i):
        self.optiune_selectata=self.set_car_combo_box.currentText()

    def update_car(self):
        query = "select numar_masina from masina"
        rez = ""
        list_id=[]
        try:
            rez = self.database.execute_query(query)
        except Exception as err:
            print(err)
        list_id.append("numar masina")
        for id in rez:
            for i in id:
                list_id.append(str(i))
        #print(list_id)

        try:
            if self.id_car_update_combo_box.count() != 0:
                self.id_car_update_combo_box.clear()
        except Exception as err:
            print(err)

        try:
            self.id_car_update_combo_box.addItems(list_id)
        except Exception as err:
            print(err)

        try:
            self.id_car_update_combo_box.currentIndexChanged.connect(self.selectionchange_id)
        except Exception as err:
            print(err)

        lista_optiuni=['optiuni:','numar_masina','an_fabricatie']

        try:
            if self.set_car_combo_box.count() != 0:
                self.set_car_combo_box.clear()
        except Exception as err:
            print(err)

        try:
            self.set_car_combo_box.addItems(lista_optiuni)
        except Exception as err:
            print(err)

        self.set_car_combo_box.currentIndexChanged.connect(self.selectionchange_optiune)

        self.value=0
        self.new_value_car_line.returnPressed.connect(lambda: self.get_text_new_value())

    def get_text_new_value(self):
        # getting text from the line edit
        self.value = self.new_value_car_line.text()

    def update(self):
        try:
            if str(self.optiune_selectata) == 'numar_masina':
                query = "update masina set {}='{}' where numar_masina='{}'".format(self.optiune_selectata.upper(),self.value,self.id_selectat)
                print(query)
            else:
                query = "update masina set {}='{}' where numar_masina='{}'".format(self.optiune_selectata.upper(), self.value,
                                                                        self.id_selectat)
                print(query)
        except Exception as err:
            print(err)

        try:
            self.database.execute_query(query)
        except Exception as err:
            print(err)
        self.populate_cars()

    def get_id_car_delete(self,i):
        self.id_car_next_to_delete = self.id_car_delete_combo_box.currentText()

    def delete(self):
        query = "select numar_masina from masina"
        rez = ""
        list_id = []
        try:
            rez = self.database.execute_query(query)
        except Exception as err:
            print(err)
        list_id.append("numar_masina")
        for id in rez:
            for i in id:
                list_id.append(str(i))
        # print(list_id)

        try:
            if self.id_car_delete_combo_box.count() != 0:
                self.id_car_delete_combo_box.clear()
        except Exception as err:
            print(err)

        try:
            self.id_car_delete_combo_box.addItems(list_id)
        except Exception as err:
            print(err)

        self.id_car_delete_combo_box.currentIndexChanged.connect(self.get_id_car_delete)

    def delete_car(self):
        try:
            query = "delete masina where numar_masina='{}'".format(self.id_car_next_to_delete)
            print(query)
        except Exception as err:
            print(err)

        ok=1
        try:
            self.database.execute_query(query)
        except Exception as err:
            print(err)
            ok=0
        if ok:
            self.no_rows-=1
            self.cars.set_no_rows(self.no_rows)
        self.populate_cars()




