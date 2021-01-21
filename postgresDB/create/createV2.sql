create schema project;

create table project.pracownik
(
	id_pracownik serial not null
		constraint pracownik_pk
			primary key,
	imie varchar not null,
	nazwisko varchar not null,
	email varchar not null,
	login varchar not null,
	haslo varchar not null,
	data_zatrudnienia date not null,
	stanowisko varchar not null
);


create table project.producent
(
	id_producent integer not null
		constraint producent_pk
			primary key,
	nazwa varchar not null,
	adres_firmy varchar not null,
	nip varchar not null,
	email varchar not null,
	nr_telefonu varchar not null
);


create table project.typ_dostawy
(
	id_typu_dostawy serial not null
		constraint typ_dostawy_pk
			primary key,
	nazwa_dostawy varchar not null,
	cena_dostawy double precision not null,
	firma_oblugujaca varchar not null
);


create table project.klient
(
	id_klient serial not null
		constraint id
			primary key,
	typ_uzytkownika varchar not null,
	imie varchar not null,
	nazwisko varchar not null,
	login varchar not null,
	haslo varchar not null,
	email varchar not null,
	constraint klient_login_email_key
		unique (login, email)
);


create table project.zwrot
(
	id_zwrot integer not null
		constraint zwrot_pk
			primary key,
	id_klient integer not null
		constraint klient_zwrot_fk
			references project.klient,
	sposob_zwrotu integer not null
		constraint typ_dostawy_zwrot_fk
			references project.typ_dostawy,
	powod_zwrotu varchar not null,
	typ_zwrotu varchar not null,
	status_zwrotu varchar not null
);


create table project.monitor
(
	id_monitor integer not null
		constraint id_monitor
			primary key,
	id_producent integer not null
		constraint producent_monitor_fk
			references project.producent,
	nazwa varchar not null,
	cena double precision not null,
	przekatna_ekranu double precision not null,
	rozdzielczosc varchar not null,
	odswiezanie integer not null,
	matryca varchar not null,
	max_jasnosc integer not null
);


create table project.galeria
(
	id_zdjecie serial not null
		constraint galeria_pk
			primary key,
	id_monitora integer not null
		constraint monitor_galeria_fk
			references project.monitor,
	nazwa_zdjecia varchar not null,
	data_dodania date not null
);


create table project.zamowienie
(
	id_zamowienie serial not null
		constraint zamowienie_pk
			primary key,
	id_uzytkownika integer not null
		constraint uzytkownik_zamowienie_fk
			references project.klient,
	dostawa integer not null
		constraint typ_dostawy_zamowienie_fk
			references project.typ_dostawy,
	status_zamowienia varchar not null,
	do_zaplaty double precision not null,
	ilosc_produktow integer not null,
	data_zlozenia date not null
);


create table project.koszyk
(
	id serial not null
		constraint koszyk_pk
			primary key,
	id_uzytkownik integer not null
		constraint uzytkownik_koszyk_fk
			references project.klient,
	id_monitor integer not null
		constraint monitor_koszyk_fk
			references project.monitor,
	cena double precision not null,
	ilosc integer default 1 not null
);


create table project.ocena
(
	id_ocena serial not null
		constraint ocena_pk
			primary key,
	id_autora integer not null
		constraint uzytkownik_ocena_fk
			references project.klient,
	id_produktu integer not null
		constraint monitor_ocena_fk
			references project.monitor,
	tekst_oceny varchar,
	ocena double precision not null
);


create table project.szczegoly_zamowienia
(
	id_szczegoly_zamowienia serial not null
		constraint szczegoly_zamowienia_pk
			primary key,
	id_monitor integer not null
		constraint monitor_szczegoly_zamowienia_fk
			references project.monitor,
	id_zamowienie integer not null
		constraint zamowienie_szczegoly_zamowienia_fk
			references project.zamowienie,
	ilosc integer not null
);


create table project.szczegoly_zwrotu
(
	id_szczegoly_zwrotu serial not null
		constraint szczegoly_zwrotu_pk
			primary key,
	id_monitor integer not null
		constraint monitor_szczegoly_zwrotu_fk
			references project.monitor,
	id_zwrot integer not null
		constraint zwrot_szczegoly_zwrotu_fk
			references project.zwrot,
	id_szczegoly_zamowienia integer not null
		constraint szczeguly_zamowienia_szczegoly_zwrotu_fk
			references project.szczegoly_zamowienia
);


create table project.adres
(
	id_adres serial not null
		constraint id_adres
			primary key,
	id_uzytkownik integer not null
		constraint uzytkownik_adres_fk
			references project.klient,
	ulica varchar not null,
	miasto varchar not null,
	kod_pocztowy varchar not null,
	nr_domu integer not null,
	nr_mieszkania integer not null,
	glowny_adres boolean default false not null
);

CREATE SEQUENCE project.msi_id_generator INCREMENT 1 MINVALUE 100 MAXVALUE 199;

CREATE SEQUENCE project.benq_id_generator INCREMENT 1 MINVALUE 200 MAXVALUE 299;

CREATE SEQUENCE project.acer_id_generator INCREMENT 1 MINVALUE 300 MAXVALUE 399;

CREATE SEQUENCE project.samsung_id_generator INCREMENT 1 MINVALUE 400 MAXVALUE 499;

CREATE SEQUENCE project.iiyama_id_generator INCREMENT 1 MINVALUE 500 MAXVALUE 599;

CREATE SEQUENCE project.aoc_id_generator INCREMENT 1 MINVALUE 600 MAXVALUE 699;

CREATE SEQUENCE project.lg_id_generator INCREMENT 1 MINVALUE 700 MAXVALUE 799;

CREATE SEQUENCE project.seq_zamowienie START 1 INCREMENT 1;

CREATE SEQUENCE project.seq_zwrot START 1 INCREMENT 1;


create function pobierz_koszyk(user_id integer) returns TABLE(nazwa text, ilosc integer, cena_jednostkowa double precision, suma double precision)
language sql
as 
$$
	SELECT m.nazwa,k.ilosc ilosc,m.cena as cena_jednostkowa,k.cena as suma FROM project.koszyk k,project.monitor m WHERE k.id_monitor = m.id_monitor AND k.id_uzytkownik = user_id;
$$;

create function pobierz_typy_dostawy() returns SETOF text
language plpgsql
as
$$
	DECLARE
        row RECORD;
    BEGIN
        FOR row IN SELECT nazwa_dostawy,cena_dostawy,firma_oblugujaca FROM project.typ_dostawy ORDER BY cena_dostawy
        LOOP
            RETURN next row.nazwa_dostawy ||' ' || row.firma_oblugujaca || ' cena: ' || row.cena_dostawy; 
        END LOOP;
    END;
$$;


create function utworz_zamowienie(id_uzytkownika integer, id_dostawy integer, suma double precision, data date, status character varying) returns void
language plpgsql
as
$$
	DECLARE
        wiersz RECORD;
        ilosc_przedmiotow bigint;
        suma_z_dostawa double precision;
        id_zamowienie INTEGER;
    BEGIN
        SELECT into id_zamowienie nextval('project.seq_zamowienie');

        suma_z_dostawa := (SELECT cena_dostawy FROM project.typ_dostawy WHERE id_typu_dostawy = id_dostawy);
        suma_z_dostawa = suma_z_dostawa + suma;
        ilosc_przedmiotow = COUNT(*) FROM project.koszyk WHERE id_uzytkownik = id_uzytkownika;
        INSERT INTO project.zamowienie VALUES(id_zamowienie,id_uzytkownika,id_dostawy,status,suma_z_dostawa,ilosc_przedmiotow,data);

        FOR wiersz IN SELECT id_monitor,ilosc FROM project.koszyk WHERE id_uzytkownik = id_uzytkownika
        LOOP
            INSERT INTO project.szczegoly_zamowienia VALUES(DEFAULT,wiersz.id_monitor,id_zamowienie,wiersz.ilosc);
        END LOOP;
    END;
$$;

CREATE OR REPLACE FUNCTION utworz_zwrot(id_uzytkownika INTEGER,id_dostawy INTEGER, powod text, id_przedmiotu INTEGER, id_szczegoly_zamowienia INTEGER, typ_zwrotu text)
RETURNS void AS
$$   
    DECLARE
        id_zwrot INTEGER;
    BEGIN
        SELECT into id_zwrot nextval('project.seq_zwrot');
        INSERT INTO project.zwrot VALUES(id_zwrot,id_uzytkownika,id_dostawy,powod,typ_zwrotu,'W trakcie realizacji');
        INSERT INTO project.szczegoly_zwrotu VALUES(DEFAULT,id_przedmiotu,id_zwrot,id_szczegoly_zamowienia);
    END; 
$$ LANGUAGE plpgsql;
