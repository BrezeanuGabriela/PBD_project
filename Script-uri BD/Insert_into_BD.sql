insert into client (nume, prenume, telefon, email, cartier, numar_cartier, nr_bloc, etaj, nr_apartament) values ('popescu','ion','0712345678','ion.popescu@gmail.com','dacia',36,3,1,5);
insert into card_fidelitate (id_client, data_nastere_client) values (client_id_client_seq.currval, '25-jan-2000');
insert into client (nume, prenume, telefon, email, cartier, numar_cartier, nr_bloc, etaj, nr_apartament) values ('carp','ana','0778956412','ana.carp@gmail.com','copou',24,78,2,10);
insert into card_fidelitate (id_client, data_nastere_client) values (client_id_client_seq.currval, '25-may-1995');
insert into client (nume, prenume, telefon, email, cartier, numar_cartier, nr_bloc, etaj, nr_apartament) values ('toma','alexandra','0745802031','toma.alexandra@gmail.com','tatarasi',30,85,0,1);
insert into card_fidelitate (id_client, data_nastere_client) values (client_id_client_seq.currval, '3-mar-1984');
insert into client (nume, prenume, telefon, email, cartier, numar_cartier, nr_bloc, etaj, nr_apartament) values ('mihnea','andrei','0745987451','andrei.m@yahoo.com','galata',55,41,1,7);
insert into card_fidelitate (id_client, data_nastere_client) values (client_id_client_seq.currval, '12-oct-1975');
insert into client (nume, prenume, telefon, email, cartier, numar_cartier, nr_bloc, etaj, nr_apartament) values ('apetrei','sergiu','0736802031','sergiu.apetrei@gmail.com','cug',93,124,6,25);
insert into card_fidelitate (id_client, data_nastere_client) values (client_id_client_seq.currval, '30-dec-2001');
insert into client (nume, prenume, telefon, email, cartier, numar_cartier, nr_bloc, etaj, nr_apartament) values ('toma','bogdan','0734516781','toma.bogdan@gmail.com','alexandru cel bun',67,4,8,35);
insert into card_fidelitate (id_client, data_nastere_client) values (client_id_client_seq.currval, '7-jun-1982');
insert into client (nume, prenume, telefon, email, cartier, numar_cartier, nr_bloc, etaj, nr_apartament) values ('ciulin','mihai','0758412367','ciulin.mihai@gmail.com','galata',72,12,3,14);
insert into card_fidelitate (id_client, data_nastere_client) values (client_id_client_seq.currval, '5-nov-1999');
insert into client (nume, prenume, telefon, email, cartier, numar_cartier, nr_bloc, etaj, nr_apartament) values ('olaru','andreea','0756271389','andreea.olaru@gmail.com','dacia',2,1,0,1);
insert into card_fidelitate (id_client, data_nastere_client) values (client_id_client_seq.currval, '12-aug-1992');
insert into client (nume, prenume, telefon, email, cartier, numar_cartier, nr_bloc, etaj, nr_apartament) values ('albert','diana','0754926437','albert.diana@gmail.com','dacia',104,512,2,8);
insert into card_fidelitate (id_client, data_nastere_client) values (client_id_client_seq.currval, '10-sep-1973');

insert into masina values('IS 21 OUL', 'VW', 'UP 1', 2013);
insert into masina values('IS 56 XSD', 'VW', 'UP 1', 2013);
insert into masina values('IS 14 MEN', 'VW', 'UP 1', 2013);
insert into masina values('IS 37 MMM', 'VW', 'UP 1', 2013);
insert into masina values('IS 85 HJF', 'VW', 'UP 1', 2013);
insert into masina values('IS 75 AIR', 'VW', 'UP 1', 2014);
insert into masina values('IS 52 BRT', 'VW', 'UP 1', 2014);
insert into masina values('IS 28 TAI', 'VW', 'UP 1', 2014);

insert into sofer (nume, prenume, cnp, telefon, email, salariu, pos,numar_masina) values ('costel','gigel',5000530456789,'0772345678','costel@yahoo.com',2000,1,'IS 21 OUL');
insert into sofer (nume, prenume, cnp, telefon, email, salariu, pos,numar_masina) values ('tiberiu','alexandru',5960825361489,'0769587412','alex.tibi@yahoo.com',2500,1,'IS 37 MMM');
insert into sofer (nume, prenume, cnp, telefon, email, salariu, pos,numar_masina) values ('florea','andrei',5871221475896,'0724156378','florea.andrei@yahoo.com',2000,1,'IS 75 AIR');
insert into sofer (nume, prenume, cnp, telefon, email, salariu, pos,numar_masina) values ('marian','costel',5000412695764,'0775236498','costi.marian@yahoo.com',1500,0,'IS 85 HJF');
insert into sofer (nume, prenume, cnp, telefon, email, salariu, pos,numar_masina) values ('matei','bogdan',5760824917325,'0757854123','matei.bogdan@yahoo.com',2600,0,'IS 28 TAI');
insert into sofer (nume, prenume, cnp, telefon, email, salariu, pos,numar_masina) values ('enache','stefan',5840614164375,'0746915273','enache.stefan@yahoo.com',2000,0,'IS 56 XSD');

insert into tipuri_pizza (denumire, gramaj, pret) values ('mammaMia', 560,35);
insert into tipuri_pizza (denumire, gramaj, pret) values ('quatroFormaggi', 400,30);
insert into tipuri_pizza (denumire, gramaj, pret) values ('conTonno', 500,40);
insert into tipuri_pizza (denumire, gramaj, pret) values ('margherita', 560,28);
insert into tipuri_pizza (denumire, gramaj, pret) values ('mammaMia', 1500,80);
insert into tipuri_pizza (denumire, gramaj, pret) values ('conPollo', 560,37);


