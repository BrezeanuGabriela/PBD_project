from Basic_Gui import *
from Oracle import *
import threading

if __name__ == "__main__":
    db=database()
    db_thread=threading.Thread(target=db.connect_to_db)
    db_thread.start()

    display_gui(db)