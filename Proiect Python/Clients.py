from PyQt5 import QtWidgets

import gui_clients


class Client:
    def __init__(self,window,db):
        self.main_window=window
        self.database=db
        self.no_rows=9

    def print_clients(self):
        self.clients=gui_clients.Clients_TableWidget()
        self.clients.setupUi(self.main_window,self.no_rows)

        self.clients_tables = self.clients.get_table()
        self.populate_clients()
        self.clients.show_table()

        # insert
        self.insert_client_main_button, self.nume_client_line, self.prenume_client_line, self.telefon_client_line, \
        self.email_client_line, self.cartier_client_line, self.nr_cartier_client_line, self.nr_bloc_client_line, \
        self.etaj_client_line, self.nr_apartament_client_line, self.add_client_button = self.clients.get_insert_boxes()

        self.nume = ''
        self.prenume = ''
        self.telefon = ''
        self.email = ''
        self.cartier = ''
        self.nr_cartier = ''
        self.nr_bloc = ''
        self.nr_apartament=''

        self.insert_client_main_button.clicked.connect(self.insert)
        self.add_client_button.clicked.connect(self.add_new_client)

        # update
        self.update_client_main_button, self.id_client_update_combo_box, self.set_client_combo_box, \
        self.new_value_client_line, self.set_client_button=self.clients.get_update_boxes()

        self.optiune_selectata = ''

        self.update_client_main_button.clicked.connect(self.update_client)
        self.set_client_button.clicked.connect(self.update)

        #delete
        self.delete_client_main_button, self.id_client_delete_combo_box, self.delete_client_button=self.clients.get_delete_boxes()
        self.delete_client_main_button.clicked.connect(self.delete)
        self.delete_client_button.clicked.connect(self.delete_client)

    def populate_clients(self):
        query = "select * from client order by id_client"
        self.rez = ""
        try:
            self.rez = self.database.execute_query(query)
        except Exception as err:
            print(err)

        # add data
        table_data = []
        for client in self.rez:
            table_data.append(list(client))
        # print(table_data)

        row = 0
        for r in table_data:
            col = 0
            for item in r:
                cell = QtWidgets.QTableWidgetItem(str(item))
                self.clients_tables.setItem(row, col, cell)
                col += 1
            row += 1

    def hide(self):
        self.clients.hide_clients()

    def get_nume(self):
        self.nume = self.nume_client_line.text()

    def get_prenume(self):
        self.prenume=self.prenume_client_line.text()

    def get_telefon(self):
        self.telefon=self.telefon_client_line.text()

    def get_email(self):
        self.email=self.email_client_line.text()

    def get_cartier(self):
        self.cartier=self.cartier_client_line.text()

    def get_nr_cartier(self):
        self.nr_cartier=self.nr_cartier_client_line.text()

    def get_nr_bloc(self):
        self.nr_bloc=self.nr_bloc_client_line.text()

    def get_etaj(self):
        self.etaj=self.etaj_client_line.text()

    def get_nr_apartament(self):
        self.nr_apartament=self.nr_apartament_client_line.text()

    def insert(self):
        self.nume_client_line.returnPressed.connect(lambda: self.get_nume())
        self.prenume_client_line.returnPressed.connect(lambda: self.get_prenume())
        self.telefon_client_line.returnPressed.connect(lambda: self.get_telefon())
        self.email_client_line.returnPressed.connect(lambda: self.get_email())
        self.cartier_client_line.returnPressed.connect(lambda: self.get_cartier())
        self.nr_cartier_client_line.returnPressed.connect(lambda: self.get_nr_cartier())
        self.nr_bloc_client_line.returnPressed.connect(lambda: self.get_nr_bloc())
        self.etaj_client_line.returnPressed.connect(lambda: self.get_etaj())
        self.nr_apartament_client_line.returnPressed.connect(lambda: self.get_nr_apartament())

    def add_new_client(self):
        try:
            query = "insert into client (nume, prenume, telefon, email, cartier, numar_cartier, nr_bloc,etaj,nr_apartament) " \
                    "values ('{}','{}','{}','{}','{}',{},{},{},{})"\
                .format(self.nume, self.prenume,self.telefon,self.email, self.cartier, int(self.nr_cartier),
                        int(self.nr_bloc),int(self.etaj),int(self.nr_apartament))
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
            self.clients.set_no_rows(self.no_rows)
        #print(self.clients_tables.rowCount())
        self.populate_clients()

    def selectionchange_id(self,i):
        self.id_selectat=int(self.id_client_update_combo_box.currentText())
        #print(self.id_selectat)

    def selectionchange_optiune(self,i):
        self.optiune_selectata=self.set_client_combo_box.currentText()

    def update_client(self):
        query = "select id_client from client"
        rez = ""
        list_id=[]
        try:
            rez = self.database.execute_query(query)
        except Exception as err:
            print(err)
        list_id.append("id client")
        for id in rez:
            for i in id:
                list_id.append(str(i))
        #print(list_id)

        try:
            self.id_client_update_combo_box.addItems(list_id)
        except Exception as err:
            print(err)
        self.id_client_update_combo_box.currentIndexChanged.connect(self.selectionchange_id)

        lista_optiuni=['optiuni:','nume','prenume','telefon','email','cartier','numar_cartier','nr_bloc','etaj','nr_apartament']

        #print(f'set updt:{self.set_combo_box.count()}')
        try:
            if self.set_client_combo_box.count() != 0:
                self.set_client_combo_box.clear()
        except Exception as err:
            print(err)

        try:
            self.set_client_combo_box.addItems(lista_optiuni)
        except Exception as err:
            print(err)
        self.set_client_combo_box.currentIndexChanged.connect(self.selectionchange_optiune)

        # adding action to the line edit when enter key is pressed
        self.value=0
        self.new_value_client_line.returnPressed.connect(lambda: self.get_text_new_value())

    def get_text_new_value(self):
        # getting text from the line edit
        self.value = self.new_value_client_line.text()

    def update(self):
        try:
            if str(self.optiune_selectata) == 'nume'or self.optiune_selectata=='prenume' or \
                    self.optiune_selectata=='telefon' or self.optiune_selectata=='email' or self.optiune_selectata=='cartier':
                query = "update client set {}='{}' where ID_client={}".format(self.optiune_selectata.upper(),self.value,self.id_selectat)
                print(query)
            else:
                query = "update client set {}='{}' where ID_client={}".format(self.optiune_selectata.upper(), int(self.value),
                                                                        self.id_selectat)
        except Exception as err:
            print(err)

        try:
            self.database.execute_query(query)
        except Exception as err:
            print(err)
        self.populate_clients()

    def get_id_client_delete(self,i):
        self.id_client_next_to_delete = int(self.id_client_delete_combo_box.currentText())

    def delete(self):
        query = "select id_client from client"
        rez = ""
        list_id = []
        try:
            rez = self.database.execute_query(query)
        except Exception as err:
            print(err)
        list_id.append("id sofer")
        for id in rez:
            for i in id:
                list_id.append(str(i))
        # print(list_id)

        try:
            self.id_client_delete_combo_box.addItems(list_id)
        except Exception as err:
            print(err)

        self.id_client_delete_combo_box.currentIndexChanged.connect(self.get_id_client_delete)

    def delete_client(self):
        try:
            query = "delete client where ID_client={}".format(int(self.id_client_next_to_delete))
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
            self.clients.set_no_rows(self.no_rows)
        self.populate_clients()


