from PyQt5 import QtWidgets

import gui_drivers


class Driver:
    def __init__(self,window,db):
        self.main_window=window
        self.database=db
        self.no_rows=6

    def print_soferi(self):
        self.drivers=gui_drivers.Drivers_TableWidget()
        self.drivers.setupUi(self.main_window,self.no_rows)

        # insert
        self.insert_button, self.nume_driver_line, self.prenume_driver_line, self.cnp_driver_line, self.telefon_driver_line, \
        self.email_driver_line, self.salariu_driver_line, self.pos_driver_line, self.nr_masina_driver_combo_box, \
        self.add_driver_button = self.drivers.get_insert_boxes()

        self.insert_button.clicked.connect(self.insert)
        self.add_driver_button.clicked.connect(self.add_new_driver)

        self.nume = ''
        self.prenume = ''
        self.cnp = ''
        self.telefon = ''
        self.email = ''
        self.salariu = ''
        self.pos = ''
        self.nr_masina = ''

        #update
        self.update_button=self.drivers.get_update_button()
        self.update_button.clicked.connect(self.update_driver)

        self.set_button = self.drivers.get_update_driver_button()
        self.set_button.clicked.connect(self.update)

        self.id_combo_box = self.drivers.get_id_sofer_button()
        self.set_combo_box = self.drivers.get_set_button()
        self.new_value = self.drivers.get_new_value_line()

        self.optiune_selectata = ''

        #delete
        self.delete_button=self.drivers.get_delete_driver_button()
        self.delete_button.clicked.connect(self.delete)
        self.delete_button_command=self.drivers.get_delete_command_button()
        self.delete_button_command.clicked.connect(self.delete_driver)

        self.id_driver_to_delete=self.drivers.get_delete_id_driver()
        self.id_driver_to_delete_combo_box=self.drivers.get_delete_combo_box()

        self.drivers_tables=self.drivers.get_table()
        self.populate_drivers()
        self.drivers.show_table()

        try:
            self.no_rows=self.drivers_tables.rowCount() #la insert pt marirea tabelului si la delete pt micsorare
        except Exception as err:
            print(err)

    def populate_drivers(self):
        query="select * from sofer order by id_sofer"
        self.rez=""
        try:
            self.rez=self.database.execute_query(query)
        except Exception as err:
            print(err)

        # add data
        table_data = []
        for sofer in self.rez:
            table_data.append(list(sofer))
        #print(table_data)

        row = 0
        for r in table_data:
            col = 0
            for item in r:
                cell = QtWidgets.QTableWidgetItem(str(item))
                self.drivers_tables.setItem(row, col, cell)
                col += 1
            row += 1

    def hide(self):
        self.drivers.hide_drivers()

    def update_driver(self):
        query = "select id_sofer from sofer"
        rez = ""
        list_id=[]
        try:
            rez = self.database.execute_query(query)
        except Exception as err:
            print(err)
        list_id.append("id sofer")
        for id in rez:
            for i in id:
                list_id.append(str(i))
        #print(list_id)


        try:
            self.id_combo_box.addItems(list_id)
        except Exception as err:
            print(err)
        self.id_combo_box.currentIndexChanged.connect(self.selectionchange_id)

        lista_optiuni=['optiuni:','nume','prenume','cnp','telefon','email','salariu','pos','numar_masina']

        #print(f'set updt:{self.set_combo_box.count()}')
        try:
            if self.set_combo_box.count() != 0:
                self.set_combo_box.clear()
        except Exception as err:
            print(err)

        try:
            self.set_combo_box.addItems(lista_optiuni)
        except Exception as err:
            print(err)
        self.set_combo_box.currentIndexChanged.connect(self.selectionchange_optiune)

        # adding action to the line edit when enter key is pressed
        self.value=0
        self.new_value.returnPressed.connect(lambda: self.get_text_new_value())

    def get_text_new_value(self):
        # getting text from the line edit
        self.value = self.new_value.text()

    def get_nume(self):
        self.nume = self.nume_driver_line.text()

    def get_prenume(self):
        self.prenume=self.prenume_driver_line.text()

    def get_cnp(self):
        self.cnp=self.cnp_driver_line.text()

    def get_telefon(self):
        self.telefon=self.telefon_driver_line.text()

    def get_email(self):
        self.email=self.email_driver_line.text()

    def get_salariu(self):
        self.salariu=self.salariu_driver_line.text()

    def get_pos(self):
        self.pos=self.pos_driver_line.text()

    def insert(self):
        query = "select NUMAR_MASINA from masina"
        rez = ""
        list_id = []
        try:
            rez = self.database.execute_query(query)
        except Exception as err:
            print(err)
        list_id.append("nr_masina")
        for id in rez:
            for i in id:
                list_id.append(str(i))
        # print(list_id)

        #print(f'count nr masini:{self.nr_masina_driver_combo_box.count()}')
        try:
            if self.nr_masina_driver_combo_box.count()!=0:
                self.nr_masina_driver_combo_box.clear()
        except Exception as err:
            print(err)

        try:
            self.nr_masina_driver_combo_box.addItems(list_id)
        except Exception as err:
            print(err)

        self.nume_driver_line.returnPressed.connect(lambda: self.get_nume())
        self.prenume_driver_line.returnPressed.connect(lambda: self.get_prenume())
        self.cnp_driver_line.returnPressed.connect(lambda: self.get_cnp())
        self.telefon_driver_line.returnPressed.connect(lambda: self.get_telefon())
        self.email_driver_line.returnPressed.connect(lambda: self.get_email())
        self.salariu_driver_line.returnPressed.connect(lambda: self.get_salariu())
        self.pos_driver_line.returnPressed.connect(lambda: self.get_pos())

        self.nr_masina_driver_combo_box.currentIndexChanged.connect(self.get_numar_masina)
        #print(self.nume, self.prenume, self.cnp, self.telefon, self.email, self.salariu,
        #      self.pos, self.nr_masina)

    def add_new_driver(self):
        try:
            query = "insert into sofer (nume, prenume, cnp, telefon, email, salariu, pos,numar_masina) values ('{}','{}',{},'{}','{}',\
                    {},{},'{}')".format(self.nume, self.prenume,int(self.cnp),self.telefon, self.email, int(self.salariu),
                                    int(self.pos),self.nr_masina)
            #3print(query)
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
            self.drivers.set_no_rows(self.no_rows)
        self.populate_drivers()

    def get_numar_masina(self,i):
        self.nr_masina=self.nr_masina_driver_combo_box.currentText()

    def selectionchange_id(self,i):
        self.id_selectat=int(self.id_combo_box.currentText())
        #print(self.id_selectat)

    def selectionchange_optiune(self,i):
        self.optiune_selectata=self.set_combo_box.currentText()
        #print(self.optiune_selectata,'kkkk')

    def update(self):
        try:
            if str(self.optiune_selectata) == 'nume'or self.optiune_selectata=='prenume' or \
                    self.optiune_selectata=='telefon' or self.optiune_selectata=='email' or self.optiune_selectata=='numar_masina':
                query = "update SOFER set {}='{}' where ID_SOFER={}".format(self.optiune_selectata.upper(),self.value,self.id_selectat)
                print(query)
            else:
                query = "update SOFER set {}='{}' where ID_SOFER={}".format(self.optiune_selectata.upper(), int(self.value),
                                                                        self.id_selectat)
        except Exception as err:
            print(err)

        try:
            self.database.execute_query(query)
        except Exception as err:
            print(err)
        self.populate_drivers()

    def get_id_driver_delete(self,i):
        self.id_driver_next_to_delete = int(self.id_driver_to_delete.currentText())

    def delete(self):
        query = "select id_sofer from sofer"
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
            self.id_driver_to_delete.addItems(list_id)
        except Exception as err:
            print(err)

        self.id_driver_to_delete.currentIndexChanged.connect(self.get_id_driver_delete)

    def delete_driver(self):
        try:
            query = "delete SOFER where ID_SOFER={}".format(int(self.id_driver_next_to_delete))
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
            self.drivers.set_no_rows(self.no_rows)
        self.populate_drivers()


