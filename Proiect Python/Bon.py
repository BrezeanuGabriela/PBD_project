from PyQt5 import QtWidgets

import gui_bon


class Bon:
    def __init__(self,window,db):
        self.main_window=window
        self.database=db
        self.no_rows=15

    def print_bonuri(self):
        self.bon=gui_bon.Bon_TableWidget()
        self.bon.setupUi(self.main_window,self.no_rows)

        self.bon_tables = self.bon.get_table()
        self.populate_bonuri()
        self.bon.show_table()

    def populate_bonuri(self):
        query = "with \
                com_pret_pizza as (\
                    select comanda_id_comanda, tipuri_pizza_id_pizza, pret,cantitate, pret*cantitate pret_pizza \
                        from tipuri_pizza tip, com_pizza_fk comd \
                        where tip.id_pizza=comd.tipuri_pizza_id_pizza), \
                pret_final as ( \
                    select distinct comanda_id_comanda, (select sum(pret_pizza) from com_pret_pizza c " \
                        "where c.comanda_id_comanda=c1.comanda_id_comanda) pret_total \
                            from com_pret_pizza c1 group by comanda_id_comanda, pret_pizza) \
                    select id_client, c.comanda_id_comanda,tipuri_pizza_id_pizza, pret, cantitate, pret_pizza, pret_total cost_total_comanda \
                from com_pret_pizza c, pret_final p, comanda cmd \
                    where c.comanda_id_comanda=p.comanda_id_comanda \
                        and cmd.id_comanda=c.comanda_id_comanda \
                        order by comanda_id_comanda"
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
                self.bon_tables.setItem(row, col, cell)
                col += 1
            row += 1

    def hide(self):
        self.bon.hide()

    def get_no_rows(self):
        return self.no_rows

    def set_no_rows(self,rows):
        self.no_rows=rows
        try:
            #print(self.bon)
            self.bon.set_no_rows(self.no_rows)
        except Exception as err:
            print(err)