-- Generated by Oracle SQL Developer Data Modeler 21.2.0.183.1957
--   at:        2021-12-16 18:31:58 EET
--   site:      Oracle Database 12c
--   type:      Oracle Database 12c



-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE client (
    id_client     NUMBER(5) NOT NULL,
    nume          VARCHAR2(30) NOT NULL,
    prenume       VARCHAR2(30) NOT NULL,
    telefon       VARCHAR2(10) NOT NULL,
    email         VARCHAR2(60) NOT NULL,
    cartier       VARCHAR2(30) NOT NULL,
    numar_cartier NUMBER(3) NOT NULL,
    nr_bloc       NUMBER(3),
    etaj          NUMBER(2),
    nr_apartament NUMBER(3)
)
LOGGING;

ALTER TABLE client ADD CHECK ( id_client BETWEEN 1 AND 99999 );

ALTER TABLE client
    ADD CONSTRAINT client_nume_ck CHECK ( length(nume) > 1
                                          AND REGEXP_LIKE ( nume,
                                                            '^[A-Za-z]+$' ) );

ALTER TABLE client
    ADD CONSTRAINT client_prenume_ck CHECK ( length(prenume) > 1
                                             AND REGEXP_LIKE ( prenume,
                                                               '^[A-Za-z]+$' ) );

ALTER TABLE client
    ADD CONSTRAINT client_telefon_ck CHECK ( REGEXP_LIKE ( telefon,
                                                           '^07[0-9]{8}$' ) );

ALTER TABLE client
    ADD CONSTRAINT client_email_ck CHECK ( REGEXP_LIKE ( email,
                                                         '[a-z0-9._%-]+@[a-z0-9._%-]+\.[a-z]{2,4}' ) );

ALTER TABLE client
    ADD CONSTRAINT client_cartier_ck CHECK ( length(cartier) > 1
                                             AND REGEXP_LIKE ( cartier,
                                                               '^[A-Za-z+$]' ) );

ALTER TABLE client
    ADD CONSTRAINT client_numar_cartier_ck CHECK ( REGEXP_LIKE ( numar_cartier,
                                                                 '^[0-9]+$' )
                                                   OR numar_cartier BETWEEN 1 AND 999 );

ALTER TABLE client
    ADD CONSTRAINT client_nr_bloc_ck CHECK ( REGEXP_LIKE ( nr_bloc,
                                                           '^[0-9]+$' )
                                             OR nr_bloc BETWEEN 1 AND 999 );

ALTER TABLE client
    ADD CONSTRAINT client_etaj_ck CHECK ( REGEXP_LIKE ( etaj,
                                                        '^[0-9]+$' )
                                          AND etaj BETWEEN 0 AND 10 );

ALTER TABLE client
    ADD CONSTRAINT client_nr_apartament_ck CHECK ( REGEXP_LIKE ( nr_apartament,
                                                                 '^[0-9]+$' )
                                                   OR nr_apartament BETWEEN 1 AND 999 );

ALTER TABLE client ADD CONSTRAINT client_pk PRIMARY KEY ( id_client );

ALTER TABLE client ADD CONSTRAINT client_email_uk UNIQUE ( email );

ALTER TABLE client ADD CONSTRAINT client_telefon_uk UNIQUE ( telefon );

CREATE TABLE card_fidelitate (
    id_client           NUMBER(5) NOT NULL,
    id_card             NUMBER(5) NOT NULL,
    data_nastere_client DATE,
    nr_puncte           NUMBER DEFAULT 0 NOT NULL
)
LOGGING;

ALTER TABLE card_fidelitate ADD CONSTRAINT card_fidelitate_pk PRIMARY KEY ( id_client );

ALTER TABLE card_fidelitate ADD CONSTRAINT "client.id_card_uk" UNIQUE ( id_card );

ALTER TABLE card_fidelitate
    ADD CONSTRAINT client_card_fidelitate_fk FOREIGN KEY ( id_client )
        REFERENCES client ( id_client )
    NOT DEFERRABLE;

CREATE TABLE com_pizza_fk (
    comanda_id_comanda    NUMBER(5) NOT NULL,
    tipuri_pizza_id_pizza NUMBER(2) NOT NULL,
    cantitate             NUMBER(2)
)
LOGGING;

ALTER TABLE com_pizza_fk ADD CONSTRAINT com_pizza_fk_pk PRIMARY KEY ( comanda_id_comanda,
                                                                      tipuri_pizza_id_pizza );

CREATE TABLE comanda (
    id_client    NUMBER(5) NOT NULL,
    id_comanda   NUMBER(5) NOT NULL,
    data_comanda DATE NOT NULL,
    onorata      NUMBER(1) DEFAULT 0,
    id_sofer     NUMBER(2) NOT NULL,
    pos          NUMBER(1) DEFAULT 0,
    nr_bon       NUMBER(5) NOT NULL
)
LOGGING;

ALTER TABLE comanda ADD CONSTRAINT comanda_data_ck CHECK ( data_comanda >= '10-feb-2021' );

ALTER TABLE comanda
    ADD CONSTRAINT comanda_onorata_ck CHECK ( onorata IN ( 0, 1 ) );

ALTER TABLE comanda
    ADD CONSTRAINT comanda_pos_ck CHECK ( pos IN ( 0, 1 ) );

ALTER TABLE comanda ADD CONSTRAINT comanda_pk PRIMARY KEY ( id_comanda );

ALTER TABLE comanda ADD CONSTRAINT bon_uk UNIQUE ( nr_bon );

ALTER TABLE comanda ADD CONSTRAINT com_sofer_ik UNIQUE ( id_comanda,
                                                         id_sofer );


CREATE TABLE masina (
    numar_masina  VARCHAR2(11) NOT NULL,
    marca         VARCHAR2(20) NOT NULL,
    model         VARCHAR2(20) NOT NULL,
    an_fabricatie NUMBER(4) NOT NULL
)
LOGGING;

ALTER TABLE masina
    ADD CONSTRAINT masina_numar_mas_ck CHECK ( REGEXP_LIKE ( numar_masina,
                                                             '^[A-Z]{2}\s[0-9]{2}\s[A-Z]{3}$' ) );

ALTER TABLE masina
    ADD CONSTRAINT masina_marca_ck CHECK ( REGEXP_LIKE ( marca,
                                                         '^[a-zA-Z]+$' )
                                           AND length(marca) > 1 );

ALTER TABLE masina
    ADD CONSTRAINT masina_model_ck CHECK ( REGEXP_LIKE ( model,
                                                         '^[a-zA-Z]+\s+[0-9]+$' )
                                           AND length(model) > 1 );

ALTER TABLE masina
    ADD CONSTRAINT masina_an_fab_ck CHECK ( REGEXP_LIKE ( an_fabricatie,
                                                          '^[0-9]{4}$' )
                                            OR an_fabricatie BETWEEN 2010 AND 2021 );

ALTER TABLE masina ADD CONSTRAINT masina_pk PRIMARY KEY ( numar_masina );

CREATE TABLE sofer (
    id_sofer     NUMBER(2)
        GENERATED BY DEFAULT AS IDENTITY ( START WITH 1 NOCACHE ORDER )
    NOT NULL,
    nume         VARCHAR2(30) NOT NULL,
    prenume      VARCHAR2(30) NOT NULL,
    cnp          NUMBER(13) NOT NULL,
    telefon      VARCHAR2(10) NOT NULL,
    email        VARCHAR2(60) NOT NULL,
    salariu      NUMBER(4) NOT NULL,
    pos          NUMBER(1) DEFAULT 0,
    numar_masina VARCHAR2(11) NOT NULL
)
LOGGING;

ALTER TABLE sofer
    ADD CONSTRAINT sofer_nume_ck CHECK ( length(nume) > 1
                                         AND REGEXP_LIKE ( nume,
                                                           '^[A-Za-z]+$' ) );

ALTER TABLE sofer
    ADD CONSTRAINT sofer_prenume_ck CHECK ( length(prenume) > 1
                                            AND REGEXP_LIKE ( prenume,
                                                              '^[A-Za-z]+$' ) );

ALTER TABLE sofer
    ADD CONSTRAINT sofer_cnp_ck CHECK ( length(cnp) = 13
                                        AND REGEXP_LIKE ( cnp,
                                                          '^[5-6]{1}[0-9]{6}[0-9]{6}$' )
                                        AND abs(21 - to_number(substr(cnp, 2, 2))) >= 18
                                        AND to_number(substr(cnp, 4, 2)) BETWEEN 1 AND 12
                                        AND to_number(substr(cnp, 6, 2)) BETWEEN 1 AND 31 );

ALTER TABLE sofer
    ADD CONSTRAINT sofer_telefon_ck CHECK ( REGEXP_LIKE ( telefon,
                                                          '^07[0-9]{8}$' ) );

ALTER TABLE sofer
    ADD CONSTRAINT sofer_email_ck CHECK ( REGEXP_LIKE ( email,
                                                        '[a-z0-9._%-]+@[a-z0-9._%-]+\.[a-z]{2,4}' ) );

ALTER TABLE sofer
    ADD CONSTRAINT sofer_salariu_ck CHECK ( salariu BETWEEN 0 AND 9999 );

ALTER TABLE sofer
    ADD CONSTRAINT sofer_pos_ck CHECK ( pos IN ( 0, 1 ) );

ALTER TABLE sofer ADD CONSTRAINT sofer_pk PRIMARY KEY ( id_sofer );

ALTER TABLE sofer ADD CONSTRAINT sofer_cnp_uk UNIQUE ( cnp );

ALTER TABLE sofer ADD CONSTRAINT sofer_email_uk UNIQUE ( email );

ALTER TABLE sofer ADD CONSTRAINT sofer_telefon_uk UNIQUE ( telefon );

CREATE TABLE tipuri_pizza (
    id_pizza NUMBER(2)
        GENERATED BY DEFAULT AS IDENTITY ( START WITH 1 NOCACHE ORDER )
    NOT NULL,
    denumire VARCHAR2(20) NOT NULL,
    gramaj   NUMBER(4) NOT NULL,
    pret     NUMBER(2) NOT NULL
)
LOGGING;

ALTER TABLE tipuri_pizza
    ADD CONSTRAINT tipuri_pizza_denumire_ck CHECK ( length(denumire) > 0
                                                    AND REGEXP_LIKE ( denumire,
                                                                      '^[a-zA-Z]+$' ) );

ALTER TABLE tipuri_pizza
    ADD CONSTRAINT tipuri_pizza_gramaj_ck CHECK ( gramaj BETWEEN 0 AND 2000 );

ALTER TABLE tipuri_pizza
    ADD CONSTRAINT tipuri_pizza_pret_ck CHECK ( pret BETWEEN 1 AND 99 );

ALTER TABLE tipuri_pizza ADD CONSTRAINT tipuri_pizza_pk PRIMARY KEY ( id_pizza );

ALTER TABLE comanda
    ADD CONSTRAINT client_comanda_fk FOREIGN KEY ( id_client )
        REFERENCES client ( id_client )
    NOT DEFERRABLE;

ALTER TABLE com_pizza_fk
    ADD CONSTRAINT com_pizza_fk_comanda_fk FOREIGN KEY ( comanda_id_comanda )
        REFERENCES comanda ( id_comanda )
    NOT DEFERRABLE;

ALTER TABLE com_pizza_fk
    ADD CONSTRAINT com_pizza_fk_tipuri_pizza_fk FOREIGN KEY ( tipuri_pizza_id_pizza )
        REFERENCES tipuri_pizza ( id_pizza )
    NOT DEFERRABLE;

ALTER TABLE sofer
    ADD CONSTRAINT masina_sofer_fk FOREIGN KEY ( numar_masina )
        REFERENCES masina ( numar_masina )
    NOT DEFERRABLE;

ALTER TABLE comanda
    ADD CONSTRAINT sofer_comanda_fk FOREIGN KEY ( id_sofer )
        REFERENCES sofer ( id_sofer )
    NOT DEFERRABLE;

CREATE OR REPLACE TRIGGER comanda_date_trg 
    BEFORE INSERT OR UPDATE ON Comanda 
    FOR EACH ROW 
BEGIN
	IF(:new.data_comanda<sysdate)
		THEN
			RAISE_APPLICATION_ERROR(-20001, 'Data invalida:');
	END IF;
END; 
/

CREATE SEQUENCE comanda_nr_bon_seq START WITH 2001 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER comanda_nr_bon_trg BEFORE
    INSERT ON comanda
    FOR EACH ROW
    WHEN ( new.nr_bon IS NULL )
BEGIN
    :new.nr_bon := comanda_nr_bon_seq.nextval;
END;
/

CREATE SEQUENCE card_fidelitate_id_card_seq START WITH 10001 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER card_fidelitate_id_card_trg BEFORE
    INSERT ON card_fidelitate
    FOR EACH ROW
    WHEN ( new.id_card IS NULL )
BEGIN
    :new.id_card := card_fidelitate_id_card_seq.nextval;
END;
/

CREATE SEQUENCE client_id_client_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER client_id_client_trg BEFORE
    INSERT ON client
    FOR EACH ROW
    WHEN ( new.id_client IS NULL )
BEGIN
    :new.id_client := client_id_client_seq.nextval;
END;
/

CREATE SEQUENCE comanda_id_comanda_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER comanda_id_comanda_trg BEFORE
    INSERT ON comanda
    FOR EACH ROW
    WHEN ( new.id_comanda IS NULL )
BEGIN
    :new.id_comanda := comanda_id_comanda_seq.nextval;
END;
/



-- Oracle SQL Developer Data Modeler Summary Report: 
-- 
-- CREATE TABLE                             6
-- CREATE INDEX                             0
-- ALTER TABLE                             45
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           2
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          1
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- TSDP POLICY                              0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
