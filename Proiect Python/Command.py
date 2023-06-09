from PyQt5 import QtWidgets

import gui_command


class Command:
    def __init__(self,window,db):
        self.main_window=window
        self.database=db
        self.no_rows=14

    def print_commands(self):
        self.commands=gui_command.Command_TableWidget()
        self.commands.setupUi(self.main_window,self.no_rows)

        self.commands_tables = self.commands.get_table()
        self.populate_commands()
        self.commands.show_table()

        #insert
        self.insert_comanda_main_button, self.id_client_insert_combo_box, self.data_comanda_line, self.onorata_comanda_line, \
        self.id_sofer_insert_combo_box, self.POS_comanda_insert_line, self.add_command_button = self.commands.get_insert_boxes()

        self.id_client_insert=''
        self.data_comanda=''
        self.onorata=''
        self.id_sofer_insert=''
        self.POS_insert=''

        self.insert_comanda_main_button.clicked.connect(self.insert)
        self.add_command_button.clicked.connect(self.add_new_command)

        #update
        self.update_comanda_main_button, self.id_client_update_comanda_combo_box, self.id_comanda_update_combo_box, self.set_comanda_combo_box, \
        self.new_value_comanda_line, self.set_command_button = self.commands.get_update_boxes()

        self.update_comanda_main_button.clicked.connect(self.update_comanda)
        self.set_command_button.clicked.connect(self.update)

        self.optiune_selectata = ''
        self.id_client_update=1

        #delete
        self.delete_comanda_main_button, self.id_client_delete_comanda_combo_box, self.id_comanda_delete_comanda_combo_box, \
        self.delete_comanda_button = self.commands.get_delete_boxes()

        self.id_client_next_to_delete=1

        self.delete_comanda_main_button.clicked.connect(self.delete)
        self.delete_comanda_button.clicked.connect(self.delete_comanda)

    def populate_commands(self):
        query = "select * from comanda order by id_client"
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
                self.commands_tables.setItem(row, col, cell)
                col += 1
            row += 1

    def hide(self):
        self.commands.hide_commands()

    def get_id_client_insert(self,i):
        self.id_client_insert=self.id_client_insert_combo_box.currentText()

    def get_data_comanda_insert(self):
        self.data_comanda=self.data_comanda_line.text()

    def get_onorata_insert(self):
        self.onorata=self.onorata_comanda_line.text()

    def get_id_sofer_insert(self):
        self.id_sofer_insert=self.id_sofer_insert_combo_box.currentText()

    def get_pos_insert(self):
        self.POS_insert=self.POS_comanda_insert_line.text()

    def insert(self):
        self.get_clients_id()
        self.get_drivers_id()
        self.data_comanda_line.returnPressed.connect(lambda: self.get_data_comanda_insert())
        self.onorata_comanda_line.returnPressed.connect(lambda: self.get_onorata_insert())
        self.POS_comanda_insert_line.returnPressed.connect(lambda: self.get_pos_insert())

    def get_clients_id(self):
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

    def get_drivers_id(self):
        query = "select id_sofer from sofer order by id_sofer"
        rez = ""
        list_id = []
        try:
            rez = self.database.execute_query(query)
        except Exception as err:
            print(err)
        list_id.append("id_sofer")
        for id in rez:
            for i in id:
                list_id.append(str(i))
        # print(list_id)

        try:
            if self.id_sofer_insert_combo_box.count() != 0:
                self.id_sofer_insert_combo_box.clear()
        except Exception as err:
            print(err)

        try:
            self.id_sofer_insert_combo_box.addItems(list_id)
        except Exception as err:
            print(err)

        try:
            self.id_sofer_insert_combo_box.currentIndexChanged.connect(self.get_id_sofer_insert)
        except Exception as err:
            print(err)

    def add_new_command(self):
        try:
            query = "insert into comanda (id_client, data_comanda,onorata, ID_sofer, POS) " \
                    "values ({},'{}',{},{},{})"\
                .format(int(self.id_client_insert), self.data_comanda, int(self.onorata),int(self.id_sofer_insert),int(self.POS_insert))
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
            self.commands.set_no_rows(self.no_rows)
        #print(self.clients_tables.rowCount())
        self.populate_commands()

    def get_id_client_update(self, i):
        self.id_client_update = self.id_client_update_comanda_combo_box.currentText()
        self.get_commands_id_update()

    def get_id_comanda_update(self, i):
        self.id_comanda_update = self.id_comanda_update_combo_box.currentText()

    def selectionchange_optiune(self,i):
        self.optiune_selectata=self.set_comanda_combo_box.currentText()

    def update_comanda(self):
        try:
            self.get_clients_id_update()
        except Exception as err:
            print(err)
        #try:
        #    self.get_commands_id_update()
        #except Exception as err:
        #    print(err)
        lista_optiuni=['optiuni:','data_comanda','onorata','id_sofer','pos']

        try:
            if self.set_comanda_combo_box.count() != 0:
                self.set_comanda_combo_box.clear()
        except Exception as err:
            print(err)

        try:
            self.set_comanda_combo_box.addItems(lista_optiuni)
        except Exception as err:
            print(err)
        #print(lista_optiuni)
        self.set_comanda_combo_box.currentIndexChanged.connect(self.selectionchange_optiune)

        self.value=0
        self.new_value_comanda_line.returnPressed.connect(lambda: self.get_text_new_value())

    def get_clients_id_update(self):
        query = "select distinct id_client from comanda order by id_client"
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
        #print(list_id)

        #try:
        #    if self.id_client_update_comanda_combo_box.count() != 0:
        #        self.id_client_update_comanda_combo_box.clear()
        #except Exception as err:
        #    print(err)

        #print(self.id_client_update_comanda_combo_box.count())
        try:
            self.id_client_update_comanda_combo_box.addItems(list_id)
        except Exception as err:
            print(err)

        try:
            self.id_client_update_comanda_combo_box.currentIndexChanged.connect(self.get_id_client_update)
        except Exception as err:
            print(err)

    def get_commands_id_update(self):
        query = "select id_comanda from comanda where id_client={}".format(int(self.id_client_update))
        rez = ""
        list_id = []
        try:
            rez = self.database.execute_query(query)
        except Exception as err:
            print(err)
        list_id.append("id_comanda")
        for id in rez:
            for i in id:
                list_id.append(str(i))
        #print(list_id)

        try:
            if self.id_comanda_update_combo_box.count() != 0:
                self.id_comanda_update_combo_box.clear()
        except Exception as err:
            print(err)

        try:
            self.id_comanda_update_combo_box.addItems(list_id)
        except Exception as err:
            print(err)

        try:
            self.id_comanda_update_combo_box.currentIndexChanged.connect(self.get_id_comanda_update)
        except Exception as err:
            print(err)

    def get_text_new_value(self):
        # getting text from the line edit
        self.value = self.new_value_comanda_line.text()

    def update(self):
        try:
            if str(self.optiune_selectata) == 'data_comanda':
                query = "update comanda set {}='{}' where id_client={} and id_comanda={}".format(self.optiune_selectata.upper(),self.value,
                                                                                    int(self.id_client_update),int(self.id_comanda_update))
                print(query)
            else:
                query = "update comanda set {}={} where id_client={} and id_comanda={}".format(self.optiune_selectata.upper(),int(self.value),
                                                                                     int(self.id_client_update),int(self.id_comanda_update))
                print(query)
        except Exception as err:
            print(err)

        try:
            self.database.execute_query(query)
        except Exception as err:
            print(err)
        self.populate_commands()

    def get_id_client_delete(self,i):
        self.id_client_next_to_delete = self.id_client_delete_comanda_combo_box.currentText()
        self.get_commands_id_delete()

    def get_id_comanda_delete(self,i):
        self.id_comanda_next_to_delete = self.id_comanda_delete_comanda_combo_box.currentText()

    def delete(self):
        self.get_clients_id_delete()
        #self.get_commands_id_delete()

    def delete_comanda(self):
        try:
            query = "delete comanda where id_client={} and id_comanda={}".format(int(self.id_client_next_to_delete),int(self.id_comanda_next_to_delete))
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
            self.commands.set_no_rows(self.no_rows)
        self.populate_commands()

    def get_clients_id_delete(self):
        query = "select distinct id_client from comanda order by id_client"
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

        #try:
        #    if self.id_client_delete_comanda_combo_box.count() != 0:
        #        self.id_client_delete_comanda_combo_box.clear()
        #except Exception as err:
        #    print(err)

        try:
            self.id_client_delete_comanda_combo_box.addItems(list_id)
        except Exception as err:
            print(err)

        try:
            self.id_client_delete_comanda_combo_box.currentIndexChanged.connect(self.get_id_client_delete)
        except Exception as err:
            print(err)

    def get_commands_id_delete(self):
        query = "select id_comanda from comanda where id_client={}".format(int(self.id_client_next_to_delete))
        rez = ""
        list_id = []
        try:
            rez = self.database.execute_query(query)
        except Exception as err:
            print(err)
        list_id.append("id_comanda")
        for id in rez:
            for i in id:
                list_id.append(str(i))
        #print(list_id)

        try:
            if self.id_comanda_delete_comanda_combo_box.count() != 0:
                self.id_comanda_delete_comanda_combo_box.clear()
        except Exception as err:
            print(err)

        try:
            self.id_comanda_delete_comanda_combo_box.addItems(list_id)
        except Exception as err:
            print(err)

        try:
            self.id_comanda_delete_comanda_combo_box.currentIndexChanged.connect(self.get_id_comanda_delete)
        except Exception as err:
            print(err)