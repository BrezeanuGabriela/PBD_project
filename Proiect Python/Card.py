from PyQt5 import QtWidgets

import gui_card


class Card:
    def __init__(self,window,db):
        self.main_window=window
        self.database=db
        self.no_rows=9

    def print_cards(self):
        self.card=gui_card.Card_TableWidget()
        self.card.setupUi(self.main_window,self.no_rows)

        self.card_tables = self.card.get_table()
        self.populate_cards()
        self.card.show_table()

        #insert
        self.insert_card_main_button, self.id_client_insert_combo_box, self.data_nastere_client_line, self.add_card_button=self.card.get_insert_boxes()

        self.id_client_insert = ''
        self.data_nastere_client = ''

        self.insert_card_main_button.clicked.connect(self.insert)
        self.add_card_button.clicked.connect(self.add_new_card)

        #update
        self.update_card_main_button, self.id_client_update_card_combo_box, self.set_card_combo_box, \
            self.new_value_card_line, self.set_card_button=self.card.get_update_boxes()

        self.update_card_main_button.clicked.connect(self.update_card)
        self.set_card_button.clicked.connect(self.update)

        self.optiune_selectata = ''

        #delete
        self.delete_card_main_button, self.id_client_delete_card_combo_box, self.delete_card_button=self.card.get_delete_boxes()
        self.delete_card_main_button.clicked.connect(self.delete)
        self.delete_card_button.clicked.connect(self.delete_card)


    def populate_cards(self):
        query = "select * from card_fidelitate order by id_client"
        self.rez = ""
        try:
            self.rez = self.database.execute_query(query)
        except Exception as err:
            print(err)

        # add data
        table_data = []
        for id in self.rez:
            table_data.append(list(id))
        # print(table_data)

        row = 0
        for r in table_data:
            col = 0
            for item in r:
                cell = QtWidgets.QTableWidgetItem(str(item))
                self.card_tables.setItem(row, col, cell)
                col += 1
            row += 1

    def hide(self):
        self.card.hide_card()

    def get_id_client_insert(self,i):
        self.id_client_insert=self.id_client_insert_combo_box.currentText()
        #print(self.id_selectat)

    def get_data_nastere_client(self):
        #print(self.data_nastere_client_line.text())
        self.data_nastere_client=str(self.data_nastere_client_line.text())

    def insert(self):
        query = "select id_client from client order by id_client"
        rez = ""
        list_id = []
        try:
            rez = self.database.execute_query(query)
        except Exception as err:
            print(err)
        list_id.append("id_client")
        for id in rez:
            for i in id:
                list_id.append(str(i))
        # print(list_id)

        try:
            if self.id_client_insert_combo_box.count() != 0:
                self.id_client_insert_combo_box.clear()
        except Exception as err:
            print(err)

        try:
            self.id_client_insert_combo_box.addItems(list_id)
        except Exception as err:
            print(err)

        try:
            self.id_client_insert_combo_box.currentIndexChanged.connect(self.get_id_client_insert)
        except Exception as err:
            print(err)

        self.data_nastere_client_line.returnPressed.connect(lambda: self.get_data_nastere_client())

    def add_new_card(self):
        try:
            query = "insert into card_fidelitate (id_client, data_nastere_client) " \
                    "values ({},'{}')"\
                .format(int(self.id_client_insert), self.data_nastere_client)
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
            self.card.set_no_rows(self.no_rows)
        #print(self.clients_tables.rowCount())
        self.populate_cards()

    def selectionchange_id(self,i):
        self.id_selectat=self.id_client_update_card_combo_box.currentText()
        #print(self.id_selectat)

    def selectionchange_optiune(self,i):
        self.optiune_selectata=self.set_card_combo_box.currentText()

    def update_card(self):
        query = "select id_client from card_fidelitate order by id_client"
        rez = ""
        list_id=[]
        try:
            rez = self.database.execute_query(query)
        except Exception as err:
            print(err)
        list_id.append("id_client")
        for id in rez:
            for i in id:
                list_id.append(str(i))
        #print(list_id)

        try:
            if self.id_client_update_card_combo_box.count() != 0:
                self.id_client_update_card_combo_box.clear()
        except Exception as err:
            print(err)

        try:
            self.id_client_update_card_combo_box.addItems(list_id)
        except Exception as err:
            print(err)

        try:
            self.id_client_update_card_combo_box.currentIndexChanged.connect(self.selectionchange_id)
        except Exception as err:
            print(err)

        lista_optiuni=['optiuni:','data_nastere_client','nr_puncte']

        try:
            if self.set_card_combo_box.count() != 0:
                self.set_card_combo_box.clear()
        except Exception as err:
            print(err)

        try:
            self.set_card_combo_box.addItems(lista_optiuni)
        except Exception as err:
            print(err)

        self.set_card_combo_box.currentIndexChanged.connect(self.selectionchange_optiune)

        self.value=0
        self.new_value_card_line.returnPressed.connect(lambda: self.get_text_new_value())

    def get_text_new_value(self):
        # getting text from the line edit
        self.value = self.new_value_card_line.text()

    def update(self):
        try:
            if str(self.optiune_selectata) == 'data_nastere_client':
                query = "update card_fidelitate set {}='{}' where id_client={}".format(self.optiune_selectata.upper(),self.value,self.id_selectat)
                print(query)
            else:
                query = "update card_fidelitate set {}='{}' where id_client={}".format(self.optiune_selectata.upper(),float(self.value),self.id_selectat)
                print(query)
        except Exception as err:
            print(err)

        try:
            self.database.execute_query(query)
        except Exception as err:
            print(err)
        self.populate_cards()

    def get_id_card_delete(self,i):
        self.id_card_next_to_delete = self.id_client_delete_card_combo_box.currentText()

    def delete(self):
        query = "select id_client from card_fidelitate order by id_client"
        rez = ""
        list_id = []
        try:
            rez = self.database.execute_query(query)
        except Exception as err:
            print(err)
        list_id.append("id client")
        for id in rez:
            for i in id:
                list_id.append(str(i))
        # print(list_id)

        try:
            if self.id_client_delete_card_combo_box.count()!=0:
                self.id_client_delete_card_combo_box.clear()
        except Exception as err:
            print(err)

        try:
            self.id_client_delete_card_combo_box.addItems(list_id)
        except Exception as err:
            print(err)

        self.id_client_delete_card_combo_box.currentIndexChanged.connect(self.get_id_card_delete)

    def delete_card(self):
        try:
            query = "delete card_fidelitate where id_client={}".format(int(self.id_card_next_to_delete))
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
            self.card.set_no_rows(self.no_rows)
        self.populate_cards()