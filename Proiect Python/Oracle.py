import cx_Oracle

class database:
    def __init__(self):
        lib_dir = "E:\Auxiliare\oracle\instant client\instantclient-basic-windows.x64-21.3.0.0.0\instantclient_21_3"
        try:
            cx_Oracle.init_oracle_client(lib_dir)
        except Exception as err:
            print(err)

        self.user = "bd019"
        self.password = "bd019"
        self.hostname = "bd-dc.cs.tuiasi.ro:1539/orcl"

    def connect_to_db(self):
        try:
            print("Se conecteaza la Oracle....")
            con = cx_Oracle.connect(self.user, self.password, self.hostname, encoding="UTF-8")
            print("S-a realizat conexiunea la baza de date Oracle cu succes")
            print(con.version)
            self.cursor = con.cursor()
        except Exception as err:
            print(err)

    def execute_query(self,query):
        answer = self.cursor.execute(query)
        return answer