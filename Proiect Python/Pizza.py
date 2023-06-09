from PyQt5 import QtWidgets

import gui_pizza


class Pizza:
    def __init__(self,window,db):
        self.main_window=window
        self.database=db
        self.no_rows=6

    def print_pizza(self):
        self.pizza=gui_pizza.Pizza_TableWidget()
        self.pizza.setupUi(self.main_window,self.no_rows)

        self.pizza_tables = self.pizza.get_table()
        self.populate_pizza()
        self.pizza.show_table()

        #insert
        self.insert_pizza_main_button, self.denumire_pizza_line, self.gramaj_pizza_line, self.pret_pizza_line, self.add_pizza_button=\
            self.pizza.get_insert_boxes()

        self.denumire_pizza = ''
        self.gramaj_pizza = ''
        self.pret_pizza = ''

        self.insert_pizza_main_button.clicked.connect(self.insert)
        self.add_pizza_button.clicked.connect(self.add_new_pizza)

        #update
        self.update_pizza_main_button, self.id_pizza_update_combo_box, self.set_pizza_combo_box, \
        self.new_value_pizza_line, self.set_pizza_button=self.pizza.get_update_boxes()

        self.update_pizza_main_button.clicked.connect(self.update_pizza)
        self.set_pizza_button.clicked.connect(self.update)

        self.optiune_selectata = ''

        #delete
        self.delete_pizza_main_button, self.id_pizza_delete_combo_box, self.delete_pizza_button=self.pizza.get_delete_boxes()
        self.delete_pizza_main_button.clicked.connect(self.delete)
        self.delete_pizza_button.clicked.connect(self.delete_pizza)

    def populate_pizza(self):
        query = "select * from tipuri_pizza order by id_pizza"
        self.rez = ""
        try:
            self.rez = self.database.execute_query(query)
        except Exception as err:
            print(err)

        # add data
        table_data = []
        for pizza in self.rez:
            table_data.append(list(pizza))
        # print(table_data)

        row = 0
        for r in table_data:
            col = 0
            for item in r:
                cell = QtWidgets.QTableWidgetItem(str(item))
                self.pizza_tables.setItem(row, col, cell)
                col += 1
            row += 1

    def hide(self):
        self.pizza.hide_pizza()

    def get_denumire_pizza(self):
        self.denumire_pizza = self.denumire_pizza_line.text()

    def get_gramaj_pizza(self):
        self.gramaj_pizza=self.gramaj_pizza_line.text()

    def get_pret_pizza(self):
        self.pret_pizza=self.pret_pizza_line.text()

    def insert(self):
        self.denumire_pizza_line.returnPressed.connect(lambda: self.get_denumire_pizza())
        self.gramaj_pizza_line.returnPressed.connect(lambda: self.get_gramaj_pizza())
        self.pret_pizza_line.returnPressed.connect(lambda: self.get_pret_pizza())

    def add_new_pizza(self):
        try:
            query = "insert into tipuri_pizza (denumire, gramaj, pret) " \
                    "values ('{}',{},{})"\
                .format(self.denumire_pizza, int(self.gramaj_pizza),int(self.pret_pizza))
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
            self.pizza.set_no_rows(self.no_rows)
        #print(self.clients_tables.rowCount())
        self.populate_pizza()

    def selectionchange_id(self,i):
        self.id_selectat=self.id_pizza_update_combo_box.currentText()
        #print(self.id_selectat)

    def selectionchange_optiune(self,i):
        self.optiune_selectata=self.set_pizza_combo_box.currentText()

    def update_pizza(self):
        query = "select id_pizza from tipuri_pizza order by id_pizza"
        rez = ""
        list_id=[]
        try:
            rez = self.database.execute_query(query)
        except Exception as err:
            print(err)
        list_id.append("tip pizza")
        for id in rez:
            for i in id:
                list_id.append(str(i))
        #print(list_id)

        try:
            if self.id_pizza_update_combo_box.count() != 0:
                self.id_pizza_update_combo_box.clear()
        except Exception as err:
            print(err)

        try:
            self.id_pizza_update_combo_box.addItems(list_id)
        except Exception as err:
            print(err)

        try:
            self.id_pizza_update_combo_box.currentIndexChanged.connect(self.selectionchange_id)
        except Exception as err:
            print(err)

        lista_optiuni=['optiuni:','denumire','gramaj','pret']

        try:
            if self.set_pizza_combo_box.count() != 0:
                self.set_pizza_combo_box.clear()
        except Exception as err:
            print(err)

        try:
            self.set_pizza_combo_box.addItems(lista_optiuni)
        except Exception as err:
            print(err)

        self.set_pizza_combo_box.currentIndexChanged.connect(self.selectionchange_optiune)

        self.value=0
        self.new_value_pizza_line.returnPressed.connect(lambda: self.get_text_new_value())

    def get_text_new_value(self):
        # getting text from the line edit
        self.value = self.new_value_pizza_line.text()

    def update(self):
        try:
            if str(self.optiune_selectata) == 'denumire':
                query = "update tipuri_pizza set {}='{}' where id_pizza={}".format(self.optiune_selectata.upper(),self.value,self.id_selectat)
                print(query)
            else:
                query = "update tipuri_pizza set {}='{}' where id_pizza={}".format(self.optiune_selectata.upper(),int(self.value),self.id_selectat)
                print(query)
        except Exception as err:
            print(err)

        try:
            self.database.execute_query(query)
        except Exception as err:
            print(err)
        self.populate_pizza()

    def get_id_pizza_delete(self,i):
        self.id_pizza_next_to_delete = self.id_pizza_delete_combo_box.currentText()

    def delete(self):
        query = "select id_pizza from tipuri_pizza"
        rez = ""
        list_id = []
        try:
            rez = self.database.execute_query(query)
        except Exception as err:
            print(err)
        list_id.append("id pizza")
        for id in rez:
            for i in id:
                list_id.append(str(i))
        # print(list_id)

        try:
            if self.id_pizza_delete_combo_box.count()!=0:
                self.id_pizza_delete_combo_box.clear()
        except Exception as err:
            print(err)

        try:
            self.id_pizza_delete_combo_box.addItems(list_id)
        except Exception as err:
            print(err)

        self.id_pizza_delete_combo_box.currentIndexChanged.connect(self.get_id_pizza_delete)

    def delete_pizza(self):
        try:
            query = "delete tipuri_pizza where ID_pizza={}".format(int(self.id_pizza_next_to_delete))
        except Exception as err:
            print(err)

        print(query)
        ok=1
        try:
            self.database.execute_query(query)
        except Exception as err:
            print(err)
            ok=0
        if ok:
            self.no_rows-=1
            self.pizza.set_no_rows(self.no_rows)
        self.populate_pizza()