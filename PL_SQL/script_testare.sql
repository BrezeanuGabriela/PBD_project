SET SERVEROUTPUT ON;
DECLARE
    v_client_id NUMBER;
    v_pizza_id NUMBER;
    v_id_comanda comenzi.id_comanda%TYPE;
    v_client clienti%ROWTYPE;
    
    your_custom_exception EXCEPTION;
    PRAGMA EXCEPTION_INIT(your_custom_exception, -20201);
BEGIN
    --------------------------------- INSERARI -------------------------------------
    
    ----- CLIENTI ------
    
    -- EXEMPLU DE TRANZACTIE CARE NU REUSESTE DIN CAUZA CK PT DATA NASTERII - sub 14 ani
    inserare_informatii.insereaza_client_si_card(
        'Barbuta',
        'Delia',
        '0756284758',
        'delia.barbuta@gmail.com',
        'central',
        12,
        2,
        4,
        7,
        '8-oct-2014'
    );
    
    -- EXEMPLU DE TRANZACTIE CARE NU REUSESTE DIN CAUZA CK PT TELEFON - mai putin de 10 cifre
    inserare_informatii.insereaza_client_si_card(
        'Barbuta',
        'Delia',
        '07562847',
        'delia.barbuta@gmail.com',
        'central',
        12,
        2,
        4,
        7,
        '8-oct-2002'
    );
    
    --- SI O TRANZACTIE REUSITA PE INSERT ----------
    inserare_informatii.insereaza_client_si_card(
        'Barbuta',
        'Delia',
        '0756284714',
        'delia.barbuta@gmail.com',
        'central',
        12,
        2,
        4,
        7,
        '8-oct-2002'
    );
    
    ---- PIZZA ----
    
    ---- TRANZACTIE REUSITA -----
    inserare_informatii.insereaza_pizza_si_stoc('Lala Spicy', 525, 55, 10);
    DBMS_OUTPUT.PUT_LINE('');
    
    ----- TRANZACTIE NEREUSITA -> Gramaj > 2000
    inserare_informatii.insereaza_pizza_si_stoc('Chicken', 2525, 55, 10);
    DBMS_OUTPUT.PUT_LINE('');
    
    ---- COMANDA ---
    ------- TRANZACTIE NEREUSITA -----------
    v_id_comanda := inserare_informatii.adauga_comanda('07456789011');
    DBMS_OUTPUT.PUT_LINE('');
    
    ------- TRANZACTIE REUSITA -----------
    v_id_comanda := inserare_informatii.adauga_comanda('0745678901');
    DBMS_OUTPUT.PUT_LINE('');
    
    ----- PRODUS ----
    ---- TRANZACTIE REUSITA ---
    inserare_informatii.adauga_produs_comanda('0745678901', v_id_comanda, 'Quattro Formaggi', 2);
    DBMS_OUTPUT.PUT_LINE('');
    
    --- TRANZACTIE NEREUSITA --- produs inexistent
    inserare_informatii.adauga_produs_comanda('0745678901', v_id_comanda, 'Prosciutto 222', 2);
    DBMS_OUTPUT.PUT_LINE('');
    
    -------------------------- ACTUALIZARI INFORMATII -----------------------
    
    --- UPDATE COMANDA -------
    
    -- actualizare cantitate produs comanda ---
    actualizare_informatii.actualizare_produs_comanda(v_id_comanda, 'Quattro Formaggi', 4);
    DBMS_OUTPUT.PUT_LINE('');
    
    -- actualizare status comanda
    actualizare_informatii.actualizare_status_comanda(v_id_comanda);
    DBMS_OUTPUT.PUT_LINE('');
    
    -- trebuie decomentat pentru a exemplifica generand direct exceptii
    
    -- tentativa de a actualiza cantitatea unui produs dupa ce a fost finalizata comanda
--    actualizare_informatii.actualizare_produs_comanda(v_id_comanda, 'Quattro Formaggi', 2);
    DBMS_OUTPUT.PUT_LINE('');
    
    -- tentativa de a actualiza din nou statusul comenzii - exemplu de tranzactie nereusita cu exceptie generata, tratata in catch ul de mai jos
--    actualizare_informatii.actualizare_status_comanda(v_id_comanda);
    
    -- TESTARE TRIGGER PT VERIFICAREA DATEI - din nou cu exceptie pana aici 
    -- tentativa de a actualiza data comenzii pt trecut si viitor
--    UPDATE comenzi SET data_comanda = ADD_MONTHS(sysdate, -1) WHERE id_comanda = v_id_comanda;
--    UPDATE comenzi SET data_comanda = ADD_MONTHS(sysdate, 1) WHERE id_comanda = v_id_comanda;
    
    -- test pentru a observa eroarea generata de o cantitate mult prea mare fata de cea existenta in stoc
--    v_id_comanda := inserare_informatii.adauga_comanda('0712345678');
--    inserare_informatii.adauga_produs_comanda('0712345678', v_id_comanda, 'Quattro Formaggi', 52);
--    actualizare_informatii.actualizare_status_comanda(v_id_comanda);
    
    ------- STERGERE INFORMATII ------------
    v_id_comanda := inserare_informatii.adauga_comanda('0712345678');
    inserare_informatii.adauga_produs_comanda('0712345678', v_id_comanda, 'Quattro Formaggi', 1);
    DBMS_OUTPUT.PUT_LINE('');
    inserare_informatii.adauga_produs_comanda('0712345678', v_id_comanda, 'Hawaiian', 2);
    DBMS_OUTPUT.PUT_LINE('');
    inserare_informatii.adauga_produs_comanda('0712345678', v_id_comanda, 'Diavola', 3);
    DBMS_OUTPUT.PUT_LINE('');
    inserare_informatii.adauga_produs_comanda('0712345678', v_id_comanda, 'Vegetariana', 3);
    DBMS_OUTPUT.PUT_LINE('');
    -- actualizare cantitate produs comanda --- pentru a ilustra ca si daca se update cu 0 buc, se va sterge produsul din comanda
    actualizare_informatii.actualizare_produs_comanda(v_id_comanda, 'Vegetariana', 0);
    DBMS_OUTPUT.PUT_LINE('');
    sterge_informatii.sterge_produs_comanda(v_id_comanda, 'Quattro Formaggi');
    DBMS_OUTPUT.PUT_LINE('');
    actualizare_informatii.actualizare_status_comanda(v_id_comanda);
    DBMS_OUTPUT.PUT_LINE('');
    
    ------- VIZUALIZARI -----
    
    -- Exemplu de pizza care nu exista --
    v_pizza_id := vizualizare_informatii.extrage_id_pizza('Mamma Mia');
    
    IF v_pizza_id != -1 THEN
        DBMS_OUTPUT.PUT_LINE('ID-ul pentru pizza Mamma Mia: ' || v_pizza_id);
        DBMS_OUTPUT.PUT_LINE('');
    END IF;        
    
    
    -------- VIZUALIZARE COMENZI ---------------------
    vizualizare_informatii.vizualizare_toate_comenzile();
    DBMS_OUTPUT.PUT_LINE('');
    
    vizualizare_informatii.vizualizare_comenzi_nefinalizate();
    DBMS_OUTPUT.PUT_LINE('');

    vizualizare_informatii.vizualizare_comenzi_finalizate();
    DBMS_OUTPUT.PUT_LINE('');
    
     DBMS_OUTPUT.PUT_LINE('MENIU:');
    vizualizare_informatii.vizualizare_meniu();
    DBMS_OUTPUT.PUT_LINE('');
    
     -------- VIZUALIZARE PENTRU DIFERITE TOP-URI ----------
    vizualizare_informatii.top_3_clienti_fideli();
    DBMS_OUTPUT.PUT_LINE('');
    
    vizualizare_informatii.top_3_pizza_comandate();
    DBMS_OUTPUT.PUT_LINE('');
    
    EXCEPTION
        WHEN your_custom_exception THEN
            DBMS_OUTPUT.PUT_LINE('Eroare: ' || SQLERRM);
        WHEN OTHERS THEN
            DBMS_OUTPUT.PUT_LINE('Eroare: ' || SQLERRM);
END;
/