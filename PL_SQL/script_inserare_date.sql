SET SERVEROUTPUT ON;
DECLARE
    v_id_comanda comenzi.id_comanda%TYPE;
BEGIN       
        -- INSERARE CLIENTI + CARDURI FIDELITATE ----       
        -- Client 0
        inserare_informatii.insereaza_client_si_card(
            'Brezeanu',
            'Gabriela',
            '0756287210',
            'gabriela.brezeanu@gmail.com',
            'zorilor',
            10,
            2,
            4,
            7,
            '30-may-2000'
        );
        
        -- Client 1
        inserare_informatii.insereaza_client_si_card(
            'Ionescu',
            'Maria',
            '0712345678',
            'maria.ionescu@gmail.com',
            'central',
            10,
            2,
            4,
            7,
            '25-jan-2000'
        );
    
        -- Client 2
        inserare_informatii.insereaza_client_si_card(
            'Popa',
            'Andrei',
            '0723456789',
            'andrei.popa@gmail.com',
            'avram iancu',
            20,
            1,
            2,
            3,
            '10-mar-1988'
        );
    
        -- Client 3
        inserare_informatii.insereaza_client_si_card(
            'Stan',
            'Ana',
            '0734567890',
            'ana.stan@gmail.com',
            'floresti',
            15,
            4,
            3,
            9,
            '05-apr-1992'
        );
    
        -- Client 4
        inserare_informatii.insereaza_client_si_card(
            'Dumitrescu',
            'Mihai',
            '0745678901',
            'mihai.dumitrescu@gmail.com',
            'zorilor',
            30,
            5,
            6,
            11,
            '20-may-1980'
        );
    
        -- Client 5
        inserare_informatii.insereaza_client_si_card(
            'Pop',
            'Elena',
            '0756789012',
            'elena.pop@gmail.com',
            'manastur',
            25,
            3,
            5,
            8,
            '30-jul-1997'
        );
    
        -- Client 6
        inserare_informatii.insereaza_client_si_card(
            'Mihai',
            'Andreea',
            '0767890123',
            'andreea.mihai@gmail.com',
            'grigorescu',
            18,
            2,
            3,
            6,
            '12-aug-1993'
        );
    
        -- Client 7
        inserare_informatii.insereaza_client_si_card(
            'Radu',
            'Cristian',
            '0778901234',
            'cristian.radu@gmail.com',
            'marasti',
            22,
            3,
            2,
            4,
            '28-sep-1985'
        );
    
        -- Client 8
        inserare_informatii.insereaza_client_si_card(
            'Popescu',
            'Alexandra',
            '0789012345',
            'alexandra.popescu@gmail.com',
            'manastur',
            25,
            5,
            7,
            12,
            '05-nov-1990'
        );
    
        -- Client 9
        inserare_informatii.insereaza_client_si_card(
            'Dragoi',
            'Ionut',
            '0790123456',
            'ionut.dragoi@gmail.com',
            'zorilor',
            30,
            6,
            10,
            20,
            '15-dec-1998'
        );
    
        -- Client 10
        inserare_informatii.insereaza_client_si_card(
            'Vasilescu',
            'Diana',
            '0701234567',
            'diana.vasilescu@gmail.com',
            'gheorgheni',
            12,
            4,
            5,
            9,
            '25-jul-1994'
            );
        
        ----------- INSERARE TIPURI DE PIZZA SI STOCURI ----------------
        inserare_informatii.insereaza_pizza_si_stoc('Margherita', 450, 30, 8);
        inserare_informatii.insereaza_pizza_si_stoc('Pepperoni', 500, 40, 12);
        inserare_informatii.insereaza_pizza_si_stoc('Hawaiian', 480, 45, 10);
        inserare_informatii.insereaza_pizza_si_stoc('Vegetariana', 550, 35, 9);
        inserare_informatii.insereaza_pizza_si_stoc('Capriciosa', 520, 42, 11);
        inserare_informatii.insereaza_pizza_si_stoc('Quattro Stagioni', 540, 48, 10);
        inserare_informatii.insereaza_pizza_si_stoc('Diavola', 510, 47, 14);
        inserare_informatii.insereaza_pizza_si_stoc('Prosciutto', 490, 38, 12);
        inserare_informatii.insereaza_pizza_si_stoc('Quattro Formaggi', 570, 50, 18);
        inserare_informatii.insereaza_pizza_si_stoc('Tres Spicy', 525, 55, 10);
        
        -------------- INSERARE COMENZI ---------
        
        -- Comanda1
        v_id_comanda := inserare_informatii.adauga_comanda('0767890123');
        inserare_informatii.adauga_produs_comanda('0767890123', v_id_comanda, 'Quattro Formaggi', 1);
        inserare_informatii.adauga_produs_comanda('0767890123', v_id_comanda, 'Hawaiian', 2);
        inserare_informatii.adauga_produs_comanda('0767890123', v_id_comanda, 'Diavola', 3); 
        actualizare_informatii.actualizare_status_comanda(v_id_comanda);
    
        -- Comanda2
        v_id_comanda := inserare_informatii.adauga_comanda('0767890123');
        inserare_informatii.adauga_produs_comanda('0767890123', v_id_comanda, 'Quattro Formaggi', 1);
        inserare_informatii.adauga_produs_comanda('0767890123', v_id_comanda, 'Hawaiian', 1);
        inserare_informatii.adauga_produs_comanda('0767890123', v_id_comanda, 'Diavola', 1); 
        actualizare_informatii.actualizare_status_comanda(v_id_comanda);
        
         -- Comanda3
        v_id_comanda := inserare_informatii.adauga_comanda('0778901234');
        inserare_informatii.adauga_produs_comanda('0767890123', v_id_comanda, 'Diavola', 1); 
        actualizare_informatii.actualizare_status_comanda(v_id_comanda);
        
         -- Comanda4
        v_id_comanda := inserare_informatii.adauga_comanda('0778901234');
        inserare_informatii.adauga_produs_comanda('0767890123', v_id_comanda, 'Hawaiian', 1); 
        actualizare_informatii.actualizare_status_comanda(v_id_comanda);
        
        -- Comanda5
        v_id_comanda := inserare_informatii.adauga_comanda('0778901234');
        inserare_informatii.adauga_produs_comanda('0767890123', v_id_comanda, 'Quattro Formaggi', 1); 
        actualizare_informatii.actualizare_status_comanda(v_id_comanda);
        
        -- Comanda6
        v_id_comanda := inserare_informatii.adauga_comanda('0789012345');
        inserare_informatii.adauga_produs_comanda('0789012345', v_id_comanda, 'Pepperoni', 1);
        inserare_informatii.adauga_produs_comanda('0789012345', v_id_comanda, 'Hawaiian', 1);
        inserare_informatii.adauga_produs_comanda('0789012345', v_id_comanda, 'Diavola', 1);
        inserare_informatii.adauga_produs_comanda('0789012345', v_id_comanda, 'Tres Spicy', 1);
        actualizare_informatii.actualizare_status_comanda(v_id_comanda);
        
        -- Comanda7
        v_id_comanda := inserare_informatii.adauga_comanda('0789012345');
        inserare_informatii.adauga_produs_comanda('0789012345', v_id_comanda, 'Tres Spicy', 1);

        COMMIT;
        
    EXCEPTION
        WHEN OTHERS THEN
            ROLLBACK;
            DBMS_OUTPUT.PUT_LINE('Eroare: ' || SQLERRM);    
END;
/