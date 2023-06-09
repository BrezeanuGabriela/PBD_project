from PyQt5 import QtWidgets

import gui_com_pizza


class Com_pizza:
    def __init__(self,window,db,bon):
        self.main_window=window
        self.database=db
        self.no_rows=15
        self.bon_comanda=bon

    def print_comenzi_explicite(self):
        self.comenzi_explicite=gui_com_pizza.Com_pizza_TableWidget()
        self.comenzi_explicite.setupUi(self.main_window,self.no_rows)

        self.comenzi_tables = self.comenzi_explicite.get_table()
        self.populate_comenzi()
        self.comenzi_explicite.show_table()

        #insert
        self.insert_com_pizza_main_button, self.id_comanda_insert_combo_box, self.id_pizza_insert_combo_box, \
        self.cantitate_insert_line, self.add_command_button= \
            self.comenzi_explicite.get_insert_boxes()

        self.id_comanda_insert=''
        self.cantitate_insert=''

        self.insert_com_pizza_main_button.clicked.connect(self.insert)
        try:
            self.add_command_button.clicked.connect(self.add_new_comanda)
        except Exception as err:
            print(err)

        #update
        self.update_com_pizza_main_button, self.id_comanda_update_combo_box, self.set_comanda_combo_box, self.new_value_comanda_line, \
        self.set_command_button = self.comenzi_explicite.get_update_boxes()

        self.update_com_pizza_main_button.clicked.connect(self.update_comanda)
        self.set_command_button.clicked.connect(self.update)

        self.optiune_selectata = ''

        #delete
        self.delete_com_pizza_main_button, self.id_comanda_delete_combo_box, self.delete_comanda_button=self.comenzi_explicite.get_delete_boxes()
        self.delete_com_pizza_main_button.clicked.connect(self.delete)
        self.delete_comanda_button.clicked.connect(self.delete_comanda)

    def populate_comenzi(self):
        query = "select * from com_pizza_fk order by comanda_id_comanda"
        self.rez = ""
        try:
            self.rez = self.database.execute_query(query)
        except Exception as err:
            print(err)

        # add data
        table_data = []
        for id in self.rez:
            table_data.append(list(id))
        #print(table_data)

        row = 0
        for r in table_data:
            col = 0
            for item in r:
                cell = QtWidgets.QTableWidgetItem(str(item))
                self.comenzi_tables.setItem(row, col, cell)
                col += 1
            row += 1

    def hide(self):
        self.comenzi_explicite.hide_comenzi()

    def get_id_comanda_insert(self,i):
        self.id_comanda_insert=self.id_comanda_insert_combo_box.currentText()

    def get_id_pizza_insert(self,i):
        self.id_pizza_insert=self.id_pizza_insert_combo_box.currentText()

    def get_cantitate(self):
        self.cantitate_insert=self.cantitate_insert_line.text()

    def insert(self):
        query = "select id_comanda from comanda order by id_comanda"
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
        # print(list_id)

        try:
            if self.id_comanda_insert_combo_box.count() != 0:
                self.id_comanda_insert_combo_box.clear()
        except Exception as err:
            print(err)

        try:
            self.id_comanda_insert_combo_box.addItems(list_id)
        except Exception as err:
            print(err)

        try:
            self.id_comanda_insert_combo_box.currentIndexChanged.connect(self.get_id_comanda_insert)
        except Exception as err:
            print(err)

        query = "select id_pizza from tipuri_pizza order by id_pizza"
        rez = ""
        list_id = []
        try:
            rez = self.database.execute_query(query)
        except Exception as err:
            print(err)
        list_id.append("id_pizza")
        for id in rez:
            for i in id:
                list_id.append(str(i))
        # print(list_id)

        try:
            if self.id_pizza_insert_combo_box.count() != 0:
                self.id_pizza_insert_combo_box.clear()
        except Exception as err:
            print(err)

        try:
            self.id_pizza_insert_combo_box.addItems(list_id)
        except Exception as err:
            print(err)

        try:
            self.id_pizza_insert_combo_box.currentIndexChanged.connect(self.get_id_pizza_insert)
        except Exception as err:
            print(err)

        self.cantitate_insert_line.returnPressed.connect(lambda: self.get_cantitate())

    def add_new_comanda(self):
        try:
            query = "insert into com_pizza_fk (comanda_id_comanda, tipuri_pizza_id_pizza, cantitate) " \
                    "values ({},{},{})"\
                .format(int(self.id_comanda_insert), int(self.id_pizza_insert),int(self.cantitate_insert))
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
            self.comenzi_explicite.set_no_rows(self.no_rows)
            self.update_card_fidelitate()
        #print(self.clients_tables.rowCount())
        self.populate_comenzi()

        no_rows_bon=self.bon_comanda.get_no_rows()+1
        try:
            #print(self.bon_comanda)
            self.bon_comanda.set_no_rows(no_rows_bon)
        except Exception as err:
            print(err)

    #se adauga numarul de puncte corespunzator noii comenzi
    def update_card_fidelitate(self):
        query = "select distinct id_client from comanda where id_comanda={}".format(int(self.id_comanda_insert))
        try:
            self.rez = self.database.execute_query(query)
        except Exception as err:
            print(err)
        self.id_client=0
        for i in self.rez:
            for id in i:
                self.id_client=id

        try:
            query="update card_fidelitate set nr_puncte=nr_puncte+0.1* \
                    (select pret from tipuri_pizza, com_pizza_fk c \
                    where c.comanda_id_comanda={} and id_pizza={} and c.tipuri_pizza_id_pizza={}) where id_client={}".\
                        format(int(self.id_comanda_insert),int(self.id_pizza_insert),int(self.id_pizza_insert),int(self.id_client))
            print(query)
        except Exception as err:
            print(err)

        try:
            self.database.execute_query(query)
        except Exception as err:
            print(err)

    def selectionchange_id(self,i):
        self.id_selectat=self.id_comanda_update_combo_box.currentText()
        #print(self.id_selectat)

    def selectionchange_optiune(self,i):
        self.optiune_selectata=self.set_comanda_combo_box.currentText()

    def update_comanda(self):
        query = "select distinct comanda_id_comanda from com_pizza_fk order by comanda_id_comanda"
        rez = ""
        list_id=[]
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
            self.id_comanda_update_combo_box.currentIndexChanged.connect(self.selectionchange_id)
        except Exception as err:
            print(err)

        lista_optiuni=['optiuni:','tipuri_pizza_id_pizza','cantitate']

        try:
            if self.set_comanda_combo_box.count() != 0:
                self.set_comanda_combo_box.clear()
        except Exception as err:
            print(err)

        try:
            self.set_comanda_combo_box.addItems(lista_optiuni)
        except Exception as err:
            print(err)

        self.set_comanda_combo_box.currentIndexChanged.connect(self.selectionchange_optiune)

        self.value=0
        self.new_value_comanda_line.returnPressed.connect(lambda: self.get_text_new_value())

    def get_text_new_value(self):
        # getting text from the line edit
        self.value = self.new_value_comanda_line.text()

    def update(self):
        try:
            query = "update com_pizza_fk set {}='{}' where comanda_id_comanda={}".format(self.optiune_selectata.upper(),float(self.value),self.id_selectat)
            print(query)
        except Exception as err:
            print(err)

        try:
            self.database.execute_query(query)
        except Exception as err:
            print(err)
        self.populate_comenzi()

    def get_id_comanda_delete(self,i):
        self.id_comanda_next_to_delete = self.id_comanda_delete_combo_box.currentText()

    def delete(self):
        query = "select distinct comanda_id_comanda from com_pizza_fk order by comanda_id_comanda"
        rez = ""
        list_id = []
        try:
            rez = self.database.execute_query(query)
        except Exception as err:
            print(err)
        list_id.append("id comanda")
        for id in rez:
            for i in id:
                list_id.append(str(i))
        # print(list_id)

        try:
            if self.id_comanda_delete_combo_box.count()!=0:
                self.id_comanda_delete_combo_box.clear()
        except Exception as err:
            print(err)

        try:
            self.id_comanda_delete_combo_box.addItems(list_id)
        except Exception as err:
            print(err)

        self.id_comanda_delete_combo_box.currentIndexChanged.connect(self.get_id_comanda_delete)

    def delete_comanda(self):
        print("\nTranzactiile efectuate simultan cu stergerea unei comenzi...........................")
        self.update_nr_puncte_card_delete()

        query="select count(*) from com_pizza_fk where comanda_id_comanda={}".format(int(self.id_comanda_next_to_delete))
        print(query)
        try:
            rez=self.database.execute_query(query)
        except Exception as err:
            print(err)

        data=[]
        for i in rez:
            data.append(list(i))

        for elem in data:
            nr_tipuri_pizza_comanda_stearsa=elem[0]
        #print(nr_tipuri_pizza)

        try:
            query = "delete com_pizza_fk where comanda_id_comanda={}".format(int(self.id_comanda_next_to_delete))
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
            self.no_rows-=nr_tipuri_pizza_comanda_stearsa
            self.comenzi_explicite.set_no_rows(self.no_rows)
        self.populate_comenzi()

        self.update_comanda_delete()

    #se sterg punctele corespunzatoare comenzii care va fi eliminata
    def update_nr_puncte_card_delete(self):
        try:
            query="select tipuri_pizza_id_pizza,cantitate from com_pizza_fk where comanda_id_comanda={}".format(int(self.id_comanda_next_to_delete))
        except Exception as err:
            print(err)
        print(query)
        try:
            rez=self.database.execute_query(query)
        except Exception as err:
            print(err)
        data=[]
        for i in rez:
            data.append(list(i))

        tip_pizza=[]
        cantitate=[]
        for elem in data:
            tip_pizza.append(elem[0])
            cantitate.append(elem[1])
        if len(tip_pizza)>1:
            query="select pret from tipuri_pizza where id_pizza in {}".format(tuple(tip_pizza))
        else:
            query = "select pret from tipuri_pizza where id_pizza={}".format(tip_pizza[0])
        print(query)
        try:
            rez = self.database.execute_query(query)
        except Exception as err:
            print(err)

        data=[]
        for i in rez:
            data.append(list(i))
        #print(data)

        pret=[]
        for elem in data:
            pret.append(elem[0])
        #print(pret)
        nr_puncte_minus=0

        #print(len(pret))
        for i in range(0,len(pret)):
            nr_puncte_minus+=pret[i]*cantitate[i]*0.1
        #print(nr_puncte_minus)

        query="select id_client from comanda where id_comanda={}".format(int(self.id_comanda_next_to_delete))
        print(query)
        try:
            rez = self.database.execute_query(query)
        except Exception as err:
            print(err)

        data=[]
        for i in rez:
            data.append(list(i))

        for elem in data:
            id_client=elem[0]

        #stergem punctele
        query="update card_fidelitate set nr_puncte=nr_puncte-{} where id_client={}".format(nr_puncte_minus,id_client)
        print(query)
        try:
            self.database.execute_query(query)
        except Exception as err:
            print(err)

    def update_comanda_delete(self):
        query = "delete comanda where id_comanda={}".format(int(self.id_comanda_next_to_delete))
        print(query)
        try:
            self.database.execute_query(query)
        except Exception as err:
            print(err)

    def get_no_rows(self):
        return self.no_rows
