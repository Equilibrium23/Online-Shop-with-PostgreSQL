DROP schema project cascade;
create schema project;

create table project.pracownik
(
	id_pracownik serial not null
		constraint pracownik_pk
			primary key,
	imie varchar not null,
	nazwisko varchar not null,
	email varchar not null unique,
	login varchar not null unique,
	haslo varchar not null,
	data_zatrudnienia date not null,
	stanowisko varchar not null
);

CREATE SEQUENCE project.default_producent START 100 MAXVALUE 200 INCREMENT 1;

create table project.producent
(
	id_producent integer not null default nextval('project.default_producent')
		constraint producent_pk
			primary key,
	nazwa varchar not null unique,
	adres_firmy varchar not null,
	nip  varchar not null unique,
	email varchar,
	nr_telefonu varchar
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
	imie varchar not null,
	nazwisko varchar not null,
	login  varchar not null unique,
	haslo varchar not null,
	email  varchar not null unique
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
	status_zwrotu varchar not null,
	data_zlozenia date not null

);

CREATE SEQUENCE project.default_monitor START 1 MAXVALUE 99 INCREMENT 1;

create table project.monitor
(
	id_monitor integer not null default nextval('project.default_monitor')
		constraint id_monitor
			primary key,
	id_producent integer not null
		constraint producent_monitor_fk
			references project.producent,
	nazwa  varchar not null unique,
	cena double precision not null,
	przekatna_ekranu double precision not null,
	rozdzielczosc varchar not null,
	odswiezanie integer not null,
	matryca varchar not null,
	max_jasnosc integer not null,
	ilosc integer not null default 100
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
	ilosc INTEGER NOT NULL DEFAULT 1,
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