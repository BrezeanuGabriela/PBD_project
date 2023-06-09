select * from client;
select * from masina;
select * from sofer;
select * from comanda;
select * from tipuri_pizza;
select * from com_pizza_fk;
select * from card_fidelitate;

--tranzactii
--insert in comanda, com_pizza_fk(tip pizza si cantitatea) si update la numarul de puncte de pe cardul clientului
insert into comanda (data_comanda, id_client, onorata,id_sofer, pos) values (sysdate,1,0,1,0);
insert into com_pizza_fk (comanda_id_comanda,tipuri_pizza_id_pizza, cantitate) values (comanda_id_comanda_seq.currval,1,1);
update card_fidelitate set nr_puncte=nr_puncte+0.1*
    (select pret from tipuri_pizza, com_pizza_fk c 
                    where c.comanda_id_comanda=1 and id_pizza=c.tipuri_pizza_id_pizza) where id_client=1;

insert into comanda (data_comanda, id_client, onorata,id_sofer, pos) values (sysdate, 2,0,4,0);
insert into com_pizza_fk (comanda_id_comanda,tipuri_pizza_id_pizza, cantitate) values (comanda_id_comanda_seq.currval,3,1);
update card_fidelitate set nr_puncte=nr_puncte+0.1*
    (select pret from tipuri_pizza, com_pizza_fk c 
                    where c.comanda_id_comanda=2 and id_pizza=c.tipuri_pizza_id_pizza) where id_client=2;

insert into comanda (data_comanda, id_client, onorata,id_sofer, pos) values (sysdate, 3,0,2,0);
insert into com_pizza_fk (comanda_id_comanda,tipuri_pizza_id_pizza, cantitate) values (comanda_id_comanda_seq.currval,1,1);
update card_fidelitate set nr_puncte=nr_puncte+0.1*
    (select pret from tipuri_pizza, com_pizza_fk c 
                    where c.comanda_id_comanda=3 and id_pizza=c.tipuri_pizza_id_pizza) where id_client=3;

insert into comanda (data_comanda, id_client, onorata,id_sofer, pos) values (sysdate, 4,0,4,0);
insert into com_pizza_fk (comanda_id_comanda,tipuri_pizza_id_pizza, cantitate) values (comanda_id_comanda_seq.currval,4,1);
update card_fidelitate set nr_puncte=nr_puncte+0.1*
    (select pret from tipuri_pizza, com_pizza_fk c 
                    where c.comanda_id_comanda=4 and id_pizza=c.tipuri_pizza_id_pizza) where id_client=4;

insert into comanda (data_comanda, id_client, onorata,id_sofer, pos) values (sysdate, 5,0,3,0);
insert into com_pizza_fk (comanda_id_comanda,tipuri_pizza_id_pizza, cantitate) values (comanda_id_comanda_seq.currval,6,2);
update card_fidelitate set nr_puncte=nr_puncte+0.1*
    (select pret from tipuri_pizza, com_pizza_fk c 
                    where c.comanda_id_comanda=5 and id_pizza=c.tipuri_pizza_id_pizza) where id_client=5;

insert into comanda (data_comanda, id_client, onorata,id_sofer, pos) values (sysdate, 6,0,5,0);
insert into com_pizza_fk (comanda_id_comanda,tipuri_pizza_id_pizza, cantitate) values (comanda_id_comanda_seq.currval,5,1);
update card_fidelitate set nr_puncte=nr_puncte+0.1*
    (select pret from tipuri_pizza, com_pizza_fk c 
                    where c.comanda_id_comanda=6 and id_pizza=c.tipuri_pizza_id_pizza) where id_client=6;

insert into comanda (data_comanda, id_client, onorata,id_sofer, pos) values (sysdate, 7,0,1,1);
insert into com_pizza_fk (comanda_id_comanda,tipuri_pizza_id_pizza, cantitate) values (comanda_id_comanda_seq.currval,2,1);
update card_fidelitate set nr_puncte=nr_puncte+0.1*
    (select pret from tipuri_pizza, com_pizza_fk c 
                    where c.comanda_id_comanda=7 and id_pizza=c.tipuri_pizza_id_pizza) where id_client=7;

insert into comanda (data_comanda, id_client, onorata,id_sofer, pos) values (sysdate, 8,0,1,1);
insert into com_pizza_fk (comanda_id_comanda,tipuri_pizza_id_pizza, cantitate) values (comanda_id_comanda_seq.currval,1,1);
update card_fidelitate set nr_puncte=nr_puncte+0.1*
    (select pret from tipuri_pizza, com_pizza_fk c 
                    where c.comanda_id_comanda=8 and id_pizza=c.tipuri_pizza_id_pizza) where id_client=8;

insert into comanda (data_comanda, id_client, onorata,id_sofer, pos) values (sysdate, 9,0,2,1);
insert into com_pizza_fk (comanda_id_comanda,tipuri_pizza_id_pizza, cantitate) values (comanda_id_comanda_seq.currval,2,1);
update card_fidelitate set nr_puncte=nr_puncte+0.1*
    (select pret from tipuri_pizza, com_pizza_fk c 
                    where c.comanda_id_comanda=9 and id_pizza=c.tipuri_pizza_id_pizza) where id_client=9;

insert into comanda (data_comanda, id_client, onorata,id_sofer, pos) values (sysdate, 1,0,6,0);
insert into com_pizza_fk (comanda_id_comanda,tipuri_pizza_id_pizza, cantitate) values (comanda_id_comanda_seq.currval,6,3);
update card_fidelitate set nr_puncte=nr_puncte+0.1*
    (select pret from tipuri_pizza, com_pizza_fk c 
                    where c.comanda_id_comanda=10 and id_pizza=c.tipuri_pizza_id_pizza) where id_client=1;

insert into comanda (data_comanda, id_client, onorata,id_sofer, pos) values (sysdate, 3,0,3,1);
insert into com_pizza_fk (comanda_id_comanda,tipuri_pizza_id_pizza, cantitate) values (comanda_id_comanda_seq.currval,5,2);
update card_fidelitate set nr_puncte=nr_puncte+0.1*
    (select pret from tipuri_pizza, com_pizza_fk c 
                    where c.comanda_id_comanda=11 and id_pizza=c.tipuri_pizza_id_pizza) where id_client=3;

insert into comanda (data_comanda, id_client, onorata,id_sofer, pos) values (sysdate, 6,0,5,0);
insert into com_pizza_fk (comanda_id_comanda,tipuri_pizza_id_pizza, cantitate) values (comanda_id_comanda_seq.currval,4,4);
update card_fidelitate set nr_puncte=nr_puncte+0.1*
    (select pret from tipuri_pizza, com_pizza_fk c 
                    where c.comanda_id_comanda=12 and id_pizza=c.tipuri_pizza_id_pizza) where id_client=6;

insert into comanda (data_comanda, id_client, onorata,id_sofer, pos) values (sysdate, 9,0,2,1);
insert into com_pizza_fk (comanda_id_comanda,tipuri_pizza_id_pizza, cantitate) values (comanda_id_comanda_seq.currval,3,2);
update card_fidelitate set nr_puncte=nr_puncte+0.1*
    (select pret from tipuri_pizza, com_pizza_fk c 
                    where c.comanda_id_comanda=13 and id_pizza=c.tipuri_pizza_id_pizza) where id_client=9;

--comanda cu 2 tipuri de pizza comandate
insert into comanda (data_comanda, id_client, onorata,id_sofer, pos) values (sysdate, 6,0,6,0);
insert into com_pizza_fk (comanda_id_comanda,tipuri_pizza_id_pizza, cantitate) values (comanda_id_comanda_seq.currval,2,2);
update card_fidelitate set nr_puncte=nr_puncte+0.1*
        (select pret from tipuri_pizza, com_pizza_fk c 
                        where c.comanda_id_comanda=14 and id_pizza=c.tipuri_pizza_id_pizza) 
    where id_client=6;
insert into com_pizza_fk (comanda_id_comanda,tipuri_pizza_id_pizza, cantitate) values (comanda_id_comanda_seq.currval,4,3);

update card_fidelitate set nr_puncte=nr_puncte+0.1*
    (select (select pret from tipuri_pizza tip where tip.id_pizza=4) *
    (select cantitate from com_pizza_fk c where c.comanda_id_comanda=14 and tipuri_pizza_id_pizza=4) pret_c from dual)
    where id_client=6;

--costul total pe fiecare comanda
with 
 com_pret_pizza as (
     select comanda_id_comanda, tipuri_pizza_id_pizza, pret,cantitate, pret*cantitate pret_pizza
        from tipuri_pizza tip, com_pizza_fk comd 
        where tip.id_pizza=comd.tipuri_pizza_id_pizza)
        
    select distinct comanda_id_comanda, (select sum(pret_pizza) from com_pret_pizza c where c.comanda_id_comanda=c1.comanda_id_comanda) pret_total 
    from com_pret_pizza c1 group by comanda_id_comanda, pret_pizza order by comanda_id_comanda;

--rest de plata din costul total al unei comenzi daca ar alege clientul sa utilizeze numarul de puncte de pe card
with 
 com_pret_pizza as (
     select comanda_id_comanda, tipuri_pizza_id_pizza, pret,cantitate, pret*cantitate pret_pizza
        from tipuri_pizza tip, com_pizza_fk comd 
        where tip.id_pizza=comd.tipuri_pizza_id_pizza)
        
    select distinct comanda_id_comanda, (select card.id_client from card_fidelitate card,comanda cmd where cmd.id_comanda=c1.comanda_id_comanda and cmd.id_client=card.id_client) id_client,
                                        (select sum(pret_pizza) from com_pret_pizza c where c.comanda_id_comanda=c1.comanda_id_comanda) pret_total,
                                        (select nr_puncte from card_fidelitate card,comanda cmd where cmd.id_comanda=c1.comanda_id_comanda and cmd.id_client=card.id_client) puncte_client,
                                        (select sum(pret_pizza) from com_pret_pizza c where c.comanda_id_comanda=c1.comanda_id_comanda) -
                                        (select nr_puncte from card_fidelitate card,comanda cmd where cmd.id_comanda=c1.comanda_id_comanda and cmd.id_client=card.id_client) rest_plata_puncte_folosite                               
    from com_pret_pizza c1 group by comanda_id_comanda, pret_pizza order by comanda_id_comanda;

--un fel de bon, in sensul ca se va afisa id_client, id_comanda, tipul/tipurile de pizza comandate, pretul si cantitatea pentru fiecare tip, 
--pretul pentru acelasi tip de pizza daca a comandat mai multe bucati si costul total
with 
    com_pret_pizza as (
        select comanda_id_comanda, tipuri_pizza_id_pizza, pret,cantitate, pret*cantitate pret_pizza
        from tipuri_pizza tip, com_pizza_fk comd 
        where tip.id_pizza=comd.tipuri_pizza_id_pizza),
    pret_final as (
        select distinct comanda_id_comanda, (select sum(pret_pizza) from com_pret_pizza c where c.comanda_id_comanda=c1.comanda_id_comanda) pret_total 
        from com_pret_pizza c1 group by comanda_id_comanda, pret_pizza)
    
    select id_client, c.comanda_id_comanda,tipuri_pizza_id_pizza, pret, cantitate, pret_pizza, pret_total cost_total_comanda
    from com_pret_pizza c, pret_final p, comanda cmd 
    where c.comanda_id_comanda=p.comanda_id_comanda 
        and cmd.id_comanda=c.comanda_id_comanda 
    order by comanda_id_comanda;

select * from card_fidelitate;
select * from com_pizza_fk;
select * from tipuri_pizza;

--evidenta comenzilor pe cartiere
select cartier,count(cartier) nr_comenzi_pe_cartier from client group by cartier;

--numarul de comenzi date de fiecare client
select c.id_client,
    (select nume from client cl where cl.id_client=c.id_client) nume,
    (select prenume from client cl where cl.id_client=c.id_client) prenume, 
    count(*) nr_comenzi_client 
    from comanda c group by id_client order by id_client; 

--numarul de comenzi livrate de fiecare sofer    
select id_sofer, 
    (select nume from sofer where id_sofer=c.id_sofer) nume,
    (select prenume from sofer where id_sofer=c.id_sofer) prenume,
    count(id_sofer) nr_comenzi_preluate from comanda c group by id_sofer order by id_sofer;

--varsta soferilor    
select abs(21-min(to_number(substr(cnp,2,2)))) varsta_soferi from sofer group by cnp having to_number(substr(cnp, 2,2))=min(to_number(substr(cnp,2,2)));

--soferul cel mai tanar si cel mai in varsta
select abs(21-min(to_number(substr(cnp,2,2)))) cel_mai_tanar_sofer, abs(21-max(to_number(substr(cnp,2,2)))) cel_mai_in_varsta_sofer  from sofer;

--clientul/clientii cu cele mai multe comenzi date
with 
    nr_comenzi_max as (select max(count(*)) nr_max_comenzi from comanda group by id_client),
    nr_comenzi_client as (select id_client, count(*) nr_comenzi from comanda group by id_client)
    select c.id_client, c.nume, c.prenume, nr_max_comenzi from client c, nr_comenzi_max nr_max, nr_comenzi_client nr_client where  c.id_client=nr_client.id_client and nr_comenzi=nr_max_comenzi;

--evidenta preferintelor clientilor in materie de pizza    
select tipuri_pizza_id_pizza, count(*) nr_pizza_vandute  from com_pizza_fk group by tipuri_pizza_id_pizza order by nr_pizza_vandute desc;

--bonus soferi muncitori
select id_sofer, count(*) nr_comenzi from comanda group by id_sofer order by nr_comenzi desc;
update sofer s set salariu=salariu + 5 * (select count(*) from comanda where s.id_sofer=id_sofer group by id_sofer) where 2<(select count(*) from comanda where s.id_sofer=id_sofer group by id_sofer);
    
select * from client;
select * from masina;
select * from sofer;
select * from comanda;
select * from tipuri_pizza;
select * from com_pizza_fk;
select * from card_fidelitate;

commit;
