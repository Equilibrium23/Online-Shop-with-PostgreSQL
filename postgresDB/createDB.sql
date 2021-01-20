DROP SCHEMA project cascade;
CREATE SCHEMA project;
CREATE TABLE project.pracownik (
                id_pracownik SERIAL NOT NULL,
                imie VARCHAR NOT NULL,
                nazwisko VARCHAR NOT NULL,
                email VARCHAR NOT NULL,
                login VARCHAR NOT NULL,
                haslo VARCHAR NOT NULL,
                uprawnienia VARCHAR NOT NULL,
                data_zatrudnienia DATE NOT NULL,
                stanowisko VARCHAR NOT NULL,
                CONSTRAINT pracownik_pk PRIMARY KEY (id_pracownik)
);


CREATE TABLE project.producent (
                id_producent INTEGER NOT NULL,
                nazwa VARCHAR NOT NULL,
                adres_firmy VARCHAR NOT NULL,
                NIP VARCHAR NOT NULL,
                email VARCHAR NOT NULL,
                nr_telefonu VARCHAR NOT NULL,
                CONSTRAINT producent_pk PRIMARY KEY (id_producent)
);


CREATE TABLE project.typ_dostawy (
                id_typu_dostawy SERIAL NOT NULL,
                nazwa_dostawy VARCHAR NOT NULL,
                cena_dostawy DOUBLE PRECISION NOT NULL,
                firma_oblugujaca VARCHAR NOT NULL,
                CONSTRAINT typ_dostawy_pk PRIMARY KEY (id_typu_dostawy)
);


CREATE TABLE project.klient (
                id_klient SERIAL NOT NULL,
                typ_uzytkownika VARCHAR NOT NULL,
                imie VARCHAR NOT NULL,
                nazwisko VARCHAR NOT NULL,
                login VARCHAR NOT NULL,
                haslo VARCHAR NOT NULL,
                email VARCHAR NOT NULL,
                CONSTRAINT id PRIMARY KEY (id_klient),
                UNIQUE (login,email)
);


CREATE TABLE project.zwrot (
                id_zwrot INTEGER NOT NULL,
                id_klient INTEGER NOT NULL,
                sposob_zwrotu INTEGER NOT NULL,
                id_produktu INTEGER NOT NULL,
                powod_zwrotu VARCHAR NOT NULL,
                typ_zwrotu VARCHAR NOT NULL,
                status_zwrotu VARCHAR NOT NULL,
                CONSTRAINT zwrot_pk PRIMARY KEY (id_zwrot)
);


CREATE TABLE project.adres (
                id_adres SERIAL NOT NULL,
                id_uzytkownik INTEGER NOT NULL,
                ulica VARCHAR NOT NULL,
                miasto VARCHAR NOT NULL,
                kod_pocztowy VARCHAR NOT NULL,
                nr_domu INTEGER NOT NULL,
                nr_mieszkania INTEGER NOT NULL,
                glowny_adres boolean DEFAULT FALSE NOT NULL,
                CONSTRAINT id_adres PRIMARY KEY (id_adres)
);


CREATE TABLE project.zamowienie (
                id_zamowienie INTEGER NOT NULL,
                id_uzytkownika INTEGER NOT NULL,
                dostawa INTEGER NOT NULL,
                status_zamowienia VARCHAR NOT NULL,
                do_zaplaty DOUBLE PRECISION NOT NULL,
                ilosc_produktow INTEGER NOT NULL,
                data_zlozenia DATE NOT NULL,
                CONSTRAINT zamowienie_pk PRIMARY KEY (id_zamowienie)
);


CREATE TABLE project.monitor (
                id_monitor INTEGER NOT NULL,
                id_producent INTEGER NOT NULL,
                nazwa VARCHAR NOT NULL,
                cena DOUBLE PRECISION NOT NULL,
                przekatna_ekranu DOUBLE PRECISION NOT NULL,
                rozdzielczosc VARCHAR NOT NULL,
                odswiezanie INTEGER NOT NULL,
                matryca VARCHAR NOT NULL,
                max_jasnosc INTEGER NOT NULL,
                CONSTRAINT id_monitor PRIMARY KEY (id_monitor)
);

CREATE TABLE project.szczegoly_zwrotu (
                id_szczegoly_zwrotu SERIAL NOT NULL,
                id_monitor INTEGER NOT NULL,
                id_zwrot INTEGER NOT NULL,
                id_szczegoly_zamowienia INTEGER NOT NULL,
                CONSTRAINT szczegoly_zwrotu_pk PRIMARY KEY (id_szczegoly_zwrotu)
);


CREATE TABLE project.szczegoly_zamowienia (
                id_szczegoly_zamowienia SERIAL NOT NULL,
                id_monitor INTEGER NOT NULL,
                id_zamowienie INTEGER NOT NULL,
                ilosc INTEGER NOT NULL,
                CONSTRAINT szczegoly_zamowienia_pk PRIMARY KEY (id_szczegoly_zamowienia)
);


CREATE TABLE project.galeria (
                id_zdjecie INTEGER NOT NULL,
                id_monitora INTEGER NOT NULL,
                nazwa_zdjecia VARCHAR NOT NULL,
                data_dodania DATE NOT NULL,
                kolejnosc_wyswietlania INTEGER NOT NULL,
                CONSTRAINT galeria_pk PRIMARY KEY (id_zdjecie)
);


CREATE TABLE project.ocena (
                id_ocena INTEGER NOT NULL,
                id_autora INTEGER NOT NULL,
                id_produktu INTEGER NOT NULL,
                tekst_oceny VARCHAR,
                ocena DOUBLE PRECISION NOT NULL,
                CONSTRAINT ocena_pk PRIMARY KEY (id_ocena)
);

ALTER TABLE project.monitor ADD CONSTRAINT producent_monitor_fk
FOREIGN KEY (id_producent)
REFERENCES project.producent (id_producent)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE project.zamowienie ADD CONSTRAINT typ_dostawy_zamowienie_fk
FOREIGN KEY (dostawa)
REFERENCES project.typ_dostawy (id_typu_dostawy)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE project.zwrot ADD CONSTRAINT typ_dostawy_zwrot_fk
FOREIGN KEY (sposob_zwrotu)
REFERENCES project.typ_dostawy (id_typu_dostawy)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE project.ocena ADD CONSTRAINT uzytkownik_ocena_fk
FOREIGN KEY (id_autora)
REFERENCES project.klient (id_klient)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE project.zamowienie ADD CONSTRAINT uzytkownik_zamowienie_fk
FOREIGN KEY (id_uzytkownika)
REFERENCES project.klient (id_klient)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE project.adres ADD CONSTRAINT uzytkownik_adres_fk
FOREIGN KEY (id_uzytkownik)
REFERENCES project.klient (id_klient)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE project.zwrot ADD CONSTRAINT klient_zwrot_fk
FOREIGN KEY (id_klient)
REFERENCES project.klient (id_klient)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE project.szczegoly_zwrotu ADD CONSTRAINT zwrot_szczegoly_zwrotu_fk
FOREIGN KEY (id_zwrot)
REFERENCES project.zwrot (id_zwrot)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE project.szczegoly_zamowienia ADD CONSTRAINT zamowienie_szczegoly_zamowienia_fk
FOREIGN KEY (id_zamowienie)
REFERENCES project.zamowienie (id_zamowienie)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE project.ocena ADD CONSTRAINT monitor_ocena_fk
FOREIGN KEY (id_produktu)
REFERENCES project.monitor (id_monitor)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE project.galeria ADD CONSTRAINT monitor_galeria_fk
FOREIGN KEY (id_monitora)
REFERENCES project.monitor (id_monitor)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE project.szczegoly_zamowienia ADD CONSTRAINT monitor_szczegoly_zamowienia_fk
FOREIGN KEY (id_monitor)
REFERENCES project.monitor (id_monitor)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE project.szczegoly_zwrotu ADD CONSTRAINT monitor_szczegoly_zwrotu_fk
FOREIGN KEY (id_monitor)
REFERENCES project.monitor (id_monitor)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;


ALTER TABLE project.szczegoly_zwrotu ADD CONSTRAINT szczeguly_zamowienia_szczegoly_zwrotu_fk
FOREIGN KEY (id_szczegoly_zamowienia)
REFERENCES project.szczegoly_zamowienia (id_szczegoly_zamowienia)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;